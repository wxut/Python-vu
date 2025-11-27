# -*- coding: utf-8 -*-
"""
VU色块查找任务 - 查找指定颜色的色块区域
"""

import logging
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)

TASK_NAME = "VU色块查找"
TASK_TYPE = "VU色块查找"


def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """返回参数定义"""
    from .task_utils import get_standard_next_step_delay_params, get_standard_action_params, merge_params_definitions
    
    params = {
        "---task_params---": {"type": "separator", "label": "主要任务参数"},
        "target_color": {"label": "目标颜色(RGB)", "type": "text", "default": "FF0000", "widget_hint": "colorpicker"},
        "min_width": {"label": "最小宽度", "type": "int", "default": 10, "min": 1},
        "min_height": {"label": "最小高度", "type": "int", "default": 10, "min": 1},
        "confidence": {"label": "相似度", "type": "float", "default": 0.9, "min": 0.1, "max": 1.0, "decimals": 2},
        
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
    """执行VU色块查找任务"""
    try:
        from core.vu_wrapper import get_vu_wrapper
        from .task_utils import handle_success_action, handle_failure_action
        from .vu_find_pic_ex import _get_search_region
        
        vu = get_vu_wrapper()
        if not vu or not vu.is_initialized():
            logger.error("VU插件未初始化")
            return handle_failure_action(params, card_id)
        
        x1, y1, x2, y2 = _get_search_region(vu, window_region)
        result = vu.vu.FindColorBlockEx(x1, y1, x2, y2, params.get('target_color', 'FF0000'),
                                        params.get('min_width', 10), params.get('min_height', 10),
                                        params.get('confidence', 0.9))
        
        if result and '|' in result:
            first_block = result.split('|')[0]
            parts = first_block.split(',')
            if len(parts) >= 4:
                x, y, w, h = map(int, parts[:4])
                logger.info(f"找到色块: 位置({x}, {y}), 大小({w}x{h})")
                counters[f'vu_colorblock_x_{card_id}'] = x
                counters[f'vu_colorblock_y_{card_id}'] = y
                counters[f'vu_colorblock_w_{card_id}'] = w
                counters[f'vu_colorblock_h_{card_id}'] = h
                return handle_success_action(params, card_id, kwargs.get('stop_checker'))
        
        logger.info("未找到匹配的色块")
        return handle_failure_action(params, card_id)
        
    except Exception as e:
        logger.error(f"VU色块查找执行失败: {e}")
        from .task_utils import handle_failure_action
        return handle_failure_action(params, card_id)