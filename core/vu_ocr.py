# -*- coding: utf-8 -*-
"""
VU OCR操作封装

提供文字识别、查找等功能
"""

import ctypes
import logging
from typing import Optional, Tuple, List

logger = logging.getLogger(__name__)


class VUOCR:
    """VU OCR操作封装
    
    提供以下功能:
    - 文字识别
    - 文字查找
    - 字典管理
    """

    def __init__(self, vu_wrapper):
        """初始化OCR操作
        
        Args:
            vu_wrapper: VUWrapper实例
        """
        self.wrapper = vu_wrapper
        self.vu = vu_wrapper.vu if vu_wrapper.vu else None

    def recognize_text(self, x1: int, y1: int, x2: int, y2: int,
                       color_format: str = "", sim: float = 0.9) -> str:
        """识别区域文字
        
        Args:
            x1, y1, x2, y2: 识别区域
            color_format: 颜色格式
            sim: 相似度
            
        Returns:
            str: 识别到的文字
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return ""
        try:
            result = self.vu.Ocr(x1, y1, x2, y2, color_format, sim)
            return result if result else ""
        except Exception as e:
            logger.error(f"OCR识别失败: {e}")
            return ""

    def find_str(self, x1: int, y1: int, x2: int, y2: int, text: str,
                 color_format: str = "000000-000000", similarity: float = 0.9) -> Optional[Tuple[int, int]]:
        """查找文字位置
        
        Args:
            x1, y1, x2, y2: 搜索区域
            text: 要查找的文本
            color_format: 颜色格式
            similarity: 相似度
            
        Returns:
            tuple: (x, y) 找到返回坐标，未找到返回None
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return None
        try:
            x = ctypes.c_long(0)
            y = ctypes.c_long(0)
            ret = self.vu.FindStr(x1, y1, x2, y2, text, color_format, similarity, x, y)
            return (x.value, y.value) if ret > 0 else None
        except Exception as e:
            logger.error(f"查找文字失败: {e}")
            return None

    def find_str_ex(self, x1: int, y1: int, x2: int, y2: int, text: str,
                    color_format: str = "000000-000000", similarity: float = 0.9) -> List[Tuple[int, int]]:
        """查找所有文字位置
        
        Args:
            x1, y1, x2, y2: 搜索区域
            text: 要查找的文本
            color_format: 颜色格式
            similarity: 相似度
            
        Returns:
            list: [(x1, y1), (x2, y2), ...] 所有找到的坐标
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return []
        try:
            result = self.vu.FindStrEx(x1, y1, x2, y2, text, color_format, similarity)
            if result:
                return [(int(parts[0]), int(parts[1]))
                        for item in result.split('|')
                        if ',' in item and len(parts := item.split(',')) >= 2]
            return []
        except Exception as e:
            logger.error(f"查找所有文字失败: {e}")
            return []

    def find_text(self, text: str, x1: int, y1: int, x2: int, y2: int) -> Optional[Tuple[int, int]]:
        """查找文字位置（兼容旧接口）"""
        return self.find_str(x1, y1, x2, y2, text)

    def set_dict(self, dict_path: str) -> bool:
        """设置OCR字典
        
        Args:
            dict_path: 字典文件路径
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            ret = self.vu.SetDict(0, dict_path)
            return ret == 1
        except Exception as e:
            logger.error(f"设置字典失败: {e}")
            return False

    def use_default_dict(self) -> bool:
        """使用默认字典"""
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            ret = self.vu.UseDict(0)
            return ret == 1
        except Exception as e:
            logger.error(f"使用默认字典失败: {e}")
            return False
