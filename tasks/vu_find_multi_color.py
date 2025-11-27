# -*- coding: utf-8 -*-
"""
VU多色查找任务 - 查找多个颜色组合的位置
"""

import logging
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)

TASK_NAME = "VU多色查找"
TASK_TYPE = "VU多色查找"


def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """返回参数定义"""
    from .task_utils import get_standard_next_step_delay_params, get_standard_action_params, merge_params_definitions
    
    params = {
        "---task_params---": {"type": "separator", "label": "主要任务参数"},
        "first_color": {"label": "第一个颜色(RGB)", "type": "text", "default": "FF0000", "widget_hint": "colorpicker"},
        "offset_colors": {"label": "偏移颜色串", "type": "text", "default": "10|10|00FF00,20|20|0000FF", "tooltip": "格式: x1|y1|color1,x2|y2|color2"},
        "confidence": {"label": "相似度", "type": "float", "default": 0.9, "min": 0.1, "max": 1.0, "decimals": 2},
        "search_direction": {"label": "查找方向", "type": "select", "options": ["从左到右", "从右到左", "从上到下", "从下到上"], "default": "从左到右"},
        
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
    """执行VU多色查找任务"""
    try:
        from core.vu_wrapper import get_vu_wrapper
        from .task_utils import handle_success_action, handle_failure_action
        from .vu_find_pic_ex import _get_search_region, _parse_positions
        
        vu = get_vu_wrapper()
        if not vu or not vu.is_initialized():
            logger.error("VU插件未初始化")
            return handle_failure_action(params, card_id)
        
        dir_map = {"从左到右": 0, "从右到左": 1, "从上到下": 2, "从下到上": 3}
        find_dir = dir_map.get(params.get('search_direction', '从左到右'), 0)
        
        x1, y1, x2, y2 = _get_search_region(vu, window_region)
        result = vu.vu.FindMultiColorEx(x1, y1, x2, y2, params.get('first_color', 'FF0000'),
                                        params.get('offset_colors', ''),
                                        params.get('confidence', 0.9), find_dir)
        
        if positions := _parse_positions(result):
            x, y = positions[0]
            logger.info(f"找到多色位置: ({x}, {y})")
            counters[f'vu_multicolor_x_{card_id}'] = x
            counters[f'vu_multicolor_y_{card_id}'] = y
            return handle_success_action(params, card_id, kwargs.get('stop_checker'))
        
        logger.info("未找到匹配的多色组合")
        return handle_failure_action(params, card_id)
        
    except Exception as e:
        logger.error(f"VU多色查找执行失败: {e}")
        from .task_utils import handle_failure_action
        return handle_failure_action(params, card_id)