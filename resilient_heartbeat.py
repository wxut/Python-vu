#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
弹性心跳监控器 - 已禁用（使用VU插件注册替代）
"""

import logging

logger = logging.getLogger(__name__)

# 保留类定义以避免导入错误，但功能已禁用
class ResilientHeartbeatMonitor:
    """弹性心跳监控器 - 存根类（已禁用）"""
    
    def __init__(self, *args, **kwargs):
        logger.info("心跳监控器已禁用（使用VU插件注册）")
        self.running = False
    
    def start(self):
        """启动心跳监控（已禁用）"""
        logger.info("心跳监控器启动被跳过（已禁用）")
        pass
    
    def stop(self):
        """停止心跳监控（已禁用）"""
        pass
    
    def get_status(self):
        """获取监控状态（已禁用）"""
        return {"status": "disabled"}
    
    def is_thread_healthy(self):
        """检查线程健康（已禁用）"""
        return True

# 保留配置类以避免导入错误
class RetryConfig:
    def __init__(self, *args, **kwargs):
        pass

class CircuitBreakerConfig:
    def __init__(self, *args, **kwargs):
        pass

class HealthCheckConfig:
    def __init__(self, *args, **kwargs):
        pass
