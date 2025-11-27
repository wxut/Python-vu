# -*- coding: utf-8 -*-
"""
VU内存操作核心模块
提供内存读写、查找功能
"""

import logging
from typing import Optional, List, Union
from core.vu_wrapper import VUWrapper

logger = logging.getLogger(__name__)


class VUMemory:
    """VU内存操作核心类"""
    
    def __init__(self, vu_wrapper: VUWrapper):
        """
        初始化内存操作器
        
        Args:
            vu_wrapper: VU核心包装器实例
        """
        self.vu = vu_wrapper
    
    # ==================== 读取操作 ====================
    
    def read_int(self, address: int, type_code: int = 0) -> Optional[int]:
        """
        读取整数
        
        Args:
            address: 内存地址
            type_code: 数据类型 (0=int32, 1=int16, 2=int8, 3=uint32, 4=uint16, 5=uint8)
            
        Returns:
            读取的整数值,失败返回None
        """
        try:
            value = self.vu.call_api("ReadInt", address, type_code)
            return value if value is not None else None
        except Exception as e:
            logger.error(f"读取整数失败 [地址:{hex(address)}]: {e}")
            return None
    
    def read_float(self, address: int) -> Optional[float]:
        """
        读取浮点数
        
        Args:
            address: 内存地址
            
        Returns:
            读取的浮点数值,失败返回None
        """
        try:
            value = self.vu.call_api("ReadFloat", address)
            return value if value is not None else None
        except Exception as e:
            logger.error(f"读取浮点数失败 [地址:{hex(address)}]: {e}")
            return None
    
    def read_double(self, address: int) -> Optional[float]:
        """
        读取双精度浮点数
        
        Args:
            address: 内存地址
            
        Returns:
            读取的双精度值,失败返回None
        """
        try:
            value = self.vu.call_api("ReadDouble", address)
            return value if value is not None else None
        except Exception as e:
            logger.error(f"读取双精度失败 [地址:{hex(address)}]: {e}")
            return None
    
    def read_string(self, address: int, length: int, encoding: str = "utf-8") -> Optional[str]:
        """
        读取字符串
        
        Args:
            address: 内存地址
            length: 字符串长度
            encoding: 编码方式 (utf-8/gbk/ascii)
            
        Returns:
            读取的字符串,失败返回None
        """
        try:
            value = self.vu.call_api("ReadString", address, length, encoding)
            return value if value else None
        except Exception as e:
            logger.error(f"读取字符串失败 [地址:{hex(address)}]: {e}")
            return None
    
    def read_data(self, address: int, length: int) -> Optional[bytes]:
        """
        读取原始数据
        
        Args:
            address: 内存地址
            length: 数据长度
            
        Returns:
            读取的字节数据,失败返回None
        """
        try:
            data = self.vu.call_api("ReadData", address, length)
            return data if data else None
        except Exception as e:
            logger.error(f"读取数据失败 [地址:{hex(address)}]: {e}")
            return None
    
    # ==================== 写入操作 ====================
    
    def write_int(self, address: int, value: int, type_code: int = 0) -> bool:
        """
        写入整数
        
        Args:
            address: 内存地址
            value: 要写入的整数
            type_code: 数据类型 (0=int32, 1=int16, 2=int8, 3=uint32, 4=uint16, 5=uint8)
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("WriteInt", address, value, type_code)
            return result == 1
        except Exception as e:
            logger.error(f"写入整数失败 [地址:{hex(address)}]: {e}")
            return False
    
    def write_float(self, address: int, value: float) -> bool:
        """
        写入浮点数
        
        Args:
            address: 内存地址
            value: 要写入的浮点数
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("WriteFloat", address, value)
            return result == 1
        except Exception as e:
            logger.error(f"写入浮点数失败 [地址:{hex(address)}]: {e}")
            return False
    
    def write_double(self, address: int, value: float) -> bool:
        """
        写入双精度浮点数
        
        Args:
            address: 内存地址
            value: 要写入的双精度值
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("WriteDouble", address, value)
            return result == 1
        except Exception as e:
            logger.error(f"写入双精度失败 [地址:{hex(address)}]: {e}")
            return False
    
    def write_string(self, address: int, value: str, encoding: str = "utf-8") -> bool:
        """
        写入字符串
        
        Args:
            address: 内存地址
            value: 要写入的字符串
            encoding: 编码方式 (utf-8/gbk/ascii)
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("WriteString", address, value, encoding)
            return result == 1
        except Exception as e:
            logger.error(f"写入字符串失败 [地址:{hex(address)}]: {e}")
            return False
    
    def write_data(self, address: int, data: bytes) -> bool:
        """
        写入原始数据
        
        Args:
            address: 内存地址
            data: 要写入的字节数据
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("WriteData", address, data)
            return result == 1
        except Exception as e:
            logger.error(f"写入数据失败 [地址:{hex(address)}]: {e}")
            return False
    
    # ==================== 查找操作 ====================
    
    def find_int(self, start: int, end: int, value: int, type_code: int = 0) -> List[int]:
        """
        查找整数
        
        Args:
            start: 起始地址
            end: 结束地址
            value: 要查找的整数
            type_code: 数据类型
            
        Returns:
            找到的地址列表
        """
        try:
            result = self.vu.call_api("FindInt", start, end, value, type_code)
            if result:
                return [int(addr, 16) for addr in result.split('|') if addr]
            return []
        except Exception as e:
            logger.error(f"查找整数失败: {e}")
            return []
    
    def find_float(self, start: int, end: int, value: float) -> List[int]:
        """
        查找浮点数
        
        Args:
            start: 起始地址
            end: 结束地址
            value: 要查找的浮点数
            
        Returns:
            找到的地址列表
        """
        try:
            result = self.vu.call_api("FindFloat", start, end, value)
            if result:
                return [int(addr, 16) for addr in result.split('|') if addr]
            return []
        except Exception as e:
            logger.error(f"查找浮点数失败: {e}")
            return []
    
    def find_double(self, start: int, end: int, value: float) -> List[int]:
        """
        查找双精度浮点数
        
        Args:
            start: 起始地址
            end: 结束地址
            value: 要查找的双精度值
            
        Returns:
            找到的地址列表
        """
        try:
            result = self.vu.call_api("FindDouble", start, end, value)
            if result:
                return [int(addr, 16) for addr in result.split('|') if addr]
            return []
        except Exception as e:
            logger.error(f"查找双精度失败: {e}")
            return []
    
    def find_string(self, start: int, end: int, value: str, encoding: str = "utf-8") -> List[int]:
        """
        查找字符串
        
        Args:
            start: 起始地址
            end: 结束地址
            value: 要查找的字符串
            encoding: 编码方式
            
        Returns:
            找到的地址列表
        """
        try:
            result = self.vu.call_api("FindString", start, end, value, encoding)
            if result:
                return [int(addr, 16) for addr in result.split('|') if addr]
            return []
        except Exception as e:
            logger.error(f"查找字符串失败: {e}")
            return []
    
    def find_data(self, start: int, end: int, data: bytes) -> List[int]:
        """
        查找原始数据
        
        Args:
            start: 起始地址
            end: 结束地址
            data: 要查找的字节数据
            
        Returns:
            找到的地址列表
        """
        try:
            result = self.vu.call_api("FindData", start, end, data)
            if result:
                return [int(addr, 16) for addr in result.split('|') if addr]
            return []
        except Exception as e:
            logger.error(f"查找数据失败: {e}")
            return []