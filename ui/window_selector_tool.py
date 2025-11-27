#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
窗口选择器工具 - 拖拽瞄准器选择窗口
提供类似Spy++的拖拽选择窗口功能
"""

import logging
from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QApplication)
from PySide6.QtCore import Qt, Signal, QPoint, QTimer
from PySide6.QtGui import QPixmap, QPainter, QColor, QPen, QCursor, QIcon
import sys

logger = logging.getLogger(__name__)

# 尝试导入win32相关模块
try:
    import win32gui
    import win32api
    import win32con
    WIN32_AVAILABLE = True
except ImportError:
    WIN32_AVAILABLE = False
    logger.warning("win32gui未安装，窗口选择器功能将不可用")


class WindowSelectorTool(QWidget):
    """
    窗口选择器工具 - 拖拽瞄准器选择窗口
    
    信号:
        window_selected(int, str): 当选择窗口时发出，参数为(窗口句柄, 窗口标题)
    """
    
    window_selected = Signal(int, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("选择窗口")
        self.setFixedSize(300, 120)
        
        # 窗口始终置顶
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        
        # 状态变量
        self.is_selecting = False
        self.last_hwnd = None
        self.timer = None
        
        self._init_ui()
        
    def _init_ui(self):
        """初始化UI"""
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # 说明文字
        info_label = QLabel("拖拽下方的瞄准器图标到目标窗口上")
        info_label.setWordWrap(True)
        info_label.setStyleSheet("color: #555; font-size: 10pt;")
        layout.addWidget(info_label)
        
        # 瞄准器图标
        self.target_label = QLabel()
        self.target_label.setFixedSize(48, 48)
        self.target_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.target_label.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # 创建瞄准器图标
        pixmap = self._create_target_icon(48, 48)
        self.target_label.setPixmap(pixmap)
        
        # 安装事件过滤器以捕获鼠标事件
        self.target_label.installEventFilter(self)
        
        layout.addWidget(self.target_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # 当前窗口信息显示
        self.info_label = QLabel("准备选择窗口...")
        self.info_label.setStyleSheet("""
            QLabel {
                color: #666;
                font-size: 9pt;
                padding: 5px;
                background-color: #f5f5f5;
                border-radius: 3px;
            }
        """)
        self.info_label.setWordWrap(True)
        layout.addWidget(self.info_label)
        
        # 应用样式
        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        
    def _create_target_icon(self, width: int, height: int) -> QPixmap:
        """创建瞄准器图标"""
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 绘制圆形背景
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(0, 123, 255, 200))
        painter.drawEllipse(4, 4, width-8, height-8)
        
        # 绘制瞄准器十字线
        painter.setPen(QPen(QColor(255, 255, 255), 3))
        center = width // 2
        # 水平线
        painter.drawLine(center - 12, center, center + 12, center)
        # 垂直线
        painter.drawLine(center, center - 12, center, center + 12)
        
        # 绘制外圈
        painter.setPen(QPen(QColor(255, 255, 255), 2))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(8, 8, width-16, height-16)
        
        painter.end()
        return pixmap
        
    def eventFilter(self, obj, event):
        """事件过滤器 - 处理拖拽事件"""
        if obj == self.target_label:
            if event.type() == event.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self._start_selection()
                    return True
            elif event.type() == event.Type.MouseButtonRelease:
                if event.button() == Qt.MouseButton.LeftButton and self.is_selecting:
                    self._end_selection()
                    return True
        
        return super().eventFilter(obj, event)
        
    def _start_selection(self):
        """开始选择窗口"""
        if not WIN32_AVAILABLE:
            self.info_label.setText("❌ win32gui未安装，无法选择窗口")
            return
            
        self.is_selecting = True
        self.info_label.setText("🎯 拖拽到目标窗口...")
        
        # 更改鼠标光标为十字准星
        QApplication.setOverrideCursor(Qt.CursorShape.CrossCursor)
        
        # 启动定时器，实时跟踪鼠标下的窗口
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_window_under_cursor)
        self.timer.start(100)  # 每100ms更新一次
        
        logger.debug("开始窗口选择")
        
    def _update_window_under_cursor(self):
        """更新鼠标光标下的窗口信息"""
        if not self.is_selecting or not WIN32_AVAILABLE:
            return
            
        try:
            # 获取鼠标光标位置
            cursor_pos = QCursor.pos()
            x, y = cursor_pos.x(), cursor_pos.y()
            
            # 获取光标位置的窗口句柄
            hwnd = win32gui.WindowFromPoint((x, y))
            
            if hwnd and hwnd != self.last_hwnd:
                self.last_hwnd = hwnd
                
                try:
                    # 获取窗口标题
                    title = win32gui.GetWindowText(hwnd)
                    if not title:
                        title = "(无标题)"
                    
                    # 获取窗口类名
                    class_name = win32gui.GetClassName(hwnd)
                    
                    # 更新显示信息
                    self.info_label.setText(f"🎯 {title}\n类名: {class_name}\nHWND: {hwnd}")
                    
                    # 高亮目标窗口（可选功能）
                    # self._highlight_window(hwnd)
                    
                except Exception as e:
                    logger.debug(f"获取窗口信息失败: {e}")
                    
        except Exception as e:
            logger.error(f"更新窗口信息失败: {e}")
            
    def _end_selection(self):
        """结束选择窗口"""
        self.is_selecting = False
        
        # 停止定时器
        if self.timer:
            self.timer.stop()
            self.timer = None
        
        # 恢复光标
        QApplication.restoreOverrideCursor()
        
        if not WIN32_AVAILABLE:
            return
            
        try:
            # 获取最终的窗口句柄
            cursor_pos = QCursor.pos()
            x, y = cursor_pos.x(), cursor_pos.y()
            hwnd = win32gui.WindowFromPoint((x, y))
            
            if hwnd:
                try:
                    title = win32gui.GetWindowText(hwnd)
                    if not title:
                        title = f"窗口_{hwnd}"
                    
                    logger.info(f"选择了窗口: {title} (HWND: {hwnd})")
                    self.info_label.setText(f"✅ 已选择: {title}")
                    
                    # 发出信号
                    self.window_selected.emit(hwnd, title)
                    
                    # 延迟关闭
                    QTimer.singleShot(500, self.close)
                    
                except Exception as e:
                    logger.error(f"获取窗口信息失败: {e}")
                    self.info_label.setText("❌ 获取窗口信息失败")
            else:
                self.info_label.setText("❌ 未找到有效窗口")
                
        except Exception as e:
            logger.error(f"结束窗口选择失败: {e}")
            self.info_label.setText(f"❌ 选择失败: {e}")
        
        logger.debug("结束窗口选择")
        
    def closeEvent(self, event):
        """关闭事件"""
        # 清理资源
        if self.timer:
            self.timer.stop()
        if self.is_selecting:
            QApplication.restoreOverrideCursor()
        super().closeEvent(event)


class WindowSelectorWidget(QWidget):
    """
    嵌入式窗口选择器组件 - 直接显示在界面上的瞄准器
    可以嵌入到其他对话框中使用
    
    信号:
        window_selected(int, str): 当选择窗口时发出，参数为(窗口句柄, 窗口标题)
    """
    
    window_selected = Signal(int, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._dragging = False
        self._selected_hwnd = 0
        self._update_timer = QTimer(self)
        self._update_timer.timeout.connect(self._update_window_under_cursor)
        self._setup_ui()
        
    def _setup_ui(self):
        """设置UI"""
        from PySide6.QtWidgets import QHBoxLayout
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        
        # 创建瞄准器图标标签
        self.target_label = QLabel(self)
        target_pixmap = self._create_compact_target_icon(28, 28)
        self.target_label.setPixmap(target_pixmap)
        self.target_label.setFixedSize(28, 28)
        self.target_label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.target_label.setToolTip("按住并拖拽此图标到目标窗口进行绑定")
        
        # 状态标签
        self.status_label = QLabel("拖拽瞄准器到目标窗口", self)
        self.status_label.setStyleSheet("color: #666; font-size: 9pt;")
        self.status_label.setMinimumWidth(180)
        
        layout.addWidget(self.target_label)
        layout.addWidget(self.status_label)
        layout.addStretch(1)
        
        # 安装事件过滤器
        self.target_label.installEventFilter(self)
        
    def _create_compact_target_icon(self, width: int, height: int) -> QPixmap:
        """创建紧凑的瞄准器图标"""
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        center_x, center_y = width // 2, height // 2
        
        # 绘制圆形背景
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(0, 120, 215))
        painter.drawEllipse(2, 2, width-4, height-4)
        
        # 绘制瞄准器十字线
        painter.setPen(QPen(QColor(255, 255, 255), 2))
        # 水平线
        painter.drawLine(center_x - 6, center_y, center_x + 6, center_y)
        # 垂直线
        painter.drawLine(center_x, center_y - 6, center_x, center_y + 6)
        
        # 中心点
        painter.setBrush(QColor(255, 255, 255))
        painter.drawEllipse(center_x - 2, center_y - 2, 4, 4)
        
        painter.end()
        return pixmap
    
    def eventFilter(self, obj, event):
        """事件过滤器 - 处理鼠标拖拽"""
        if obj == self.target_label:
            if event.type() == event.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self._start_selection()
                    return True
            elif event.type() == event.Type.MouseButtonRelease:
                if event.button() == Qt.MouseButton.LeftButton and self._dragging:
                    self._end_selection()
                    return True
        return super().eventFilter(obj, event)
    
    def _start_selection(self):
        """开始选择"""
        if not WIN32_AVAILABLE:
            self.status_label.setText("❌ win32gui未安装")
            self.status_label.setStyleSheet("color: #d13438; font-size: 9pt;")
            return
            
        self._dragging = True
        self.status_label.setText("🎯 正在选择窗口...")
        self.status_label.setStyleSheet("color: #0078d7; font-size: 9pt; font-weight: bold;")
        
        # 改变鼠标光标
        self.target_label.setCursor(Qt.CursorShape.CrossCursor)
        
        # 启动定时器更新窗口信息
        self._update_timer.start(100)
        
        logger.info("开始窗口选择")
    
    def _update_window_under_cursor(self):
        """更新光标下的窗口信息"""
        if not self._dragging or not WIN32_AVAILABLE:
            return
            
        try:
            cursor_pos = QCursor.pos()
            hwnd = win32gui.WindowFromPoint((cursor_pos.x(), cursor_pos.y()))
            
            if hwnd and hwnd != 0:
                title = win32gui.GetWindowText(hwnd)
                if title:
                    # 截断过长的标题
                    display_title = title if len(title) <= 30 else title[:27] + "..."
                    self.status_label.setText(f"📌 {display_title}")
                else:
                    class_name = win32gui.GetClassName(hwnd)
                    self.status_label.setText(f"📌 [{class_name}]")
                    
                self._selected_hwnd = hwnd
        except Exception as e:
            logger.error(f"获取窗口信息失败: {e}")
    
    def _end_selection(self):
        """结束选择"""
        self._dragging = False
        self._update_timer.stop()
        
        # 恢复光标
        self.target_label.setCursor(Qt.CursorShape.PointingHandCursor)
        
        if not WIN32_AVAILABLE:
            return
        
        if self._selected_hwnd and self._selected_hwnd != 0:
            try:
                title = win32gui.GetWindowText(self._selected_hwnd)
                if not title:
                    class_name = win32gui.GetClassName(self._selected_hwnd)
                    title = f"[{class_name}]"
                
                logger.info(f"选择了窗口: {title} (HWND: {self._selected_hwnd})")
                
                # 发射信号
                self.window_selected.emit(self._selected_hwnd, title)
                
                # 显示成功状态
                display_title = title if len(title) <= 25 else title[:22] + "..."
                self.status_label.setText(f"✅ 已选择: {display_title}")
                self.status_label.setStyleSheet("color: #107c10; font-size: 9pt;")
                
                # 3秒后恢复默认状态
                QTimer.singleShot(3000, self._reset_status)
                
            except Exception as e:
                logger.error(f"处理选择的窗口失败: {e}")
                self.status_label.setText("❌ 选择失败")
                self.status_label.setStyleSheet("color: #d13438; font-size: 9pt;")
                QTimer.singleShot(3000, self._reset_status)
        else:
            self.status_label.setText("❌ 未选择有效窗口")
            self.status_label.setStyleSheet("color: #d13438; font-size: 9pt;")
            QTimer.singleShot(3000, self._reset_status)
        
        self._selected_hwnd = 0
    
    def _reset_status(self):
        """重置状态"""
        if not self._dragging:
            self.status_label.setText("拖拽瞄准器到目标窗口")
            self.status_label.setStyleSheet("color: #666; font-size: 9pt;")


# 测试代码
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = WindowSelectorTool()
    
    def on_window_selected(hwnd, title):
        print(f"选择了窗口: {title} (句柄: {hwnd})")
    
    window.window_selected.connect(on_window_selected)
    window.show()
    
    sys.exit(app.exec())