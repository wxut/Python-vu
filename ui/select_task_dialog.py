
# -*- coding: utf-8 -*-
"""
优化的任务选择对话框
提供更直观、快速的任务类型选择体验
"""
from typing import List, Optional, Dict
import json
import os
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QListWidgetItem, QLineEdit, QTabWidget, 
    QWidget, QGridLayout, QScrollArea, QFrame, QButtonGroup
)
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QFont, QColor, QIcon, QPalette

class TaskButton(QPushButton):
    """任务按钮组件 - 网格视图中的单个任务按钮"""
    def __init__(self, task_name: str, icon_emoji: str = "📋", parent=None):
        super().__init__(parent)
        self.task_name = task_name
        self.setCheckable(True)
        self.setMinimumSize(120, 80)
        self.setMaximumSize(150, 90)
        
        # 设置按钮文本（图标+任务名）
        display_text = f"{icon_emoji}\n{task_name}"
        self.setText(display_text)
        
        # 样式
        self.setStyleSheet("""
            TaskButton {
                background-color: white;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                padding: 8px;
                font-size: 12px;
                color: #333;
                text-align: center;
            }
            TaskButton:hover {
                background-color: #F5F5F5;
                border: 2px solid #B0B0B0;
            }
            TaskButton:checked {
                background-color: #E3F2FD;
                border: 2px solid #2196F3;
                color: #1976D2;
                font-weight: bold;
            }
            TaskButton:pressed {
                background-color: #BBDEFB;
            }
        """)

