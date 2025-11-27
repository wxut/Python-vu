# -*- coding: utf-8 -*-
"""
VU键盘操作封装

提供键盘按键、文本输入等功能
"""

import logging
from typing import Union

logger = logging.getLogger(__name__)


class VUKeyboard:
    """VU键盘操作封装
    
    提供以下功能:
    - 按键操作
    - 文本输入
    """

    def __init__(self, vu_wrapper):
        """初始化键盘操作
        
        Args:
            vu_wrapper: VUWrapper实例
        """
        self.wrapper = vu_wrapper
        self.vu = vu_wrapper.vu if vu_wrapper.vu else None

    def _encode_text(self, text: str) -> bytes:
        """编码文本为字节
        
        Args:
            text: 要编码的文本
            
        Returns:
            bytes: 编码后的字节
        """
        try:
            return text.encode('gbk')
        except UnicodeEncodeError:
            return text.encode('utf-8', errors='ignore')

    def key_press(self, key: Union[str, bytes]) -> bool:
        """按键
        
        Args:
            key: 按键或文本
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            if isinstance(key, str):
                key = self._encode_text(key)
            return self.vu.KeyPress(key) > 0
        except Exception as e:
            logger.error(f"按键失败: {e}")
            return False

    def key_down(self, key: Union[str, int]) -> bool:
        """按下按键"""
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            return self.vu.KeyDown(key) > 0
        except Exception as e:
            logger.error(f"按下按键失败: {e}")
            return False

    def key_up(self, key: Union[str, int]) -> bool:
        """释放按键"""
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            return self.vu.KeyUp(key) > 0
        except Exception as e:
            logger.error(f"释放按键失败: {e}")
            return False

    def send_string(self, text: str) -> bool:
        """发送字符串
        
        Args:
            text: 要输入的文本
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            encoded_text = self._encode_text(text)
            return self.vu.SendString(encoded_text) > 0
        except Exception as e:
            logger.error(f"发送字符串失败: {e}")
            return False

    def type_text(self, text: str) -> bool:
        """输入文字"""
        return self.key_press(text)
