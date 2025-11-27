"""
悬浮卡片窗口组件
在绑定窗口上显示工作流执行状态
"""
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer, QPoint
from PySide6.QtGui import QPainter, QColor, QPen
import win32gui
import win32con


class FloatingCardWidget(QWidget):
    """悬浮卡片窗口，附着在目标窗口右上角"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.target_hwnd = None
        self.current_card_id = None
        self.current_state = "idle"
        
        # 设置窗口属性：无边框、置顶、透明背景
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # 初始化UI
        self._init_ui()
        
        # 位置更新定时器
        self.position_timer = QTimer(self)
        self.position_timer.timeout.connect(self._update_position)
        self.position_timer.setInterval(100)  # 100ms更新一次
        
    def _init_ui(self):
        """初始化UI组件"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # 任务名称标签
        self.task_label = QLabel("等待执行...")
        self.task_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 180);
                padding: 8px 12px;
                border-radius: 6px;
            }
        """)
        layout.addWidget(self.task_label)
        
        self.setFixedSize(200, 50)
        
    def attach_to_window(self, hwnd):
        """附着到指定窗口"""
        self.target_hwnd = hwnd
        if hwnd:
            self._update_position()
            self.position_timer.start()
            self.show()
        else:
            self.position_timer.stop()
            self.hide()
            
    def _update_position(self):
        """更新悬浮窗位置，保持在目标窗口右上角"""
        if not self.target_hwnd:
            return
            
        try:
            # 检查窗口是否仍然存在
            if not win32gui.IsWindow(self.target_hwnd):
                self.attach_to_window(None)
                return
                
            # 获取目标窗口位置和大小
            rect = win32gui.GetWindowRect(self.target_hwnd)
            x, y, right, bottom = rect
            
            # 计算右上角位置（留出边距）
            new_x = right - self.width() - 20
            new_y = y + 20
            
            self.move(new_x, new_y)
            
        except Exception as e:
            print(f"更新悬浮窗位置失败: {e}")
            self.attach_to_window(None)
            
    def update_card_info(self, card_id, task_type, state):
        """更新卡片显示信息
        
        Args:
            card_id: 卡片ID
            task_type: 任务类型
            state: 状态 (executing/success/failure)
        """
        self.current_card_id = card_id
        self.current_state = state
        
        # 状态图标
        state_icons = {
            "executing": "⏳",
            "success": "✓",
            "failure": "✗"
        }
        icon = state_icons.get(state, "●")
        
        # 状态颜色
        state_colors = {
            "executing": "rgba(255, 193, 7, 220)",  # 黄色
            "success": "rgba(76, 175, 80, 220)",    # 绿色
            "failure": "rgba(244, 67, 54, 220)"     # 红色
        }
        bg_color = state_colors.get(state, "rgba(0, 0, 0, 180)")
        
        # 更新显示
        self.task_label.setText(f"{icon} {task_type}")
        self.task_label.setStyleSheet(f"""
            QLabel {{
                color: white;
                font-size: 12px;
                font-weight: bold;
                background-color: {bg_color};
                padding: 8px 12px;
                border-radius: 6px;
            }}
        """)
        
    def hide_card(self):
        """隐藏卡片"""
        self.hide()
        self.position_timer.stop()