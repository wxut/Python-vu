# -*- coding: utf-8 -*-
"""
VU窗口管理任务模块
提供完整的窗口操作功能
"""

import logging
from typing import Dict, Any, Optional, Tuple
from core.vu_window import VUWindow
from core.vu_wrapper import VUWrapper

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧窗口管理"
TASK_NAME = "无忧窗口管理"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "operation": {
            "label": "操作类型",
            "type": "select",
            "options": ["解绑窗口", "获取客户区大小", "获取窗口状态", "设置窗口状态", "设置窗口大小", "移动窗口", "设置窗口标题"],
            "default": "获取窗口状态",
            "tooltip": "选择窗口管理操作"
        },
        "hwnd": {
            "label": "窗口句柄",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "目标窗口句柄",
            "condition": {"param": "operation", "value": ["获取客户区大小", "获取窗口状态", "设置窗口状态", "设置窗口大小", "移动窗口", "设置窗口标题"]}
        },
        "state": {
            "label": "窗口状态",
            "type": "select",
            "options": ["正常", "最小化", "最大化"],
            "default": "正常",
            "tooltip": "窗口显示状态",
            "condition": {"param": "operation", "value": "设置窗口状态"}
        },
        "width": {
            "label": "宽度",
            "type": "int",
            "default": 800,
            "min": 0,
            "tooltip": "窗口宽度",
            "condition": {"param": "operation", "value": "设置窗口大小"}
        },
        "height": {
            "label": "高度",
            "type": "int",
            "default": 600,
            "min": 0,
            "tooltip": "窗口高度",
            "condition": {"param": "operation", "value": "设置窗口大小"}
        },
        "x": {
            "label": "X坐标",
            "type": "int",
            "default": 0,
            "tooltip": "窗口X坐标",
            "condition": {"param": "operation", "value": "移动窗口"}
        },
        "y": {
            "label": "Y坐标",
            "type": "int",
            "default": 0,
            "tooltip": "窗口Y坐标",
            "condition": {"param": "operation", "value": "移动窗口"}
        },
        "text": {
            "label": "窗口标题",
            "type": "text",
            "default": "",
            "tooltip": "新的窗口标题",
            "condition": {"param": "operation", "value": "设置窗口标题"}
        },
        "---next_step_delay---": {"type": "separator", "label": "下一步延迟执行"},
        "enable_next_step_delay": {
            "label": "启用下一步延迟执行",
            "type": "bool",
            "default": False
        },
        "delay_mode": {
            "label": "延迟模式",
            "type": "select",
            "options": ["固定延迟", "随机延迟"],
            "default": "固定延迟",
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
            "condition": {"param": "delay_mode", "value": "随机延迟"}
        },
        "---post_execute---": {"type": "separator", "label": "执行后操作"},
        "on_success": {
            "label": "成功后操作",
            "type": "select",
            "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"],
            "default": "执行下一步"
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
            "label": "失败后操作",
            "type": "select",
            "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"],
            "default": "执行下一步"
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
    """执行无忧窗口管理任务"""
    return execute(params, counters, execution_mode, target_hwnd, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], card_id: Optional[int], stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧窗口管理任务"""
    
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    try:
        window_manager = VUWindowManager()
        
        # 转换状态参数
        if params.get('operation') == '设置窗口状态':
            state_map = {"正常": 0, "最小化": 1, "最大化": 2}
            state_str = params.get('state', '正常')
            params['state'] = state_map.get(state_str, 0)
        
        result = window_manager.execute(params)
        
        if result.get('success', False):
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧窗口管理时发生异常: {e}", exc_info=True)
        return _handle_failure(on_failure_action, failure_jump_id, card_id)

def _handle_success(action: str, jump_id: Optional[int], card_id: Optional[int]) -> Tuple[bool, str, Optional[int]]:
    if action == '跳转到步骤':
        return True, '跳转到步骤', jump_id
    elif action == '停止工作流':
        return True, '停止工作流', None
    elif action == '继续执行本步骤':
        return True, '继续执行本步骤', card_id
    else:
        return True, '执行下一步', None

def _handle_failure(action: str, jump_id: Optional[int], card_id: Optional[int]) -> Tuple[bool, str, Optional[int]]:
    if action == '跳转到步骤':
        return False, '跳转到步骤', jump_id
    elif action == '停止工作流':
        return False, '停止工作流', None
    elif action == '继续执行本步骤':
        return False, '继续执行本步骤', card_id
    else:
        return False, '执行下一步', None

class VUWindowManager:
    """VU窗口管理任务执行器"""
    
    def __init__(self):
        """初始化窗口管理器"""
        self.vu_wrapper = VUWrapper()
        self.window = VUWindow(self.vu_wrapper)
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行窗口管理任务
        
        Args:
            params: 任务参数
                - operation: 操作类型
                - hwnd: 窗口句柄
                - 其他参数根据操作类型而定
                
        Returns:
            执行结果字典
        """
        operation = params.get('operation', '')
        hwnd = params.get('hwnd', 0)
        
        try:
            if operation == 'unbind':
                return {'success': self.window.unbind_window()}
            elif operation == 'get_client_size':
                size = self.window.get_client_size(hwnd)
                return {'success': size is not None, 'size': size}
            elif operation == 'get_state':
                state = self.window.get_window_state(hwnd)
                return {'success': state >= 0, 'state': state}
            elif operation == 'set_state':
                state = params.get('state', 0)
                return {'success': self.window.set_window_state(hwnd, state)}
            elif operation == 'set_size':
                width = params.get('width', 0)
                height = params.get('height', 0)
                return {'success': self.window.set_window_size(hwnd, width, height)}
            elif operation == 'move':
                x = params.get('x', 0)
                y = params.get('y', 0)
                return {'success': self.window.move_window(hwnd, x, y)}
            elif operation == 'set_text':
                text = params.get('text', '')
                return {'success': self.window.set_window_text(hwnd, text)}
            else:
                return {'success': False, 'error': f'未知操作: {operation}'}
        except Exception as e:
            logger.error(f"窗口管理失败: {e}")
            return {'success': False, 'error': str(e)}


def create_task():
    """创建任务实例"""
    return VUWindowManager()