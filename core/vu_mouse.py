# -*- coding: utf-8 -*-
"""
VU鼠标操作封装

提供鼠标移动、点击、滚轮等操作
"""

import ctypes
import logging
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


class VUMouse:
    """VU鼠标操作封装
    
    提供以下功能:
    - 鼠标移动
    - 左键/右键/中键点击
    - 鼠标按下/释放
    - 滚轮操作
    """

    def __init__(self, vu_wrapper):
        """初始化鼠标操作
        
        Args:
            vu_wrapper: VUWrapper实例
        """
        self.wrapper = vu_wrapper
        self.vu = vu_wrapper.vu if vu_wrapper.vu else None

    def _execute_action(self, action_name: str, action_func) -> bool:
        """执行鼠标操作的通用方法
        
        Args:
            action_name: 操作名称(用于日志)
            action_func: 要执行的函数
            
        Returns:
            bool: 成功返回True
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            return action_func() > 0
        except Exception as e:
            logger.error(f"{action_name}失败: {e}")
            return False

    def move_to(self, x: int, y: int) -> bool:
        """移动鼠标到指定坐标"""
        return self._execute_action("移动鼠标", lambda: self.vu.MoveTo(x, y))

    def left_click(self) -> bool:
        """鼠标左键单击"""
        return self._execute_action("左键单击", self.vu.LeftClick)

    def right_click(self) -> bool:
        """鼠标右键单击"""
        return self._execute_action("右键单击", self.vu.RightClick)

    def double_click(self) -> bool:
        """鼠标左键双击"""
        return self._execute_action("双击", self.vu.LeftDoubleClick)

    def middle_click(self) -> bool:
        """鼠标中键单击"""
        return self._execute_action("中键单击", self.vu.MiddleClick)

    def left_down(self) -> bool:
        """鼠标左键按下"""
        return self._execute_action("左键按下", self.vu.LeftDown)

    def left_up(self) -> bool:
        """鼠标左键释放"""
        return self._execute_action("左键释放", self.vu.LeftUp)

    def right_down(self) -> bool:
        """鼠标右键按下"""
        return self._execute_action("右键按下", self.vu.RightDown)

    def right_up(self) -> bool:
        """鼠标右键释放"""
        return self._execute_action("右键释放", self.vu.RightUp)

    def middle_down(self) -> bool:
        """鼠标中键按下"""
        return self._execute_action("中键按下", self.vu.MiddleDown)

    def middle_up(self) -> bool:
        """鼠标中键释放"""
        return self._execute_action("中键释放", self.vu.MiddleUp)

    def wheel_up(self) -> bool:
        """鼠标滚轮向上"""
        return self._execute_action("滚轮向上", self.vu.WheelUp)

    def wheel_down(self) -> bool:
        """鼠标滚轮向下"""
        return self._execute_action("滚轮向下", self.vu.WheelDown)

    def wheel(self, clicks: int) -> bool:
        """鼠标滚轮滚动
        
        Args:
            clicks: 滚动量，正数向上，负数向下
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            action = self.vu.WheelUp if clicks > 0 else self.vu.WheelDown
            for _ in range(abs(clicks)):
                action()
            return True
        except Exception as e:
            logger.error(f"滚轮滚动失败: {e}")
            return False

    def move_r(self, rx: int, ry: int) -> bool:
        """相对移动鼠标"""
        return self._execute_action("相对移动", lambda: self.vu.MoveR(rx, ry))

    def move_to_ex(self, x: int, y: int, w: int, h: int) -> bool:
        """扩展移动鼠标"""
        return self._execute_action("扩展移动", lambda: self.vu.MoveToEx(x, y, w, h))

    def click_at(self, x: int, y: int, button: str = 'left') -> bool:
        """在指定位置点击
        
        Args:
            x, y: 点击坐标
            button: 按键类型 ('left', 'right', 'middle')
        """
        if not self.move_to(x, y):
            return False
        
        click_map = {
            'left': self.left_click,
            'right': self.right_click,
            'middle': self.middle_click
        }
        return click_map.get(button, self.left_click)()

    def get_cursor_pos(self) -> Optional[Tuple[int, int]]:
        """获取鼠标位置"""
        if not self.wrapper.is_initialized() or not self.vu:
            return None
        try:
            x = ctypes.c_long(0)
            y = ctypes.c_long(0)
            ret = self.vu.GetCursorPos(x, y)
            if ret:
                return (x.value, y.value)
        except Exception as e:
            logger.error(f"获取鼠标位置失败: {e}")
        return None
