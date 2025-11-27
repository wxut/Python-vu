# -*- coding: utf-8 -*-
"""
VU JSON处理核心模块
提供JSON读写、解析和构建功能
"""

import logging
from typing import Any, Optional, Union
from core.vu_wrapper import VUWrapper

logger = logging.getLogger(__name__)


class VUJson:
    """VU JSON处理核心类"""
    
    def __init__(self, vu_wrapper: VUWrapper):
        """
        初始化JSON处理器
        
        Args:
            vu_wrapper: VU核心包装器实例
        """
        self.vu = vu_wrapper
        self._json_handles = {}  # 存储JSON句柄
    
    def read_input(self, json_str: str) -> int:
        """
        读取JSON字符串并创建句柄
        
        Args:
            json_str: JSON字符串
            
        Returns:
            JSON句柄ID,失败返回-1
        """
        try:
            handle = self.vu.call_api("JsonReadInPut", json_str)
            if handle > 0:
                self._json_handles[handle] = True
                logger.info(f"JSON读取成功,句柄: {handle}")
            return handle
        except Exception as e:
            logger.error(f"JSON读取失败: {e}")
            return -1
    
    def read_get_str(self, handle: int, key: str) -> Optional[str]:
        """
        从JSON中获取字符串值
        
        Args:
            handle: JSON句柄
            key: 键名
            
        Returns:
            字符串值,失败返回None
        """
        try:
            value = self.vu.call_api("JsonReadGetStr", handle, key)
            return value if value else None
        except Exception as e:
            logger.error(f"获取JSON字符串失败 [{key}]: {e}")
            return None
    
    def read_get_num(self, handle: int, key: str) -> Optional[Union[int, float]]:
        """
        从JSON中获取数值
        
        Args:
            handle: JSON句柄
            key: 键名
            
        Returns:
            数值,失败返回None
        """
        try:
            value = self.vu.call_api("JsonReadGetNum", handle, key)
            return value
        except Exception as e:
            logger.error(f"获取JSON数值失败 [{key}]: {e}")
            return None
    
    def write_create_obj(self) -> int:
        """
        创建JSON写入对象
        
        Returns:
            JSON句柄ID,失败返回-1
        """
        try:
            handle = self.vu.call_api("JsonWriteCreateObj")
            if handle > 0:
                self._json_handles[handle] = True
                logger.info(f"JSON对象创建成功,句柄: {handle}")
            return handle
        except Exception as e:
            logger.error(f"创建JSON对象失败: {e}")
            return -1
    
    def write_add_str(self, handle: int, key: str, value: str) -> bool:
        """
        向JSON添加字符串
        
        Args:
            handle: JSON句柄
            key: 键名
            value: 字符串值
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("JsonWriteAddStr", handle, key, value)
            return result == 1
        except Exception as e:
            logger.error(f"添加JSON字符串失败 [{key}]: {e}")
            return False
    
    def write_add_num(self, handle: int, key: str, value: Union[int, float]) -> bool:
        """
        向JSON添加数值
        
        Args:
            handle: JSON句柄
            key: 键名
            value: 数值
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("JsonWriteAddNum", handle, key, value)
            return result == 1
        except Exception as e:
            logger.error(f"添加JSON数值失败 [{key}]: {e}")
            return False
    
    def write_output(self, handle: int) -> Optional[str]:
        """
        输出JSON字符串
        
        Args:
            handle: JSON句柄
            
        Returns:
            JSON字符串,失败返回None
        """
        try:
            json_str = self.vu.call_api("JsonWriteOutPut", handle)
            return json_str if json_str else None
        except Exception as e:
            logger.error(f"输出JSON失败: {e}")
            return None
    
    def release_handle(self, handle: int) -> bool:
        """
        释放JSON句柄
        
        Args:
            handle: JSON句柄
            
        Returns:
            成功返回True
        """
        try:
            if handle in self._json_handles:
                del self._json_handles[handle]
                logger.info(f"JSON句柄已释放: {handle}")
            return True
        except Exception as e:
            logger.error(f"释放JSON句柄失败: {e}")
            return False
    
    def __del__(self):
        """析构函数,清理所有句柄"""
        for handle in list(self._json_handles.keys()):
            self.release_handle(handle)