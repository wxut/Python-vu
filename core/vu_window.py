# -*- coding: utf-8 -*-
"""
VU窗口操作封装

提供窗口查找、标题获取、位置大小获取等功能
"""

import ctypes
import logging
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


class VUWindow:
    """VU窗口操作封装
    
    提供以下功能:
    - 查找窗口
    - 获取窗口标题
    - 获取窗口位置和大小
    """

    def __init__(self, vu_wrapper):
        """初始化窗口操作
        
        Args:
            vu_wrapper: VUWrapper实例
        """
        self.wrapper = vu_wrapper
        self.vu = vu_wrapper.vu if vu_wrapper.vu else None

    def find_window(self, class_name: str = "", title: str = "") -> int:
        """查找窗口
        
        Args:
            class_name: 窗口类名，为空则不限制
            title: 窗口标题，为空则不限制
            
        Returns:
            int: 窗口句柄，未找到返回0
            
        Example:
            hwnd = vu_window.find_window(title="记事本")
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return 0
        try:
            hwnd = self.vu.FindWindow(class_name, title)
            return hwnd if hwnd else 0
        except Exception as e:
            logger.error(f"查找窗口失败: {e}")
            return 0

    def get_window_title(self, hwnd: int) -> str:
        """获取窗口标题
        
        Args:
            hwnd: 窗口句柄
            
        Returns:
            str: 窗口标题，失败返回空字符串
            
        Example:
            title = vu_window.get_window_title(hwnd)
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return ""
        try:
            title = self.vu.GetWindowTitle(hwnd)
            return title if title else ""
        except Exception as e:
            logger.error(f"获取窗口标题失败: {e}")
            return ""

    def get_window_rect(self, hwnd: int) -> Optional[Tuple[int, int, int, int]]:
        """获取窗口位置和大小
        
        Args:
            hwnd: 窗口句柄
            
        Returns:
            tuple: (x1, y1, x2, y2) 窗口左上角和右下角坐标，失败返回None
            
        Example:
            rect = vu_window.get_window_rect(hwnd)
            if rect:
                x1, y1, x2, y2 = rect
                width = x2 - x1
                height = y2 - y1
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return None
        try:
            x1 = ctypes.c_long(0)
            y1 = ctypes.c_long(0)
            x2 = ctypes.c_long(0)
            y2 = ctypes.c_long(0)
            ret = self.vu.GetWindowRect(hwnd, x1, y1, x2, y2)
            if ret:
                return (x1.value, y1.value, x2.value, y2.value)
        except Exception as e:
            logger.error(f"获取窗口位置失败: {e}")
        return None
    
    def unbind_window(self) -> bool:
        """解绑窗口
        
        Returns:
            bool: 成功返回True
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            result = self.vu.UnBindWindow()
            return result == 1
        except Exception as e:
            logger.error(f"解绑窗口失败: {e}")
            return False
    
    def get_client_size(self, hwnd: int) -> Optional[Tuple[int, int]]:
        """获取窗口客户区大小
        
        Args:
            hwnd: 窗口句柄
            
        Returns:
            tuple: (width, height) 客户区宽高,失败返回None
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return None
        try:
            width = ctypes.c_long(0)
            height = ctypes.c_long(0)
            ret = self.vu.GetClientSize(hwnd, width, height)
            if ret:
                return (width.value, height.value)
        except Exception as e:
            logger.error(f"获取客户区大小失败: {e}")
        return None
    
    def get_window_state(self, hwnd: int) -> int:
        """获取窗口状态
        
        Args:
            hwnd: 窗口句柄
            
        Returns:
            int: 窗口状态 (0=正常, 1=最小化, 2=最大化)
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return -1
        try:
            return self.vu.GetWindowState(hwnd)
        except Exception as e:
            logger.error(f"获取窗口状态失败: {e}")
            return -1
    
    def set_window_state(self, hwnd: int, state: int) -> bool:
        """设置窗口状态
        
        Args:
            hwnd: 窗口句柄
            state: 窗口状态 (0=正常, 1=最小化, 2=最大化)
            
        Returns:
            bool: 成功返回True
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            result = self.vu.SetWindowState(hwnd, state)
            return result == 1
        except Exception as e:
            logger.error(f"设置窗口状态失败: {e}")
            return False
    
    def set_window_size(self, hwnd: int, width: int, height: int) -> bool:
        """设置窗口大小
        
        Args:
            hwnd: 窗口句柄
            width: 宽度
            height: 高度
            
        Returns:
            bool: 成功返回True
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            result = self.vu.SetWindowSize(hwnd, width, height)
            return result == 1
        except Exception as e:
            logger.error(f"设置窗口大小失败: {e}")
            return False
    
    def move_window(self, hwnd: int, x: int, y: int) -> bool:
        """移动窗口
        
        Args:
            hwnd: 窗口句柄
            x: X坐标
            y: Y坐标
            
        Returns:
            bool: 成功返回True
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            result = self.vu.MoveWindow(hwnd, x, y)
            return result == 1
        except Exception as e:
            logger.error(f"移动窗口失败: {e}")
            return False
    
    def set_window_text(self, hwnd: int, text: str) -> bool:
        """设置窗口标题
        
        Args:
            hwnd: 窗口句柄
            text: 新标题
            
        Returns:
            bool: 成功返回True
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            result = self.vu.SetWindowText(hwnd, text)
            return result == 1
        except Exception as e:
            logger.error(f"设置窗口标题失败: {e}")
            return False
