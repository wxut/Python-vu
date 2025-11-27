#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
性能监控工具 - 用于测试和验证性能优化效果
"""

import time
import logging
from typing import Dict, Any, Optional
from contextlib import contextmanager

logger = logging.getLogger(__name__)


class PerformanceMonitor:
    """性能监控器"""
    
    def __init__(self):
        self._metrics: Dict[str, Dict[str, Any]] = {}
    
    @contextmanager
    def measure(self, operation: str):
        """测量操作耗时"""
        start_time = time.time()
        try:
            yield
        finally:
            elapsed = time.time() - start_time
            self._record(operation, elapsed)
    
    def _record(self, operation: str, elapsed: float):
        """记录性能数据"""
        if operation not in self._metrics:
            self._metrics[operation] = {
                'count': 0,
                'total_time': 0.0,
                'min_time': float('inf'),
                'max_time': 0.0
            }
        
        metrics = self._metrics[operation]
        metrics['count'] += 1
        metrics['total_time'] += elapsed
        metrics['min_time'] = min(metrics['min_time'], elapsed)
        metrics['max_time'] = max(metrics['max_time'], elapsed)
    
    def get_report(self) -> str:
        """生成性能报告"""
        if not self._metrics:
            return "无性能数据"
        
        lines = ["性能监控报告", "=" * 60]
        
        for operation, metrics in sorted(self._metrics.items()):
            avg_time = metrics['total_time'] / metrics['count']
            lines.append(f"\n操作: {operation}")
            lines.append(f"  执行次数: {metrics['count']}")
            lines.append(f"  总耗时: {metrics['total_time']:.3f}s")
            lines.append(f"  平均耗时: {avg_time:.3f}s")
            lines.append(f"  最小耗时: {metrics['min_time']:.3f}s")
            lines.append(f"  最大耗时: {metrics['max_time']:.3f}s")
        
        return "\n".join(lines)
    
    def clear(self):
        """清空统计数据"""
        self._metrics.clear()


# 全局实例
_monitor: Optional[PerformanceMonitor] = None


def get_performance_monitor() -> PerformanceMonitor:
    """获取全局性能监控器"""
    global _monitor
    if _monitor is None:
        _monitor = PerformanceMonitor()
    return _monitor