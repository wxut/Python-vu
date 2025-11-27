#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
截图缓存管理器 - 性能优化模块

实现智能截图缓存机制，避免重复截图开销
特性：
- 基于时间的缓存失效
- 基于窗口句柄的缓存隔离
- 线程安全
- 自动内存管理
"""

import time
import threading
import logging
from typing import Optional, Tuple, Dict, Any
import numpy as np

logger = logging.getLogger(__name__)


class ScreenshotCache:
    """截图缓存管理器"""
    
    def __init__(self, cache_ttl: float = 0.1, max_cache_size: int = 10):
        """
        初始化截图缓存
        
        Args:
            cache_ttl: 缓存有效期（秒），默认100ms
            max_cache_size: 最大缓存数量
        """
        self.cache_ttl = cache_ttl
        self.max_cache_size = max_cache_size
        
        # 缓存数据结构
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._cache_lock = threading.RLock()
        
        # 统计信息
        self._hits = 0
        self._misses = 0
        self._total_requests = 0
        
        logger.info(f"截图缓存初始化: TTL={cache_ttl}s, 最大缓存数={max_cache_size}")
    
    def _generate_cache_key(self, hwnd: Optional[int], region: Optional[Tuple[int, int, int, int]], 
                           mode: str) -> str:
        """生成缓存键"""
        hwnd_str = str(hwnd) if hwnd else "全屏"
        region_str = f"{region}" if region else "全区域"
        return f"{mode}_{hwnd_str}_{region_str}"
    
    def get(self, hwnd: Optional[int], region: Optional[Tuple[int, int, int, int]], 
            mode: str = "screenshot") -> Optional[np.ndarray]:
        """
        获取缓存的截图
        
        Args:
            hwnd: 窗口句柄
            region: 截图区域
            mode: 截图模式
            
        Returns:
            Optional[np.ndarray]: 缓存的截图，未命中返回None
        """
        self._total_requests += 1
        cache_key = self._generate_cache_key(hwnd, region, mode)
        
        with self._cache_lock:
            if cache_key in self._cache:
                cache_entry = self._cache[cache_key]
                
                # 检查是否过期
                if time.time() - cache_entry['timestamp'] < self.cache_ttl:
                    self._hits += 1
                    cache_entry['hits'] += 1
                    logger.debug(f"截图缓存命中: {cache_key} (总命中率: {self.get_hit_rate():.1%})")
                    return cache_entry['screenshot'].copy()  # 返回副本防止被修改
                else:
                    # 过期，删除缓存
                    del self._cache[cache_key]
                    logger.debug(f"截图缓存过期: {cache_key}")
            
            self._misses += 1
            return None
    
    def put(self, screenshot: np.ndarray, hwnd: Optional[int], 
            region: Optional[Tuple[int, int, int, int]], mode: str = "screenshot"):
        """
        存储截图到缓存
        
        Args:
            screenshot: 截图数据
            hwnd: 窗口句柄
            region: 截图区域
            mode: 截图模式
        """
        if screenshot is None:
            return
        
        cache_key = self._generate_cache_key(hwnd, region, mode)
        
        with self._cache_lock:
            # 检查缓存大小限制
            if len(self._cache) >= self.max_cache_size:
                self._evict_oldest()
            
            # 存储缓存
            self._cache[cache_key] = {
                'screenshot': screenshot.copy(),  # 存储副本
                'timestamp': time.time(),
                'hits': 0
            }
            logger.debug(f"截图已缓存: {cache_key} (缓存数: {len(self._cache)}/{self.max_cache_size})")
    
    def _evict_oldest(self):
        """清除最旧的缓存项"""
        if not self._cache:
            return
        
        # 找到最旧的缓存项
        oldest_key = min(self._cache.items(), key=lambda x: x[1]['timestamp'])[0]
        del self._cache[oldest_key]
        logger.debug(f"清除最旧缓存: {oldest_key}")
    
    def clear(self):
        """清空所有缓存"""
        with self._cache_lock:
            cache_count = len(self._cache)
            self._cache.clear()
            logger.info(f"清空截图缓存: 已清除{cache_count}个缓存项")
    
    def get_stats(self) -> Dict[str, Any]:
        """获取缓存统计信息"""
        with self._cache_lock:
            return {
                'total_requests': self._total_requests,
                'hits': self._hits,
                'misses': self._misses,
                'hit_rate': self.get_hit_rate(),
                'cache_size': len(self._cache),
                'max_cache_size': self.max_cache_size,
                'cache_ttl': self.cache_ttl
            }
    
    def get_hit_rate(self) -> float:
        """获取缓存命中率"""
        if self._total_requests == 0:
            return 0.0
        return self._hits / self._total_requests
    
    def invalidate_window(self, hwnd: int):
        """使指定窗口的所有缓存失效"""
        with self._cache_lock:
            keys_to_remove = [k for k in self._cache.keys() if f"_{hwnd}_" in k]
            for key in keys_to_remove:
                del self._cache[key]
            if keys_to_remove:
                logger.debug(f"已清除窗口{hwnd}的{len(keys_to_remove)}个缓存项")


# 全局缓存实例
_screenshot_cache: Optional[ScreenshotCache] = None
_cache_lock = threading.Lock()


def get_screenshot_cache() -> ScreenshotCache:
    """获取全局截图缓存实例"""
    global _screenshot_cache
    if _screenshot_cache is None:
        with _cache_lock:
            if _screenshot_cache is None:
                _screenshot_cache = ScreenshotCache()
    return _screenshot_cache


def clear_screenshot_cache():
    """清空全局截图缓存"""
    cache = get_screenshot_cache()
    cache.clear()


def get_cache_stats() -> Dict[str, Any]:
    """获取缓存统计信息"""
    cache = get_screenshot_cache()
    return cache.get_stats()