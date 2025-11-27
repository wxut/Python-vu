# -*- coding: utf-8 -*-
"""
VU键盘操作任务模块
支持KeyPress、KeyDown、KeyUp等键盘操作
"""
from typing import Dict, Any, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧键盘操作"
TASK_NAME = "无忧键盘操作"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "operation": {
            "label": "操作类型",
            "type": "select",
            "options": ["按键(KeyPress)", "按下(KeyDown)", "释放(KeyUp)"],
            "default": "按键(KeyPress)",
            "tooltip": "选择键盘操作类型"
        },
        "key_code": {
            "label": "按键码",
            "type": "int",
            "default": 0,
            "min": 0,
            "max": 255,
            "tooltip": "虚拟键码(VK Code),如13=回车,32=空格"
        },
        "delay": {
            "label": "延迟时间(ms)",
            "type": "int",
            "default": 50,
            "min": 0,
            "max": 1000,
            "tooltip": "按键操作的延迟时间",
            "condition": {"param": "operation", "value": "按键(KeyPress)"}
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
            "label": "成功后操作",
            "type": "select",
            "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"],
            "default": "执行下一步",
            "tooltip": "操作成功后的行为"
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
            "default": "执行下一步",
            "tooltip": "操作失败后的行为"
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
    """执行无忧键盘操作任务"""
    return execute(params, counters, execution_mode, target_hwnd, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], card_id: Optional[int], stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧键盘操作任务"""
    
    operation = params.get('operation', '按键(KeyPress)')
    key_code = params.get('key_code', 0)
    delay = params.get('delay', 50)
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    logger.info(f"开始执行无忧键盘操作: 类型={operation}, 按键码={key_code}")
    
    try:
        from core.dual_mode_manager import get_dual_mode_manager
        manager = get_dual_mode_manager()
        vu = manager.vu_wrapper
        
        if not vu.is_initialized():
            logger.error("VU插件未初始化")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        if not key_code:
            logger.error("未指定按键码")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        # 执行键盘操作
        result = 0
        if operation == '按键(KeyPress)':
            result = vu.vu.KeyPress(key_code, delay)
        elif operation == '按下(KeyDown)':
            result = vu.vu.KeyDown(key_code)
        elif operation == '释放(KeyUp)':
            result = vu.vu.KeyUp(key_code)
        
        if result > 0:
            logger.info(f"键盘操作成功: {operation} key={key_code}")
            
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            logger.error(f"键盘操作失败")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧键盘操作时发生异常: {e}", exc_info=True)
        return _handle_failure(on_failure_action, failure_jump_id, card_id)

def _handle_success(action: str, jump_id: Optional[int], card_id: Optional[int]) -> Tuple[bool, str, Optional[int]]:
    """处理成功情况"""
    if action == '跳转到步骤':
        return True, '跳转到步骤', jump_id
    elif action == '停止工作流':
        return True, '停止工作流', None
    elif action == '继续执行本步骤':
        return True, '继续执行本步骤', card_id
    else:
        return True, '执行下一步', None

def _handle_failure(action: str, jump_id: Optional[int], card_id: Optional[int]) -> Tuple[bool, str, Optional[int]]:
    """处理失败情况"""
    if action == '跳转到步骤':
        return False, '跳转到步骤', jump_id
    elif action == '停止工作流':
        return False, '停止工作流', None
    elif action == '继续执行本步骤':
        return False, '继续执行本步骤', card_id
    else:
        return False, '执行下一步', None

class VuKeyboardTask:
    """VU键盘操作任务"""
    
    def __init__(self):
        self.name = "VU键盘操作"
        self.description = "使用VU插件进行键盘操作"
    
    def execute(self, vu, params: Dict[str, Any]) -> bool:
        """
        执行键盘操作
        
        Args:
            vu: VU插件实例
            params: 参数字典,包含:
                - operation: 操作类型 (press/down/up)
                - key_code: 按键码
                - delay: 延迟时间(ms)
        """
        try:
            operation = params.get('operation', 'press')
            key_code = params.get('key_code', 0)
            delay = params.get('delay', 50)
            
            if not key_code:
                logger.error("未指定按键码")
                return False
            
            # 执行键盘操作
            if operation == 'press':
                result = vu.KeyPress(key_code, delay)
            elif operation == 'down':
                result = vu.KeyDown(key_code)
            elif operation == 'up':
                result = vu.KeyUp(key_code)
            else:
                logger.error(f"不支持的操作类型: {operation}")
                return False
            
            if result == 1:
                logger.info(f"键盘操作成功: {operation} key={key_code}")
                return True
            else:
                logger.error(f"键盘操作失败: {vu.GetLastError()}")
                return False
                
        except Exception as e:
            logger.error(f"键盘操作异常: {e}")
            return False