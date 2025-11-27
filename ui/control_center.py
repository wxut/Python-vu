import sys
import logging
import json
import copy
import os
from typing import Dict, Any, List, Optional
from enum import Enum
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QTableWidget, QTableWidgetItem,
                               QHeaderView, QGroupBox, QTextEdit, QSplitter,
                               QComboBox, QFrame, QScrollArea,
                               QFileDialog, QMessageBox)
from PySide6.QtCore import Qt, QTimer, Signal, QThread
from PySide6.QtGui import QFont, QColor, QPalette

# 导入工作流执行器
from task_workflow.executor import WorkflowExecutor

logger = logging.getLogger(__name__)


class TaskState(Enum):
    """任务状态枚举"""
    IDLE = "等待开始"
    STARTING = "正在启动"
    RUNNING = "正在运行"
    STOPPING = "正在停止"
    STOPPED = "已中断"
    COMPLETED = "已完成"
    FAILED = "执行失败"

class WindowTaskRunner(QThread):
    """为单个窗口运行工作流的线程"""
    status_updated = Signal(str, str)  # window_id, status
    step_updated = Signal(str, str)    # window_id, step_info
    task_completed = Signal(str, bool) # window_id, success

    def __init__(self, window_info, workflow_data, task_modules):
        super().__init__()
        self.window_info = window_info
        self.workflow_data = workflow_data
        self.task_modules = task_modules

        # 状态管理
        self._current_state = TaskState.IDLE
        self._is_running = False
        self._should_stop = False
        self._is_cleaned = False  # 防止重复清理

        # 执行器相关
        self.executor = None
        self.executor_thread = None

        # 窗口ID
        self.window_id = str(window_info.get('hwnd', 'unknown'))

    def _set_state(self, new_state: TaskState, step_info: str = None):
        """设置任务状态并发送信号"""
        if self._current_state != new_state:
            logger.info(f"窗口{self.window_id}状态变更: {self._current_state.value} -> {new_state.value}")
            self._current_state = new_state

            # 发送状态更新信号
            self.status_updated.emit(self.window_id, new_state.value)

            # 发送步骤更新信号
            if step_info:
                self.step_updated.emit(self.window_id, step_info)
            else:
                # 使用默认步骤信息
                default_steps = {
                    TaskState.IDLE: "等待开始",
                    TaskState.STARTING: "正在启动工作流",
                    TaskState.RUNNING: "工作流运行中",
                    TaskState.STOPPING: "正在停止工作流",
                    TaskState.STOPPED: "工作流已中断",
                    TaskState.COMPLETED: "工作流已完成",
                    TaskState.FAILED: "工作流执行失败"
                }
                self.step_updated.emit(self.window_id, default_steps.get(new_state, "未知状态"))

    def _can_transition_to(self, new_state: TaskState) -> bool:
        """检查是否可以转换到新状态"""
        valid_transitions = {
            TaskState.IDLE: [TaskState.STARTING],
            TaskState.STARTING: [TaskState.RUNNING, TaskState.FAILED, TaskState.STOPPING],
            TaskState.RUNNING: [TaskState.STOPPING, TaskState.COMPLETED, TaskState.FAILED],
            TaskState.STOPPING: [TaskState.STOPPED, TaskState.FAILED],
            TaskState.STOPPED: [TaskState.STARTING],  # 可以重新启动
            TaskState.COMPLETED: [TaskState.STARTING],  # 可以重新启动
            TaskState.FAILED: [TaskState.STARTING]  # 可以重新启动
        }

        allowed = valid_transitions.get(self._current_state, [])
        return new_state in allowed

    @property
    def current_state(self) -> TaskState:
        """获取当前状态"""
        return self._current_state

    @property
    def is_running(self) -> bool:
        """检查是否正在运行"""
        return self._current_state in [TaskState.STARTING, TaskState.RUNNING]

    @property
    def can_start(self) -> bool:
        """检查是否可以启动"""
        return self._current_state in [TaskState.IDLE, TaskState.STOPPED, TaskState.COMPLETED, TaskState.FAILED]

    @property
    def can_stop(self) -> bool:
        """检查是否可以停止"""
        return self._current_state in [TaskState.STARTING, TaskState.RUNNING]
        
    def run(self):
        """运行工作流"""
        try:
            # 检查是否可以启动
            if not self.can_start:
                logger.warning(f"窗口{self.window_id}当前状态{self._current_state.value}不允许启动")
                return

            # 设置启动状态
            self._set_state(TaskState.STARTING, "正在初始化工作流")
            self._is_running = True

            window_title = self.window_info.get('title', '未知窗口')
            window_hwnd = self.window_info.get('hwnd', 0)

            if not self.workflow_data:
                self._set_state(TaskState.FAILED, "错误: 未分配工作流")
                self.task_completed.emit(self.window_id, False)
                return

            # 检查工作流格式
            if 'cards' not in self.workflow_data:
                self._set_state(TaskState.FAILED, "错误: 工作流格式不正确")
                self.task_completed.emit(self.window_id, False)
                return

            # 转换数据格式 - 确保键类型一致
            cards_dict = {}
            for card in self.workflow_data.get('cards', []):
                card_id = card['id']
                # 同时支持整数和字符串键
                cards_dict[card_id] = card
                cards_dict[str(card_id)] = card

            connections_list = self.workflow_data.get('connections', [])

            # 查找起始卡片
            start_card_id = None
            for card in self.workflow_data.get('cards', []):
                if card.get('task_type') == '起点':
                    start_card_id = card.get('id')
                    break

            if start_card_id is None and self.workflow_data.get('cards'):
                start_card_id = self.workflow_data['cards'][0].get('id')

            if start_card_id is None:
                self._set_state(TaskState.FAILED, "错误: 找不到起始卡片")
                self.task_completed.emit(self.window_id, False)
                return

            logger.info(f"找到起始卡片ID: {start_card_id}, 类型: {type(start_card_id)}")
            logger.info(f"cards_dict中的键: {list(cards_dict.keys())}")

            # 设置窗口隔离的环境变量
            import os
            os.environ['MULTI_WINDOW_MODE'] = 'true'
            os.environ['TARGET_WINDOW_HWND'] = str(window_hwnd)
            os.environ['TARGET_WINDOW_TITLE'] = window_title

            # 存储工作流数据用于步骤显示
            self.workflow_data = {
                'cards': [cards_dict[card_id] for card_id in cards_dict],
                'connections': connections_list
            }
            logger.info(f"存储工作流数据，包含 {len(self.workflow_data['cards'])} 个卡片")

            # 创建工作流执行器
            self.executor = WorkflowExecutor(
                cards_data=cards_dict,
                connections_data=connections_list,
                task_modules=self.task_modules,
                target_window_title=window_title,
                target_hwnd=window_hwnd,
                execution_mode='background',  # 强制使用后台模式确保窗口隔离
                start_card_id=start_card_id
            )

            # 连接信号 - 使用Qt.QueuedConnection确保跨线程安全
            self.executor.execution_started.connect(
                self._on_execution_started,
                Qt.ConnectionType.QueuedConnection
            )
            self.executor.execution_finished.connect(
                self._on_execution_finished,
                Qt.ConnectionType.QueuedConnection
            )
            self.executor.step_details.connect(
                self._on_step_details,
                Qt.ConnectionType.QueuedConnection
            )
            self.executor.card_executing.connect(
                self._on_card_executing,
                Qt.ConnectionType.QueuedConnection
            )
            self.executor.card_finished.connect(
                self._on_card_finished,
                Qt.ConnectionType.QueuedConnection
            )

            # 设置运行状态并启动执行器
            self._set_state(TaskState.RUNNING, "工作流启动中")
            logger.info(f"窗口工作流已启动: {window_title} (HWND: {window_hwnd})")
            self._run_executor_in_main_thread()

        except Exception as e:
            logger.error(f"窗口工作流执行失败: {e}")
            self._set_state(TaskState.FAILED, f"错误: {str(e)}")
            self.task_completed.emit(self.window_id, False)
        finally:
            self._is_running = False

    def _run_executor_in_main_thread(self):
        """在主线程中运行执行器"""
        try:
            logger.info(f"_run_executor_in_main_thread 被调用")
            if hasattr(self, 'executor') and self.executor and not self._should_stop:
                # 直接在主线程中运行执行器
                logger.info(f"在主线程中启动执行器")
                self.executor.run()
            else:
                logger.warning(f"执行器状态检查失败: hasattr(self, 'executor')={hasattr(self, 'executor')}, self.executor={getattr(self, 'executor', None)}, should_stop={self._should_stop}")
        except Exception as e:
            logger.error(f"主线程执行器运行失败: {e}")
            self._set_state(TaskState.FAILED, f"启动失败: {str(e)}")
            self.task_completed.emit(self.window_id, False)

    def _on_execution_started(self):
        """工作流开始执行回调"""
        logger.info(f"_on_execution_started 被调用: window_id={self.window_id}")
        self._set_state(TaskState.RUNNING, "工作流已启动")
        logger.info(f"已发出状态更新信号: 正在运行, 步骤: 工作流已启动")

    def _on_step_details(self, details):
        """步骤详情更新回调"""
        logger.info(f"_on_step_details 被调用: window_id={self.window_id}, details={details}")
        self.step_updated.emit(self.window_id, details)

    def _on_card_executing(self, card_id):
        """卡片开始执行回调"""
        logger.info(f"_on_card_executing 被调用: window_id={self.window_id}, card_id={card_id}, type={type(card_id)}")

        # 查找卡片信息
        if hasattr(self, 'workflow_data') and self.workflow_data:
            logger.debug(f"查找卡片信息，工作流数据中有 {len(self.workflow_data.get('cards', []))} 个卡片")
            for card in self.workflow_data.get('cards', []):
                # 尝试多种类型匹配
                card_id_in_data = card.get('id')
                logger.debug(f"比较卡片ID: {card_id_in_data} (type: {type(card_id_in_data)}) vs {card_id} (type: {type(card_id)})")

                if (card_id_in_data == card_id or
                    str(card_id_in_data) == str(card_id) or
                    int(card_id_in_data) == int(card_id)):
                    task_type = card.get('task_type', '未知任务')
                    custom_name = card.get('custom_name')
                    if custom_name:
                        step_info = f"执行卡片{card_id}: {custom_name} ({task_type})"
                    else:
                        step_info = f"执行卡片{card_id}: {task_type}"
                    self.step_updated.emit(self.window_id, step_info)
                    logger.info(f"窗口{self.window_id}开始执行: {step_info}")
                    return

            # 如果没有找到匹配的卡片，记录所有卡片ID用于调试
            all_card_ids = [card.get('id') for card in self.workflow_data.get('cards', [])]
            logger.warning(f"未找到匹配的卡片ID {card_id}，工作流中的所有卡片ID: {all_card_ids}")
        else:
            logger.warning(f"没有工作流数据可用")

        # 如果没有工作流数据或找不到卡片，至少显示卡片ID
        step_info = f"执行卡片{card_id}"
        self.step_updated.emit(self.window_id, step_info)
        logger.info(f"窗口{self.window_id}开始执行: {step_info}")

    def _on_card_finished(self, card_id, success):
        """卡片执行完成回调"""
        if success:
            self.step_updated.emit(self.window_id, "步骤执行成功")
        else:
            self.step_updated.emit(self.window_id, "步骤执行失败")

    def _on_execution_finished(self, message):
        """工作流执行完成回调"""
        try:
            # 区分不同的完成状态
            if "被用户停止" in message or "用户停止" in message:
                # 用户主动停止
                self._set_state(TaskState.STOPPED, "工作流被中断")
                success = False
            elif "成功" in message or "完成" in message:
                # 正常完成
                self._set_state(TaskState.COMPLETED, "工作流已完成")
                success = True
            else:
                # 执行失败
                self._set_state(TaskState.FAILED, "工作流执行失败")
                success = False

            logger.info(f"窗口{self.window_id}工作流执行完成: {self._current_state.value} - {message}")

            # 发送任务完成信号
            self.task_completed.emit(self.window_id, success)

            # 延迟清理资源，避免立即清理导致的问题
            QTimer.singleShot(1000, self._cleanup_thread)

        except Exception as e:
            logger.error(f"执行完成回调处理失败: {e}")
            self._set_state(TaskState.FAILED, f"错误: {str(e)}")
            self.task_completed.emit(self.window_id, False)

    def _cleanup_thread(self):
        """清理执行器线程"""
        if self._is_cleaned:
            return  # 防止重复清理

        self._is_cleaned = True
        logger.info(f"开始清理窗口{self.window_id}的资源")
        try:
            # 断开信号连接，防止清理过程中的信号问题
            if hasattr(self, 'executor') and self.executor:
                try:
                    self.executor.execution_started.disconnect()
                    self.executor.execution_finished.disconnect()
                    self.executor.step_details.disconnect()
                    self.executor.card_executing.disconnect()
                    self.executor.card_finished.disconnect()
                except:
                    pass  # 忽略断开连接的错误

            # 清理执行器对象
            if hasattr(self, 'executor') and self.executor:
                try:
                    self.executor.deleteLater()
                except:
                    pass

            # 清理环境变量
            import os
            env_vars_to_clean = ['TARGET_WINDOW_HWND', 'TARGET_WINDOW_TITLE', 'MULTI_WINDOW_MODE']
            for var in env_vars_to_clean:
                if var in os.environ:
                    try:
                        del os.environ[var]
                    except:
                        pass

        except Exception as e:
            logger.warning(f"清理线程时发生错误: {e}")
        finally:
            self.executor = None
            self._is_running = False
            logger.info(f"窗口{self.window_id}工作流资源清理完成")

    def stop(self):
        """停止工作流执行"""
        logger.info(f"收到停止请求，当前状态: {self._current_state.value}")

        # 检查是否可以停止
        if not self.can_stop:
            logger.warning(f"窗口{self.window_id}当前状态{self._current_state.value}不允许停止")
            return

        # 设置停止标志
        self._should_stop = True

        # 立即设置停止状态
        self._set_state(TaskState.STOPPING, "正在停止工作流")

        # 停止执行器
        if hasattr(self, 'executor') and self.executor:
            try:
                self.executor.request_stop()
                logger.info(f"窗口{self.window_id}工作流停止请求已发送")
            except Exception as e:
                logger.warning(f"停止执行器时发生错误: {e}")

        # 强制设置为已停止状态（防止卡住）
        QTimer.singleShot(2000, self._force_stop_completion)

    def _force_stop_completion(self):
        """强制完成停止操作（防止卡住）"""
        if self._current_state == TaskState.STOPPING:
            logger.warning(f"窗口{self.window_id}停止超时，强制设置为已停止状态")
            self._set_state(TaskState.STOPPED, "工作流已强制停止")
            self.task_completed.emit(self.window_id, False)
            self._cleanup_thread()

