# -*- coding: utf-8 -*-
"""
VU图像操作封装 - 性能优化版

提供图像识别、找图、找色等功能
优化特性：
- 模板图片缓存
- 减少重复加载
"""

import ctypes
import os
import time
import threading
import logging
from typing import Optional, Tuple, List, Dict

logger = logging.getLogger(__name__)


class VUImage:
    """VU图像操作封装 - 性能优化版
    
    提供以下功能：
    - 找图（FindPic）
    - 找图Ex（FindPicEx，找所有）
    - 找色（FindColor）
    - 找色Ex（FindColorEx）
    - 截图（CaptureScreen）
    
    性能优化：
    - 模板图片路径缓存（避免重复验证）
    - 线程安全的缓存机制
    """

    # 缓存配置常量
    CACHE_TTL_SECONDS = 300  # 5分钟
    CACHE_MAX_SIZE = 100  # 最大缓存条目数

    def __init__(self, vu_wrapper):
        """初始化图像操作

        Args:
            vu_wrapper: VUWrapper实例
        """
        self.wrapper = vu_wrapper
        self.vu = vu_wrapper.vu if vu_wrapper.vu else None
        
        # 性能优化：图片路径缓存
        self._pic_cache: Dict[str, float] = {}  # path -> last_access_time
        self._cache_lock = threading.Lock()
        self._cache_ttl = self.CACHE_TTL_SECONDS

    def _clean_expired_cache(self):
        """清理过期缓存"""
        try:
            current_time = time.time()
            expired_keys = [k for k, v in self._pic_cache.items()
                            if current_time - v > self._cache_ttl]
            if expired_keys:
                for key in expired_keys:
                    del self._pic_cache[key]
                logger.debug(f"清理了{len(expired_keys)}个过期缓存条目")
        except Exception as e:
            logger.warning(f"清理缓存时出错: {e}")

    def _validate_pic_path(self, pic_name: str) -> bool:
        """验证图片路径（带缓存）"""
        with self._cache_lock:
            current_time = time.time()
            
            # 定期清理缓存
            if len(self._pic_cache) > self.CACHE_MAX_SIZE:
                self._clean_expired_cache()
                
                # 如果清理后仍超过阈值,清理最旧的条目
                if len(self._pic_cache) > self.CACHE_MAX_SIZE:
                    # 按时间排序,删除最旧的条目
                    sorted_items = sorted(self._pic_cache.items(), key=lambda x: x[1])
                    num_to_remove = len(self._pic_cache) - self.CACHE_MAX_SIZE + 10  # 额外删除10个
                    for key, _ in sorted_items[:num_to_remove]:
                        del self._pic_cache[key]
                    logger.debug(f"强制清理了{num_to_remove}个最旧的缓存条目")
            
            # 检查缓存
            if pic_name in self._pic_cache:
                last_time = self._pic_cache[pic_name]
                if current_time - last_time < self._cache_ttl:
                    # 更新访问时间(LRU策略)
                    self._pic_cache[pic_name] = current_time
                    return True
                else:
                    # 缓存过期,删除
                    del self._pic_cache[pic_name]
            
            # 验证路径
            if os.path.exists(pic_name):
                self._pic_cache[pic_name] = current_time
                return True
            return False

    def _get_region(self, region: Optional[Tuple[int, int, int, int]]) -> Tuple[int, int, int, int]:
        """获取查找区域"""
        if region:
            return region
        width, height = self.wrapper.get_screen_size()
        return (0, 0, width, height)

    def find_pic(self, pic_name: str, region: Optional[Tuple[int, int, int, int]] = None,
                 threshold: float = 0.9, find_type: int = 0) -> Optional[Tuple[int, int]]:
        """找图

        Args:
            pic_name: 图片路径
            region: 查找区域 (x1, y1, x2, y2)，None表示全屏
            threshold: 相似度阈值 0.0-1.0
            find_type: 查找类型

        Returns:
            tuple: (x, y) 找到返回坐标，未找到返回None
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return None

        try:
            x = ctypes.c_long(0)
            y = ctypes.c_long(0)
            x1_val, y1_val, x2_val, y2_val = self._get_region(region)
            
            ret = self.vu.FindPic(x1_val, y1_val, x2_val, y2_val, pic_name, "000000", threshold, find_type, x, y)
            return (x.value, y.value) if ret > 0 else None

        except Exception as e:
            logger.error(f"找图异常: {e}")
            return None

    def find_pic_ex(self, pic_name: str, region: Optional[Tuple[int, int, int, int]] = None,
                    threshold: float = 0.9, find_type: int = 0) -> List[Tuple[int, int]]:
        """找图Ex（查找所有匹配的图片）

        Args:
            pic_name: 图片路径
            region: 查找区域
            threshold: 相似度阈值
            find_type: 查找类型

        Returns:
            list: [(x1, y1), (x2, y2), ...] 所有找到的坐标
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return []

        try:
            x1_val, y1_val, x2_val, y2_val = self._get_region(region)
            result = self.vu.FindPicEx(x1_val, y1_val, x2_val, y2_val, pic_name, "000000", threshold, find_type)

            if result:
                return [(int(parts[0]), int(parts[1]))
                        for item in result.split('|')
                        if ',' in item and len(parts := item.split(',')) >= 2]
            return []

        except Exception as e:
            logger.error(f"找图Ex异常: {e}")
            return []

    def find_color(self, color: str, region: Optional[Tuple[int, int, int, int]] = None,
                   threshold: float = 0.9) -> Optional[Tuple[int, int]]:
        """找色

        Args:
            color: 颜色值，格式："RRGGBB"
            region: 查找区域
            threshold: 相似度阈值

        Returns:
            tuple: (x, y) 找到返回坐标，未找到返回None
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return None

        try:
            x = ctypes.c_long(0)
            y = ctypes.c_long(0)
            x1_val, y1_val, x2_val, y2_val = self._get_region(region)
            
            ret = self.vu.FindColor(x1_val, y1_val, x2_val, y2_val, color, threshold, 0, x, y)
            return (x.value, y.value) if ret > 0 else None

        except Exception as e:
            logger.error(f"找色异常: {e}")
            return None

    def find_color_ex(self, color: str, region: Optional[Tuple[int, int, int, int]] = None,
                      threshold: float = 0.9) -> List[Tuple[int, int]]:
        """找色Ex（查找所有匹配的颜色）

        Args:
            color: 颜色值
            region: 查找区域
            threshold: 相似度阈值

        Returns:
            list: [(x1, y1), (x2, y2), ...] 所有找到的坐标
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return []

        try:
            x1_val, y1_val, x2_val, y2_val = self._get_region(region)
            result = self.vu.FindColorEx(x1_val, y1_val, x2_val, y2_val, color, threshold, 0)

            if result:
                return [(int(parts[0]), int(parts[1]))
                        for item in result.split('|')
                        if ',' in item and len(parts := item.split(',')) >= 2]
            return []

        except Exception as e:
            logger.error(f"找色Ex异常: {e}")
            return []

    def capture_to_file(self, x1: int, y1: int, x2: int, y2: int, file_path: str) -> bool:
        """截图保存到文件

        Args:
            x1, y1, x2, y2: 截图区域
            file_path: 保存路径

        Returns:
            bool: 成功返回True
        """
        if not self.wrapper.is_initialized():
            return False

        try:
            ret = self.vu.CaptureScreen(x1, y1, x2, y2, file_path)
            return ret > 0
        except Exception as e:
            logger.error(f"截图异常: {e}")
            return False

    def get_pixel_color(self, x: int, y: int) -> str:
        """获取指定坐标的颜色

        Args:
            x, y: 坐标

        Returns:
            str: 颜色值 "RRGGBB"，失败返回空字符串
        """
        if not self.wrapper.is_initialized():
            return ""

        try:
            color = self.vu.GetColor(x, y)
            return color if color else ""
        except Exception as e:
            logger.error(f"获取颜色异常: {e}")
            return ""

    def compare_pic(self, pic1: str, pic2: str, similarity: str) -> bool:
        """比较两张图片
        
        Args:
            pic1: 图片1路径
            pic2: 图片2路径
            similarity: 相似度字符串
            
        Returns:
            bool: 相似返回True
        """
        if not self.wrapper.is_initialized():
            return False
        try:
            ret = self.vu.CmpPic(pic1, pic2, similarity)
            return ret > 0
        except Exception as e:
            logger.error(f"比较图片失败: {e}")
            return False

    def cmp_color(self, x: int, y: int, color: str, threshold: float = 0.9) -> bool:
        """比较指定坐标的颜色

        Args:
            x, y: 坐标
            color: 期望的颜色值 "RRGGBB"
            threshold: 相似度阈值

        Returns:
            bool: 匹配返回True
        """
        if not self.wrapper.is_initialized():
            return False

        try:
            sim_str = str(int(threshold * 100))
            ret = self.vu.CmpColor(x, y, color, sim_str)
            return ret > 0
        except Exception as e:
            logger.error(f"比较颜色异常: {e}")
            return False

    def clear_cache(self) -> None:
        """清理所有缓存"""
        with self._cache_lock:
            cache_size = len(self._pic_cache)
            self._pic_cache.clear()
            if cache_size > 0:
                logger.info(f"已清理所有缓存,共{cache_size}个条目")
    
    def get_cache_stats(self) -> Dict[str, int]:
        """获取缓存统计信息
        
        Returns:
            dict: 包含缓存统计信息的字典
        """
        with self._cache_lock:
            current_time = time.time()
            expired_count = sum(1 for v in self._pic_cache.values()
                              if current_time - v > self._cache_ttl)
            return {
                'total': len(self._pic_cache),
                'expired': expired_count,
                'active': len(self._pic_cache) - expired_count,
                'max_size': self.CACHE_MAX_SIZE,
                'ttl_seconds': self._cache_ttl
            }
    
    def load_pic(self, pic_path: str) -> int:
        """加载图片并返回句柄
        
        Args:
            pic_path: 图片路径
            
        Returns:
            int: 图片句柄,失败返回-1
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return -1
        try:
            handle = self.vu.LoadPic(pic_path)
            return handle if handle > 0 else -1
        except Exception as e:
            logger.error(f"加载图片失败: {e}")
            return -1
    
    def free_pic(self, handle: int) -> bool:
        """释放图片句柄
        
        Args:
            handle: 图片句柄
            
        Returns:
            bool: 成功返回True
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return False
        try:
            ret = self.vu.FreePic(handle)
            return ret == 1
        except Exception as e:
            logger.error(f"释放图片失败: {e}")
            return False
    
    def get_pic_size(self, handle: int) -> Optional[Tuple[int, int]]:
        """获取图片尺寸
        
        Args:
            handle: 图片句柄
            
        Returns:
            tuple: (width, height) 图片尺寸,失败返回None
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return None
        try:
            width = ctypes.c_long(0)
            height = ctypes.c_long(0)
            ret = self.vu.GetPicSize(handle, width, height)
            if ret:
                return (width.value, height.value)
        except Exception as e:
            logger.error(f"获取图片尺寸失败: {e}")
        return None
    
    def get_screen_data(self, x1: int, y1: int, x2: int, y2: int) -> Optional[bytes]:
        """获取屏幕数据
        
        Args:
            x1, y1, x2, y2: 区域坐标
            
        Returns:
            bytes: 屏幕数据,失败返回None
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return None
        try:
            data = self.vu.GetScreenData(x1, y1, x2, y2)
            return data if data else None
        except Exception as e:
            logger.error(f"获取屏幕数据失败: {e}")
            return None
    
    def get_screen_data_bmp(self, x1: int, y1: int, x2: int, y2: int) -> Optional[bytes]:
        """获取屏幕BMP数据
        
        Args:
            x1, y1, x2, y2: 区域坐标
            
        Returns:
            bytes: BMP数据,失败返回None
        """
        if not self.wrapper.is_initialized() or not self.vu:
            return None
        try:
            data = self.vu.GetScreenDataBmp(x1, y1, x2, y2)
            return data if data else None
        except Exception as e:
            logger.error(f"获取BMP数据失败: {e}")
            return None
