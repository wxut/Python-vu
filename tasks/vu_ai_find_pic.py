# -*- coding: utf-8 -*-
"""
VU AI找图任务 - 使用AI算法查找图片
"""

import logging
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)

TASK_NAME = "VU AI找图"
TASK_TYPE = "VU AI找图"


def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """返回参数定义"""
    from .task_utils import get_standard_next_step_delay_params, get_standard_action_params, merge_params_definitions
    
    params = {
        "---task_params---": {"type": "separator", "label": "主要任务参数"},
        "image_path": {"label": "图片路径", "type": "text", "default": "", "widget_hint": "file_selector"},
        "confidence": {"label": "相似度", "type": "float", "default": 0.8, "min": 0.1, "max": 1.0, "decimals": 2},
        "ai_mode": {"label": "AI模式", "type": "select", "options": ["快速模式", "精确模式"], "default": "快速模式"},
        
        "---post_exec---": {"type": "separator", "label": "执行后操作"},
        "on_success": {"type": "select", "label": "找到时", "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"], "default": "执行下一步"},
        "success_jump_target_id": {"type": "int", "label": "成功跳转目标ID", "required": False, "widget_hint": "card_selector", "condition": {"param": "on_success", "value": "跳转到步骤"}},
        "on_failure": {"type": "select", "label": "未找到时", "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"], "default": "执行下一步"},
        "failure_jump_target_id": {"type": "int", "label": "失败跳转目标ID", "required": False, "widget_hint": "card_selector", "condition": {"param": "on_failure", "value": "跳转到步骤"}}
    }
    
    return merge_params_definitions(params, get_standard_next_step_delay_params(), get_standard_action_params())


def execute_task(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str, 
                target_hwnd: Optional[int], window_region: Optional[Tuple[int, int, int, int]], 
                card_id: Optional[int], **kwargs) -> Tuple[bool, str, Optional[int]]:
    """执行VU AI找图任务"""
    try:
        from core.vu_wrapper import get_vu_wrapper
        from .task_utils import handle_success_action, handle_failure_action
        from .vu_find_pic_ex import _get_search_region, _parse_positions
        
        vu = get_vu_wrapper()
        if not vu or not vu.is_initialized():
            logger.error("VU插件未初始化")
            return handle_failure_action(params, card_id)
        
        mode = 0 if params.get('ai_mode', '快速模式') == '快速模式' else 1
        x1, y1, x2, y2 = _get_search_region(vu, window_region)
        result = vu.vu.AiFindPic(x1, y1, x2, y2, params.get('image_path', ''),
                                 params.get('confidence', 0.8), mode)
        
        if positions := _parse_positions(result):
            x, y = positions[0]
            logger.info(f"AI找到图片位置: ({x}, {y})")
            counters[f'vu_ai_pic_x_{card_id}'] = x
            counters[f'vu_ai_pic_y_{card_id}'] = y
            return handle_success_action(params, card_id, kwargs.get('stop_checker'))
        
        logger.info("AI未找到匹配的图片")
        return handle_failure_action(params, card_id)
        
    except Exception as e:
        logger.error(f"VU AI找图执行失败: {e}")
        from .task_utils import handle_failure_action
        return handle_failure_action(params, card_id)