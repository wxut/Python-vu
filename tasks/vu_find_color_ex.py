# -*- coding: utf-8 -*-
"""
VU找色Ex任务 - 查找所有匹配的颜色
"""

import logging
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)

TASK_NAME = "VU找色Ex"
TASK_TYPE = "VU找色Ex"


def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """返回参数定义"""
    from .task_utils import get_standard_next_step_delay_params, get_standard_action_params, merge_params_definitions
    
    params = {
        "---task_params---": {"type": "separator", "label": "主要任务参数"},
        "target_color": {"label": "目标颜色(RGB)", "type": "text", "default": "FF0000", "widget_hint": "colorpicker"},
        "confidence": {"label": "相似度", "type": "float", "default": 0.9, "min": 0.1, "max": 1.0, "decimals": 2},
        "search_direction": {"label": "查找方向", "type": "select", "options": ["从左到右", "从右到左", "从上到下", "从下到上"], "default": "从左到右"},
        "max_results": {"label": "最大结果数", "type": "int", "default": 10, "min": 1, "max": 100},
        
        "---post_exec---": {"type": "separator", "label": "执行后操作"},
        "on_success": {"type": "select", "label": "找到颜色时", "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"], "default": "执行下一步"},
        "success_jump_target_id": {"type": "int", "label": "成功跳转目标ID", "required": False, "widget_hint": "card_selector", "condition": {"param": "on_success", "value": "跳转到步骤"}},
        "on_failure": {"type": "select", "label": "未找到颜色时", "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"], "default": "执行下一步"},
        "failure_jump_target_id": {"type": "int", "label": "失败跳转目标ID", "required": False, "widget_hint": "card_selector", "condition": {"param": "on_failure", "value": "跳转到步骤"}}
    }
    
    return merge_params_definitions(params, get_standard_next_step_delay_params(), get_standard_action_params())


def execute_task(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
                target_hwnd: Optional[int], window_region: Optional[Tuple[int, int, int, int]],
                card_id: Optional[int], **kwargs) -> Tuple[bool, str, Optional[int]]:
    """执行VU找色Ex任务"""
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
        
        result = vu.vu.FindColorEx(x1, y1, x2, y2, params.get('target_color', 'FF0000'),
                                    params.get('confidence', 0.9), find_dir)
        
        if result:
            positions = _parse_positions(result, params.get('max_results', 10))
            if positions:
                logger.info(f"找到{len(positions)}个颜色位置: {positions}")
                counters[f'vu_findcolor_ex_count_{card_id}'] = len(positions)
                counters[f'vu_findcolor_ex_x_{card_id}'] = positions[0][0]
                counters[f'vu_findcolor_ex_y_{card_id}'] = positions[0][1]
                return handle_success_action(params, card_id, kwargs.get('stop_checker'))
        
        logger.info("未找到匹配的颜色")
        return handle_failure_action(params, card_id)
        
    except Exception as e:
        logger.error(f"VU找色Ex执行失败: {e}")
        from .task_utils import handle_failure_action
        return handle_failure_action(params, card_id)