class ControlCenterWindow(QMainWindow):
    """中控软件主窗口 - 多窗口工作流管理"""

    def __init__(self, bound_windows: List[Dict], task_modules: Dict[str, Any],
                 config: Dict[str, Any] = None, vu_wrapper=None, parent=None):
        super().__init__(parent)
        self.bound_windows = bound_windows
        self.task_modules = task_modules
        self.config = config or {}
        self.vu_wrapper = vu_wrapper
        self.window_runners = {}  # 存储每个窗口的任务运行器
        self.window_workflows = {}  # 存储每个窗口分配的工作流
        self.sorted_windows = []  # 存储排序后的窗口列表

        self.setWindowTitle("中控软件 - 多窗口工作流管理")
        self.setGeometry(200, 200, 1000, 500)
        self.setMinimumSize(800, 400)
        
        # 设置样式 - 参考主程序风格
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
                font-size: 10pt;
            }
            QGroupBox {
                font-weight: bold;
                border: none;
                border-radius: 6px;
                margin-top: 8px;
                padding: 8px;
                background-color: #f8f8f8;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 8px;
                left: 15px;
                color: #555555;
            }
            QPushButton {
                padding: 8px 18px;
                border: none;
                border-radius: 4px;
                background-color: #e8e8e8;
                color: #333333;
            }
            QPushButton:hover {
                background-color: #dddddd;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            QTableWidget {
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                background-color: white;
                gridline-color: #f0f0f0;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #f0f0f0;
            }
            QTableWidget::item:selected {
                background-color: #e3f2fd;
            }
            QTextEdit {
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                background-color: white;
                padding: 8px;
            }
        """)
        
        self.init_ui()
        self.setup_timer()

    def sort_windows_by_title(self, windows):
        """按窗口标题排序，雷电模拟器窗口按数字顺序排列"""
        def get_sort_key(window):
            title = window.get('title', '')

            # 如果是雷电模拟器相关窗口（包含雷电模拟器或TheRender），按数字排序
            if '雷电模拟器' in title or 'TheRender' in title:
                import re
                # 查找标题中的数字
                match = re.search(r'(\d+)', title)
                if match:
                    return (0, int(match.group(1)))  # 0表示雷电模拟器优先级最高
                else:
                    return (0, 999)  # 没有数字的雷电模拟器放在最后
            else:
                # 其他窗口按字母顺序排列，优先级较低
                return (1, title)

        return sorted(windows, key=get_sort_key)

    def format_window_title(self, original_title, row_index):
        """格式化窗口标题显示"""
        # 如果是雷电模拟器相关窗口（包含雷电模拟器或TheRender），统一显示为"雷电模拟器-N"格式
        if '雷电模拟器' in original_title or 'TheRender' in original_title:
            return f"雷电模拟器-{row_index + 1}"
        # 如果是MuMu模拟器相关窗口，统一显示为"MuMu模拟器-N"格式
        elif 'MuMu模拟器' in original_title or 'nemudisplay' in original_title:
            return f"MuMu模拟器-{row_index + 1}"
        else:
            # 其他窗口保持原标题，但如果有多个相同的，也加上编号
            return f"{original_title}-{row_index + 1}"

    def init_ui(self):
        """初始化用户界面"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # 窗口状态表格
        window_panel = self.create_window_panel()
        main_layout.addWidget(window_panel)
        

        
    def create_window_panel(self):
        """创建窗口状态面板"""
        group = QGroupBox("绑定窗口管理")
        layout = QVBoxLayout(group)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(8)

        # 添加说明文字
        info_label = QLabel("为每个窗口分配工作流并控制执行")
        info_label.setStyleSheet("color: #666666; font-size: 9pt;")
        layout.addWidget(info_label)
        layout.addSpacing(5)

        # 窗口状态表格 - 添加绑定模式列
        self.window_table = QTableWidget()
        self.window_table.setColumnCount(6)
        self.window_table.setHorizontalHeaderLabels([
            "窗口标题", "句柄", "绑定模式", "分配的工作流", "状态", "当前步骤"
        ])

        # 设置表格属性 - 所有列都根据内容自动调节
        header = self.window_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)  # 所有列都根据内容调节

        # 设置最后一列（当前步骤）可以拉伸以填充剩余空间
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)

        # 设置表格行高 - 减少行高
        self.window_table.verticalHeader().setDefaultSectionSize(30)
        self.window_table.setAlternatingRowColors(True)
        self.window_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        # 设置表格样式 - 彻底移除虚线和边框
        self.window_table.setStyleSheet("""
            QTableWidget {
                gridline-color: #d0d0d0;
                background-color: white;
                alternate-background-color: #f5f5f5;
                selection-background-color: #3daee9;
                selection-color: white;
                show-decoration-selected: 1;
            }
            QTableWidget::item {
                padding: 8px;
                border: 0px;
                color: black;
                outline: 0px;
            }
            QTableWidget::item:selected {
                background-color: #3daee9;
                color: white;
                border: 0px solid transparent;
                outline: 0px;
            }
            QTableWidget::item:focus {
                border: 0px solid transparent;
                outline: 0px;
                background-color: #3daee9;
                color: white;
            }
            QTableWidget:focus {
                outline: 0px;
                border: 0px;
            }
        """)

        # 设置焦点策略，进一步避免虚线
        self.window_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # 连接选择变化信号
        self.window_table.selectionModel().selectionChanged.connect(self.on_selection_changed)

        layout.addWidget(self.window_table)

        # 添加操作按钮面板
        button_panel = self.create_button_panel()
        layout.addWidget(button_panel)

        # 填充窗口数据
        self.populate_window_table()

        return group

    def create_button_panel(self):
        """创建独立的按钮操作面板"""
        panel = QGroupBox("窗口操作")
        layout = QHBoxLayout(panel)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(10)

        # 分配工作流按钮
        self.assign_btn = QPushButton("分配工作流")
        self.assign_btn.setFixedSize(100, 35)
        self.assign_btn.setToolTip("为选中的窗口分配工作流文件")
        self.assign_btn.clicked.connect(self.assign_workflow_to_selected)
        self.assign_btn.setEnabled(False)
        layout.addWidget(self.assign_btn)

        # 全部开始按钮
        self.start_all_btn = QPushButton("全部开始")
        self.start_all_btn.setFixedSize(100, 35)
        self.start_all_btn.setToolTip("启动所有已分配工作流的窗口")
        self.start_all_btn.clicked.connect(self.start_all_tasks)
        layout.addWidget(self.start_all_btn)

        # 全局停止按钮
        self.stop_all_btn = QPushButton("停止全部")
        self.stop_all_btn.setFixedSize(100, 35)
        self.stop_all_btn.setToolTip("通过主程序停止所有正在运行的工作流")
        self.stop_all_btn.clicked.connect(self.stop_all_tasks)
        self.stop_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
            QPushButton:pressed {
                background-color: #b71c1c;
            }
        """)
        layout.addWidget(self.stop_all_btn)

        # 添加弹性空间
        layout.addStretch()

        # 状态标签
        self.selection_label = QLabel("请选择一个窗口进行操作")
        self.selection_label.setStyleSheet("color: #666666; font-size: 9pt;")
        layout.addWidget(self.selection_label)

        return panel

    def on_selection_changed(self):
        """表格选择变化时的处理"""
        selected_rows = set()
        for item in self.window_table.selectedItems():
            selected_rows.add(item.row())

        has_selection = len(selected_rows) > 0
        self.assign_btn.setEnabled(has_selection)

        if has_selection:
            row = list(selected_rows)[0]  # 取第一个选中的行
            window_title = self.window_table.item(row, 0).text()
            self.selection_label.setText(f"已选择: {window_title}")
        else:
            self.selection_label.setText("请选择一个窗口进行操作")

    def populate_window_table(self):
        """填充窗口表格数据"""
        # 🔧 过滤无效窗口
        from utils.window_filter import is_valid_target_window
        valid_windows = [w for w in self.bound_windows if is_valid_target_window(w.get('hwnd', 0))]
        
        # 对窗口进行排序 - 按雷电模拟器窗口-1、雷电模拟器-2等顺序
        self.sorted_windows = self.sort_windows_by_title(valid_windows)

        logger.info(f"开始填充窗口表格，共有 {len(self.sorted_windows)} 个窗口")
        self.window_table.setRowCount(len(self.sorted_windows))

        for row, window_info in enumerate(self.sorted_windows):
            # 窗口标题 - 格式化显示
            original_title = window_info.get('title', '未知窗口')
            display_title = self.format_window_title(original_title, row)
            logger.info(f"设置第{row}行窗口标题: {original_title} -> {display_title}")

            title_item = QTableWidgetItem(display_title)
            title_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.window_table.setItem(row, 0, title_item)

            # 句柄
            hwnd = window_info.get('hwnd', 0)
            hwnd_item = QTableWidgetItem(str(hwnd))
            hwnd_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.window_table.setItem(row, 1, hwnd_item)

            # 绑定模式 - 从配置中获取
            bind_preset = self.config.get('bind_preset', 'FOREGROUND')
            preset_display_map = {
                'FOREGROUND': "前台模式",
                'BACKGROUND_BASIC': "后台模式（基础）",
                'BACKGROUND_DX': "后台模式（DirectX）",
                'BACKGROUND_DX_FULL': "后台模式（完整DX）",
                'DRIVER_HIDDEN': "驱动级后台（隐藏DLL）",
                'DRIVER_FULL': "驱动级后台（完整形态）",
                'VT_MODE': "VT模式后台",
                'custom': "自定义"
            }
            bind_mode_text = preset_display_map.get(bind_preset, bind_preset)
            bind_mode_item = QTableWidgetItem(bind_mode_text)
            bind_mode_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.window_table.setItem(row, 2, bind_mode_item)

            # 分配的工作流
            workflow_item = QTableWidgetItem("未分配")
            workflow_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.window_table.setItem(row, 3, workflow_item)

            # 状态
            status_item = QTableWidgetItem("就绪")
            status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.window_table.setItem(row, 4, status_item)

            # 当前步骤
            step_item = QTableWidgetItem("等待开始")
            step_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.window_table.setItem(row, 5, step_item)

            logger.info(f"第{row}行数据设置完成: 标题={display_title}, 句柄={hwnd}, 工作流=未分配, 状态=就绪, 步骤=等待开始")

        logger.info("窗口表格填充完成")

        # 强制刷新表格显示
        self.window_table.viewport().update()
        self.window_table.repaint()

        # 验证数据是否正确设置
        for row in range(self.window_table.rowCount()):
            for col in range(self.window_table.columnCount()):
                item = self.window_table.item(row, col)
                if item:
                    logger.debug(f"验证第{row}行第{col}列: {item.text()}")
                else:
                    logger.warning(f"第{row}行第{col}列的item为空!")
            
    def setup_timer(self):
        """设置定时器更新界面"""
        pass  # 暂时不需要定时器



    def assign_workflow_to_selected(self):
        """为选中的窗口分配工作流"""
        selected_rows = set()
        for item in self.window_table.selectedItems():
            selected_rows.add(item.row())

        if not selected_rows:
            return

        row = list(selected_rows)[0]  # 取第一个选中的行
        self.assign_workflow_to_window(row)



    def start_all_tasks(self):
        """启动所有已分配工作流的窗口"""
        logger.info("开始启动所有工作流")
        self.log_message("正在启动所有工作流...")

        started_count = 0
        for row in range(self.window_table.rowCount()):
            try:
                window_info = self.sorted_windows[row]
                window_id = str(window_info.get('hwnd', row))

                # 检查是否已分配工作流
                if window_id not in self.window_workflows:
                    logger.info(f"窗口{window_id}未分配工作流，跳过启动")
                    continue

                # 检查是否已经在运行
                if window_id in self.window_runners:
                    runner = self.window_runners[window_id]
                    if runner.is_running:
                        logger.info(f"窗口{window_id}已在运行，跳过启动")
                        continue

                # 启动工作流
                self.start_window_task(row)
                started_count += 1
                logger.info(f"已启动窗口{window_id}的工作流")

            except Exception as e:
                logger.error(f"启动窗口{row}工作流时发生错误: {e}")

        self.log_message(f"已启动 {started_count} 个工作流")

    def stop_all_tasks(self):
        """停止所有正在运行的工作流"""
        logger.info("开始停止所有工作流")
        self.log_message("正在停止所有工作流...")

        # 直接停止所有运行器
        self._direct_stop_all_tasks()

        # 设置超时强制完成停止
        QTimer.singleShot(3000, self._force_stop_all_completion)

    def _confirm_global_stop(self, app):
        """确认全局停止完成"""
        try:
            if app and hasattr(app, 'task_state_manager'):
                app.task_state_manager.confirm_stopped()
                logger.info("已确认全局停止完成，状态管理器已重置")
                self.log_message("全局停止完成")
        except Exception as e:
            logger.error(f"确认全局停止时发生错误: {e}")

    def _direct_stop_all_tasks(self):
        """直接停止所有任务"""
        stopped_count = 0
        for window_id, runner in list(self.window_runners.items()):
            try:
                # 检查运行器是否可以停止
                if runner.can_stop:
                    runner.stop()
                    stopped_count += 1
                    logger.info(f"已停止窗口{window_id}的工作流")
                else:
                    logger.info(f"窗口{window_id}状态为'{runner.current_state.value}'，跳过停止操作")
            except Exception as e:
                logger.error(f"停止窗口{window_id}工作流时发生错误: {e}")

        self.log_message(f"已停止 {stopped_count} 个工作流")

    def _force_stop_all_completion(self):
        """强制完成所有停止操作（防止卡住）"""
        logger.info("强制完成所有停止操作")
        for window_id, runner in list(self.window_runners.items()):
            try:
                if runner.current_state == TaskState.STOPPING:
                    runner._force_stop_completion()
            except Exception as e:
                logger.error(f"强制停止窗口{window_id}时发生错误: {e}")

        self.log_message("所有工作流已停止")

    def assign_workflow_to_window(self, row):
        """为指定窗口分配工作流"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            f"为窗口 '{self.sorted_windows[row].get('title', '未知窗口')}' 选择工作流",
            "",
            "JSON Files (*.json);;All Files (*)"
        )

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    workflow_data = json.load(f)

                window_id = str(self.sorted_windows[row].get('hwnd', row))
                self.window_workflows[window_id] = {
                    'file_path': file_path,
                    'data': copy.deepcopy(workflow_data),
                    'name': file_path.split('/')[-1].split('\\')[-1]
                }

                # 更新表格显示
                workflow_item = self.window_table.item(row, 3)
                if workflow_item:
                    workflow_item.setText(self.window_workflows[window_id]['name'])
                    workflow_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                # 更新按钮状态
                self.on_selection_changed()

                window_title = self.sorted_windows[row].get('title', '未知窗口')
                self.log_message(f"已为窗口 '{window_title}' 分配工作流: {file_path}")

            except Exception as e:
                QMessageBox.warning(self, "错误", f"分配工作流失败: {e}")
                self.log_message(f"分配工作流失败: {e}")
        

        
    def start_window_task(self, row):
        """启动指定窗口的工作流"""
        window_info = self.sorted_windows[row]
        window_id = str(window_info.get('hwnd', row))
        window_hwnd = window_info.get('hwnd', 0)

        if window_id in self.window_runners:
            return  # 已经在运行

        # 检查是否已分配工作流
        if window_id not in self.window_workflows:
            QMessageBox.warning(self, "警告", "请先为该窗口分配工作流")
            return

        # 🔧 使用VU插件绑定窗口（如果可用）
        if self.vu_wrapper and self.vu_wrapper.is_initialized():
            bind_preset = self.config.get('bind_preset', 'FOREGROUND')
            
            if bind_preset == 'custom':
                # 使用自定义参数
                display = self.config.get('bind_display', 'normal')
                mouse = self.config.get('bind_mouse', 'normal')
                keypad = self.config.get('bind_keypad', 'normal')
                public = self.config.get('bind_public', '')
                mode = self.config.get('bind_mode_ex', 0)
            else:
                # 使用预设方案
                from config.vu_config import VUBindPresets
                preset_params = VUBindPresets.get_preset(bind_preset)
                display = preset_params['display']
                mouse = preset_params['mouse']
                keypad = preset_params['keypad']
                public = preset_params['public']
                mode = preset_params['mode']
            
            # 调用BindWindowEx绑定窗口
            ret = self.vu_wrapper.bind_window_ex(window_hwnd, display, mouse, keypad, public, mode)
            if ret > 0:
                logger.info(f"窗口绑定成功: HWND={window_hwnd}, 预设={bind_preset}")
            else:
                logger.warning(f"窗口绑定失败: HWND={window_hwnd}")

        # 获取工作流数据
        workflow_data = self.window_workflows[window_id]['data']

        # 创建任务运行器
        runner = WindowTaskRunner(window_info, workflow_data, self.task_modules)
        runner.status_updated.connect(self.on_window_status_updated)
        runner.step_updated.connect(self.on_window_step_updated)
        runner.task_completed.connect(self.on_window_task_completed)

        self.window_runners[window_id] = runner
        runner.start()

        # 更新独立按钮状态
        self.on_selection_changed()

        workflow_name = self.window_workflows[window_id]['name']
        self.log_message(f"启动窗口工作流: {window_info.get('title', '未知窗口')} - {workflow_name}")
        
    def stop_window_task(self, row):
        """停止指定窗口的工作流"""
        window_info = self.sorted_windows[row]
        window_id = str(window_info.get('hwnd', row))

        # 直接停止指定窗口的runner，不使用全局停止机制
        # 因为全局停止会影响所有窗口，而这里只想停止单个窗口
        try:
            logger.info(f"停止窗口{window_id}的工作流")
            self._direct_stop_window_task(window_id)
        except Exception as e:
            logger.error(f"停止窗口{window_id}失败: {e}")
            self.log_message(f"停止窗口{window_id}失败: {str(e)}")

        # 更新独立按钮状态
        self.on_selection_changed()

        # 更新状态
        status_item = self.window_table.item(row, 4)
        if status_item:
            status_item.setText("正在停止")
            status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        step_item = self.window_table.item(row, 5)
        if step_item:
            step_item.setText("正在停止工作流")
            step_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        self.log_message(f"停止窗口工作流: {window_info.get('title', '未知窗口')}")

    def _direct_stop_window_task(self, window_id):
        """直接停止窗口任务的备用方法"""
        # 安全地停止和清理runner
        if window_id in self.window_runners:
            try:
                runner = self.window_runners[window_id]
                runner.stop()
                # 在主线程模式下不需要等待线程
                # runner.wait()  # 等待线程结束
                # 注意：不在这里删除runner，因为stop()方法会发出task_completed信号
                # 该信号会触发on_window_task_completed方法来清理runner
                logger.info(f"已直接停止窗口{window_id}的工作流")
            except Exception as e:
                logger.error(f"直接停止窗口{window_id}工作流时发生错误: {e}")
                # 如果停止过程中出错，手动清理runner引用
                # 因为task_completed信号可能没有正常发出
                if window_id in self.window_runners:
                    try:
                        del self.window_runners[window_id]
                        logger.info(f"手动清理窗口{window_id}的运行器")
                    except Exception as cleanup_e:
                        logger.error(f"清理窗口{window_id}运行器时发生错误: {cleanup_e}")
        
    def on_window_status_updated(self, window_id, status):
        """窗口状态更新回调"""
        row = self.find_window_row(window_id)
        if row >= 0:
            status_item = self.window_table.item(row, 4)
            if status_item:
                status_item.setText(status)
                status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def on_window_step_updated(self, window_id, step_info):
        """窗口步骤更新回调"""
        logger.info(f"on_window_step_updated 被调用: window_id={window_id}, step_info={step_info}")
        row = self.find_window_row(window_id)
        logger.info(f"找到窗口行: {row}")
        if row >= 0:
            step_item = self.window_table.item(row, 5)
            if step_item:
                logger.info(f"更新步骤文本: {step_info}")
                step_item.setText(step_info)
                step_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            else:
                logger.warning(f"步骤项为空，行={row}")
        else:
            logger.warning(f"未找到窗口行，window_id={window_id}")
                    
    def on_window_task_completed(self, window_id, success):
        """窗口工作流完成回调"""
        row = self.find_window_row(window_id)
        if row >= 0:
            # 检查当前状态，判断是中断还是失败
            status_item = self.window_table.item(row, 4)
            current_status = status_item.text() if status_item else ""

            # 如果当前状态已经是"已中断"，保持不变
            if current_status == "已中断":
                # 状态已经正确设置，不需要修改
                pass
            else:
                # 根据success参数设置状态
                if status_item:
                    status_text = "完成" if success else "失败"
                    status_item.setText(status_text)
                    status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                step_item = self.window_table.item(row, 5)
                if step_item:
                    step_text = "工作流已完成" if success else "工作流执行失败"
                    step_item.setText(step_text)
                    step_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # 安全地从运行器列表中移除
        if window_id in self.window_runners:
            try:
                del self.window_runners[window_id]
                logger.info(f"已清理窗口{window_id}的运行器")
            except Exception as e:
                logger.error(f"清理窗口{window_id}运行器时发生错误: {e}")

        # 更新独立按钮状态
        self.on_selection_changed()

        window_title = "未知窗口"
        workflow_name = "未知工作流"
        if row >= 0:
            window_title = self.window_table.item(row, 0).text()
            workflow_name = self.window_table.item(row, 3).text()
            # 获取最终状态用于日志
            final_status = self.window_table.item(row, 4).text() if self.window_table.item(row, 4) else "未知"

        # 根据最终状态确定结果描述
        if row >= 0:
            final_status = self.window_table.item(row, 4).text() if self.window_table.item(row, 4) else "未知"
            if final_status == "已中断":
                result = "被中断"
            elif final_status == "完成":
                result = "成功"
            else:
                result = "失败"
        else:
            result = "成功" if success else "失败"

        self.log_message(f"窗口工作流完成: {window_title} ({workflow_name}) - {result}")
        
    def find_window_row(self, window_id):
        """根据窗口ID查找表格行"""
        for row in range(self.window_table.rowCount()):
            hwnd_item = self.window_table.item(row, 1)
            if hwnd_item and hwnd_item.text() == window_id:
                return row
        return -1
        

        
    def log_message(self, message):
        """添加日志消息到控制台"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
        
    def closeEvent(self, event):
        """窗口关闭事件"""
        # 停止所有运行中的任务
        for runner in list(self.window_runners.values()):
            runner.stop()
            runner.wait()
            
        self.window_runners.clear()
        event.accept()