class SelectTaskDialog(QDialog):
    """优化的任务选择对话框
    
    改进点:
    1. 提供列表视图和网格视图两种模式
    2. 支持快速搜索过滤
    3. 记录最近使用的任务
    4. 分类标签页组织
    5. 键盘快捷键支持
    """
    
    # 最近使用任务的保存文件
    RECENT_TASKS_FILE = "config/recent_tasks.json"
    MAX_RECENT_TASKS = 8
    
    def __init__(self, task_types: List[str], parent=None):
        super().__init__(parent)
        self.setWindowTitle("选择任务类型")
        self.setMinimumWidth(850)
        self.setMinimumHeight(650)
        
        self._selected_task_type: Optional[str] = None
        self._all_task_types = sorted(task_types)  # 排序以便查找
        self._categorized_tasks = self._categorize_tasks(task_types)
        self._recent_tasks = self._load_recent_tasks()
        
        # 按钮组（用于单选行为）
        self.grid_button_group = QButtonGroup(self)
        self.grid_button_group.setExclusive(True)
        
        self._init_ui()
        self._apply_styles()
        self._connect_signals()
        
    def _categorize_tasks(self, task_types: List[str]) -> Dict[str, List[str]]:
        """将任务分类"""
        categories = {
            "🎯 VU插件功能": [],
            "🖱️ 基础操作": [],
            "🎮 模拟器管理": [],
            "⚙️ 流程控制": [],
            "🛠️ 其他功能": []
        }
        
        for task in task_types:
            # VU插件功能 - 所有VU/无忧开头的任务
            if task.startswith("VU") or task.startswith("无忧"):
                categories["🎯 VU插件功能"].append(task)
            # 模拟器管理
            elif any(x in task for x in ["雷电", "MuMu", "应用管理"]):
                categories["🎮 模拟器管理"].append(task)
            # 流程控制
            elif any(x in task for x in ["开始", "条件", "延时"]):
                categories["⚙️ 流程控制"].append(task)
            # 基础操作
            elif any(x in task for x in ["鼠标", "键盘", "点击", "滚轮", "找图", "找色", "OCR", "识别", "旋转", "坐标"]):
                categories["🖱️ 基础操作"].append(task)
            else:
                categories["🛠️ 其他功能"].append(task)
        
        # 移除空分类并排序每个分类内的任务
        return {k: sorted(v) for k, v in categories.items() if v}
    
    def _get_task_icon(self, task_name: str) -> str:
        """根据任务名称返回对应的emoji图标"""
        icon_map = {
            "找图": "🖼️", "找色": "🎨", "OCR": "📝", "识别": "👁️",
            "鼠标": "🖱️", "键盘": "⌨️", "点击": "👆", "滚轮": "🔄",
            "雷电": "⚡", "MuMu": "🎮", "应用": "📱",
            "开始": "▶️", "条件": "🔀", "延时": "⏱️",
            "窗口": "🪟", "截图": "📸", "图像": "🖼️", "JSON": "📋",
            "内存": "💾", "AI": "🤖", "YOLO": "🎯"
        }
        
        for keyword, icon in icon_map.items():
            if keyword in task_name:
                return icon
        return "📋"
    
    def _init_ui(self):
        """初始化UI"""
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 标题和搜索栏
        header_layout = QHBoxLayout()
        
        title_label = QLabel("选择任务类型")
        title_label.setObjectName("titleLabel")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # 视图切换按钮
        self.view_grid_btn = QPushButton("网格视图 📱")
        self.view_grid_btn.setObjectName("viewButton")
        self.view_grid_btn.setCheckable(True)
        self.view_grid_btn.setChecked(True)
        self.view_grid_btn.setMinimumHeight(32)
        
        self.view_list_btn = QPushButton("列表视图 📋")
        self.view_list_btn.setObjectName("viewButton")
        self.view_list_btn.setCheckable(True)
        self.view_list_btn.setMinimumHeight(32)
        
        header_layout.addWidget(self.view_grid_btn)
        header_layout.addWidget(self.view_list_btn)
        
        main_layout.addLayout(header_layout)
        
        # 搜索框
        self.search_box = QLineEdit()
        self.search_box.setObjectName("searchBox")
        self.search_box.setPlaceholderText("🔍 输入关键词快速搜索任务...")
        self.search_box.setClearButtonEnabled(True)
        self.search_box.setMinimumHeight(38)
        main_layout.addWidget(self.search_box)
        
        # 标签页容器（包含最近使用和分类标签）
        self.tab_widget = QTabWidget()
        self.tab_widget.setObjectName("mainTabs")
        
        # === 最近使用标签页 ===
        if self._recent_tasks:
            recent_tab = self._create_recent_tab()
            self.tab_widget.addTab(recent_tab, "⭐ 最近使用")
        
        # === 所有任务标签页 ===
        all_tasks_tab = self._create_all_tasks_tab()
        self.tab_widget.addTab(all_tasks_tab, "📚 所有任务")
        
        # === 分类标签页 ===
        for category_name, tasks in self._categorized_tasks.items():
            if tasks:
                category_tab = self._create_category_tab(tasks)
                self.tab_widget.addTab(category_tab, category_name)
        
        main_layout.addWidget(self.tab_widget)
        
        # 底部按钮
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.ok_button = QPushButton("确定")
        self.ok_button.setObjectName("okButton")
        self.ok_button.setDefault(True)
        self.ok_button.setMinimumHeight(38)
        self.ok_button.setMinimumWidth(100)
        self.ok_button.setEnabled(False)
        
        self.cancel_button = QPushButton("取消")
        self.cancel_button.setObjectName("cancelButton")
        self.cancel_button.setMinimumHeight(38)
        self.cancel_button.setMinimumWidth(100)
        
        button_layout.addStretch()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
    
    def _create_recent_tab(self) -> QWidget:
        """创建最近使用标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # 提示信息
        info_label = QLabel("这些是您最近使用的任务类型，点击快速添加")
        info_label.setStyleSheet("color: #666; font-size: 12px; padding: 5px;")
        layout.addWidget(info_label)
        
        # 网格布局
        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setSpacing(10)
        
        row, col = 0, 0
        max_cols = 4
        
        for task in self._recent_tasks[:self.MAX_RECENT_TASKS]:
            if task in self._all_task_types:
                icon = self._get_task_icon(task)
                btn = TaskButton(task, icon)
                self.grid_button_group.addButton(btn)
                btn.clicked.connect(lambda checked, t=task: self._on_task_selected(t))
                
                grid_layout.addWidget(btn, row, col)
                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1
        
        layout.addWidget(grid_widget)
        layout.addStretch()
        
        return widget
    
    def _create_all_tasks_tab(self) -> QWidget:
        """创建所有任务标签页（支持切换视图）"""
        widget = QWidget()
        self.all_tasks_layout = QVBoxLayout(widget)
        self.all_tasks_layout.setContentsMargins(10, 10, 10, 10)
        
        # 默认显示网格视图
        self.grid_view_widget = self._create_grid_view(self._all_task_types)
        self.list_view_widget = self._create_list_view(self._all_task_types)
        
        self.all_tasks_layout.addWidget(self.grid_view_widget)
        self.all_tasks_layout.addWidget(self.list_view_widget)
        self.list_view_widget.setVisible(False)
        
        return widget
    
    def _create_category_tab(self, tasks: List[str]) -> QWidget:
        """创建分类标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # 使用网格布局
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        
        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setSpacing(10)
        
        row, col = 0, 0
        max_cols = 5
        
        for task in tasks:
            icon = self._get_task_icon(task)
            btn = TaskButton(task, icon)
            self.grid_button_group.addButton(btn)
            btn.clicked.connect(lambda checked, t=task: self._on_task_selected(t))
            
            grid_layout.addWidget(btn, row, col)
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
        
        # 填充剩余空间
        grid_layout.setRowStretch(row + 1, 1)
        
        scroll_area.setWidget(grid_widget)
        layout.addWidget(scroll_area)
        
        return widget
    
    def _create_grid_view(self, tasks: List[str]) -> QWidget:
        """创建网格视图"""
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        scroll_area.setObjectName("gridScrollArea")
        
        grid_widget = QWidget()
        self.grid_layout = QGridLayout(grid_widget)
        self.grid_layout.setSpacing(10)
        
        self._populate_grid_view(tasks)
        
        scroll_area.setWidget(grid_widget)
        return scroll_area
    
    def _populate_grid_view(self, tasks: List[str]):
        """填充网格视图"""
        # 清空现有内容
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        row, col = 0, 0
        max_cols = 5
        
        for task in tasks:
            icon = self._get_task_icon(task)
            btn = TaskButton(task, icon)
            self.grid_button_group.addButton(btn)
            btn.clicked.connect(lambda checked, t=task: self._on_task_selected(t))
            
            self.grid_layout.addWidget(btn, row, col)
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
        
        # 填充剩余空间
        self.grid_layout.setRowStretch(row + 1, 1)
    
    def _create_list_view(self, tasks: List[str]) -> QWidget:
        """创建列表视图"""
        self.task_list = QListWidget()
        self.task_list.setObjectName("taskList")
        
        for task in tasks:
            icon = self._get_task_icon(task)
            item = QListWidgetItem(f"{icon}  {task}")
            item.setData(Qt.ItemDataRole.UserRole, task)
            self.task_list.addItem(item)
        
        return self.task_list
    
    def _apply_styles(self):
        """应用样式"""
        self.setStyleSheet("""
            QDialog {
                background-color: #FAFAFA;
                font-family: "Microsoft YaHei", sans-serif;
            }
            QLabel#titleLabel {
                color: #333;
                padding: 5px 0px;
            }
            QLineEdit#searchBox {
                border: 2px solid #D0D0D0;
                border-radius: 8px;
                padding: 10px 15px;
                background-color: white;
                font-size: 13px;
                color: #333;
            }
            QLineEdit#searchBox:focus {
                border: 2px solid #2196F3;
            }
            QPushButton#viewButton {
                background-color: white;
                border: 2px solid #D0D0D0;
                border-radius: 6px;
                padding: 6px 15px;
                font-size: 12px;
                color: #555;
                min-width: 90px;
            }
            QPushButton#viewButton:hover {
                background-color: #F5F5F5;
                border: 2px solid #B0B0B0;
            }
            QPushButton#viewButton:checked {
                background-color: #2196F3;
                border: 2px solid #2196F3;
                color: white;
                font-weight: bold;
            }
            QTabWidget#mainTabs::pane {
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                background-color: white;
                top: -1px;
            }
            QTabWidget#mainTabs QTabBar::tab {
                background-color: #F5F5F5;
                border: 1px solid #E0E0E0;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                padding: 8px 15px;
                margin-right: 2px;
                font-size: 12px;
                color: #666;
            }
            QTabWidget#mainTabs QTabBar::tab:selected {
                background-color: white;
                color: #2196F3;
                font-weight: bold;
                border-bottom: 2px solid white;
            }
            QTabWidget#mainTabs QTabBar::tab:hover {
                background-color: #EEEEEE;
            }
            QListWidget#taskList {
                border: none;
                background-color: white;
                font-size: 13px;
                outline: none;
            }
            QListWidget#taskList::item {
                padding: 10px 15px;
                border-bottom: 1px solid #F0F0F0;
            }
            QListWidget#taskList::item:hover {
                background-color: #F5F5F5;
            }
            QListWidget#taskList::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
            }
            QPushButton#okButton {
                background-color: #2196F3;
                color: white;
                font-size: 13px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton#okButton:hover {
                background-color: #1976D2;
            }
            QPushButton#okButton:pressed {
                background-color: #1565C0;
            }
            QPushButton#okButton:disabled {
                background-color: #CCCCCC;
                color: #888888;
            }
            QPushButton#cancelButton {
                background-color: white;
                color: #555;
                font-size: 13px;
                border: 2px solid #D0D0D0;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton#cancelButton:hover {
                background-color: #F5F5F5;
                border: 2px solid #B0B0B0;
            }
            QPushButton#cancelButton:pressed {
                background-color: #EEEEEE;
            }
        """)
    
    def _connect_signals(self):
        """连接信号"""
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.search_box.textChanged.connect(self._on_search_changed)
        
        # 视图切换
        self.view_grid_btn.clicked.connect(self._switch_to_grid_view)
        self.view_list_btn.clicked.connect(self._switch_to_list_view)
        
        # 列表视图的选择
        self.task_list.itemSelectionChanged.connect(self._on_list_selection_changed)
        self.task_list.itemDoubleClicked.connect(self._on_list_double_clicked)
    
    def _switch_to_grid_view(self):
        """切换到网格视图"""
        self.view_grid_btn.setChecked(True)
        self.view_list_btn.setChecked(False)
        self.grid_view_widget.setVisible(True)
        self.list_view_widget.setVisible(False)
    
    def _switch_to_list_view(self):
        """切换到列表视图"""
        self.view_list_btn.setChecked(True)
        self.view_grid_btn.setChecked(False)
        self.grid_view_widget.setVisible(False)
        self.list_view_widget.setVisible(True)
    
    def _on_task_selected(self, task_name: str):
        """任务被选中"""
        self._selected_task_type = task_name
        self.ok_button.setEnabled(True)
    
    def _on_list_selection_changed(self):
        """列表视图选择改变"""
        selected_items = self.task_list.selectedItems()
        if selected_items:
            task_name = selected_items[0].data(Qt.ItemDataRole.UserRole)
            self._selected_task_type = task_name
            self.ok_button.setEnabled(True)
        else:
            self.ok_button.setEnabled(False)
    
    def _on_list_double_clicked(self, item: QListWidgetItem):
        """列表项双击"""
        task_name = item.data(Qt.ItemDataRole.UserRole)
        self._selected_task_type = task_name
        self.accept()
    
    def _on_search_changed(self, text: str):
        """搜索框内容改变"""
        search_text = text.lower().strip()
        
        if not search_text:
            # 显示所有任务
            filtered_tasks = self._all_task_types
        else:
            # 过滤任务
            filtered_tasks = [t for t in self._all_task_types if search_text in t.lower()]
        
        # 更新网格视图
        self._populate_grid_view(filtered_tasks)
        
        # 更新列表视图
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            task_name = item.data(Qt.ItemDataRole.UserRole)
            item.setHidden(task_name not in filtered_tasks)
    
    def _load_recent_tasks(self) -> List[str]:
        """加载最近使用的任务"""
        try:
            if os.path.exists(self.RECENT_TASKS_FILE):
                with open(self.RECENT_TASKS_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get('recent_tasks', [])
        except Exception as e:
            print(f"加载最近任务失败: {e}")
        return []
    
    def _save_recent_task(self, task_name: str):
        """保存最近使用的任务"""
        try:
            # 更新最近任务列表
            if task_name in self._recent_tasks:
                self._recent_tasks.remove(task_name)
            self._recent_tasks.insert(0, task_name)
            self._recent_tasks = self._recent_tasks[:self.MAX_RECENT_TASKS]
            
            # 确保目录存在
            os.makedirs(os.path.dirname(self.RECENT_TASKS_FILE), exist_ok=True)
            
            # 保存到文件
            with open(self.RECENT_TASKS_FILE, 'w', encoding='utf-8') as f:
                json.dump({'recent_tasks': self._recent_tasks}, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存最近任务失败: {e}")
    
    def selected_task_type(self) -> Optional[str]:
        """返回选中的任务类型"""
        return self._selected_task_type
    
    def accept(self):
        """确认选择"""
        if self._selected_task_type:
            self._save_recent_task(self._selected_task_type)
        super().accept()