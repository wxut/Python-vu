# -*- coding: utf-8 -*-
"""
VU找色任务模块
使用VU插件的FindColor功能查找指定颜色
"""

import ctypes
import logging
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧找色"
TASK_NAME = "无忧找色"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "x1": {
            "label": "左上X",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "查找区域左上角X坐标"
        },
        "y1": {
            "label": "左上Y",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "查找区域左上角Y坐标"
        },
        "x2": {
            "label": "右下X",
            "type": "int",
            "default": 1920,
            "min": 0,
            "tooltip": "查找区域右下角X坐标"
        },
        "y2": {
            "label": "右下Y",
            "type": "int",
            "default": 1080,
            "min": 0,
            "tooltip": "查找区域右下角Y坐标"
        },
        "color_format": {
            "label": "颜色值(RGB)",
            "type": "text",
            "default": "0000FF",
            "tooltip": "RGB十六进制格式,例如: FF0000(红色) 或 0000FF(蓝色)"
        },
        "similarity": {
            "label": "相似度",
            "type": "float",
            "default": 0.9,
            "min": 0.0,
            "max": 1.0,
            "step": 0.01,
            "decimals": 2,
            "tooltip": "颜色匹配相似度(0.0-1.0, 1.0为完全匹配)"
        },
        "direction": {
            "label": "查找方向",
            "type": "select",
            "options": [
                "从左到右,从上到下",
                "从左到右,从下到上",
                "从右到左,从上到下",
                "从右到左,从下到上",
                "从中心向四周",
                "从四周向中心"
            ],
            "default": "从左到右,从上到下",
            "tooltip": "选择颜色查找的方向"
        },
        "---next_step_delay---": {"type": "separator", "label": "下一步延迟执行"},
        "enable_next_step_delay": {
            "label": "启用下一步延迟执行",
            "type": "bool",
            "default": False,
            "tooltip": "勾选后,执行完当前操作会等待指定时间再执行下一步"
        },
        "delay_mode": {
            "label": "延迟模式",
            "type": "select",
            "options": ["固定延迟", "随机延迟"],
            "default": "固定延迟",
            "tooltip": "选择固定延迟时间还是随机延迟时间",
            "condition": {"param": "enable_next_step_delay", "value": True}
        },
        "fixed_delay": {
            "label": "固定延迟 (秒)",
            "type": "float",
            "default": 1.0,
            "min": 0.0,
            "max": 3600.0,
            "step": 0.1,
            "decimals": 2,
            "tooltip": "设置固定的延迟时间",
            "condition": {"param": "delay_mode", "value": "固定延迟"}
        },
        "min_delay": {
            "label": "最小延迟 (秒)",
            "type": "float",
            "default": 0.5,
            "min": 0.0,
            "max": 3600.0,
            "step": 0.1,
            "decimals": 2,
            "tooltip": "设置随机延迟的最小值",
            "condition": {"param": "delay_mode", "value": "随机延迟"}
        },
        "max_delay": {
            "label": "最大延迟 (秒)",
            "type": "float",
            "default": 2.0,
            "min": 0.0,
            "max": 3600.0,
            "step": 0.1,
            "decimals": 2,
            "tooltip": "设置随机延迟的最大值",
            "condition": {"param": "delay_mode", "value": "随机延迟"}
        },
        "---post_execute---": {"type": "separator", "label": "执行后操作"},
        "on_success": {
            "label": "找到颜色后操作",
            "type": "select",
            "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"],
            "default": "执行下一步",
            "tooltip": "找到颜色后的操作"
        },
        "success_jump_target_id": {
            "label": "成功跳转目标ID",
            "type": "int",
            "default": 0,
            "min": 0,
            "widget_hint": "card_selector",
            "condition": {"param": "on_success", "value": "跳转到步骤"}
        },
        "on_failure": {
            "label": "未找到颜色后操作",
            "type": "select",
            "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"],
            "default": "执行下一步",
            "tooltip": "未找到颜色后的操作"
        },
        "failure_jump_target_id": {
            "label": "失败跳转目标ID",
            "type": "int",
            "default": 0,
            "min": 0,
            "widget_hint": "card_selector",
            "condition": {"param": "on_failure", "value": "跳转到步骤"}
        }
    }

def execute_task(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
                target_hwnd: Optional[int], window_region: Optional[tuple], card_id: Optional[int],
                get_image_data=None, **kwargs) -> Tuple[bool, str, Optional[int]]:
    """执行无忧找色任务"""
    return execute(params, counters, execution_mode, target_hwnd, window_region, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], window_region: Optional[tuple], card_id: Optional[int],
           stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧找色任务"""
    
    x1 = params.get('x1', 0)
    y1 = params.get('y1', 0)
    x2 = params.get('x2', 1920)
    y2 = params.get('y2', 1080)
    color_format = params.get('color_format', '0000FF')
    similarity = params.get('similarity', 0.9)
    direction_str = params.get('direction', '从左到右,从上到下')
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    # 转换查找方向
    direction_map = {
        "从左到右,从上到下": 0,
        "从左到右,从下到上": 1,
        "从右到左,从上到下": 2,
        "从右到左,从下到上": 3,
        "从中心向四周": 4,
        "从四周向中心": 5
    }
    direction = direction_map.get(direction_str, 0)
    
    logger.info(f"开始执行无忧找色: 区域=({x1},{y1})-({x2},{y2}), 颜色={color_format}, 相似度={similarity}, 方向={direction}")
    
    try:
        from core.dual_mode_manager import get_dual_mode_manager
        manager = get_dual_mode_manager()
        vu = manager.vu_wrapper
        
        if not vu.is_initialized():
            logger.error("VU插件未初始化")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        x, y = ctypes.c_long(0), ctypes.c_long(0)
        result = vu.vu.FindColor(x1, y1, x2, y2, color_format, similarity, direction, 
                                ctypes.byref(x), ctypes.byref(y))
        
        if result == 1:
            found_x, found_y = x.value, y.value
            logger.info(f"找到颜色 {color_format} 位置: ({found_x}, {found_y})")
            
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            logger.info(f"未找到颜色 {color_format}")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧找色时发生异常: {e}", exc_info=True)
        return _handle_failure(on_failure_action, failure_jump_id, card_id)

def _handle_success(action: str, jump_id: Optional[int], card_id: Optional[int]) -> Tuple[bool, str, Optional[int]]:
    """处理成功情况(找到颜色)"""
    if action == '跳转到步骤':
        return True, '跳转到步骤', jump_id
    elif action == '停止工作流':
        return True, '停止工作流', None
    elif action == '继续执行本步骤':
        return True, '继续执行本步骤', card_id
    else:
        return True, '执行下一步', None

def _handle_failure(action: str, jump_id: Optional[int], card_id: Optional[int]) -> Tuple[bool, str, Optional[int]]:
    """处理失败情况(未找到颜色)"""
    if action == '跳转到步骤':
        return False, '跳转到步骤', jump_id
    elif action == '停止工作流':
        return False, '停止工作流', None
    elif action == '继续执行本步骤':
        return False, '继续执行本步骤', card_id
    else:
        return False, '执行下一步', None