# -*- coding: utf-8 -*-
"""
任务工具模块 - 提供任务执行的通用工具函数
"""
import logging
import time
import random

logger = logging.getLogger(__name__)


def handle_next_step_delay(params: dict, stop_checker=None):
    """
    处理下一步延迟执行
    
    Args:
        params: 任务参数字典
        stop_checker: 停止检查函数
    """
    if not params.get('enable_next_step_delay', False):
        return
    
    delay_mode = params.get('delay_mode', '固定延迟')
    
    if delay_mode == '固定延迟':
        delay = params.get('fixed_delay', 1.0)
    else:  # 随机延迟
        min_delay = params.get('min_delay', 0.5)
        max_delay = params.get('max_delay', 2.0)
        delay = random.uniform(min_delay, max_delay)
    
    logger.info(f"下一步延迟执行: {delay:.2f}秒")
    
    # 可中断的延迟
    _interruptible_sleep(delay, stop_checker)


def _interruptible_sleep(duration: float, stop_checker=None):
    """
    可中断的睡眠函数
    
    Args:
        duration: 睡眠时长（秒）
        stop_checker: 停止检查函数
    """
    if duration <= 0:
        return
    
    # 每0.1秒检查一次停止信号
    elapsed = 0
    check_interval = 0.1
    
    while elapsed < duration:
        if stop_checker and callable(stop_checker) and stop_checker():
            logger.info("检测到停止信号，中断延迟")
            break
        
        sleep_time = min(check_interval, duration - elapsed)
        time.sleep(sleep_time)
        elapsed += sleep_time