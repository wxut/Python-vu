# -*- coding: utf-8 -*-
"""
VU窗口绑定任务模块
支持BindWindow、UnBindWindow等窗口绑定操作
"""
from typing import Dict, Any, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧窗口绑定"
TASK_NAME = "无忧窗口绑定"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "operation": {
            "label": "操作类型",
            "type": "select",
            "options": ["绑定窗口(BindWindow)", "解绑窗口(UnBindWindow)"],
            "default": "绑定窗口(BindWindow)",
            "tooltip": "选择窗口绑定操作类型"
        },
        "hwnd": {
            "label": "窗口句柄",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "目标窗口的句柄值",
            "condition": {"param": "operation", "value": "绑定窗口(BindWindow)"}
        },
        "display": {
            "label": "图色模式",
            "type": "select",
            "options": ["normal", "gdi", "gdi2", "dx", "dx2", "dx3"],
            "default": "normal",
            "tooltip": "图色获取模式",
            "condition": {"param": "operation", "value": "绑定窗口(BindWindow)"}
        },
        "mouse": {
            "label": "鼠标模式",
            "type": "select",
            "options": ["normal", "windows", "windows2", "windows3", "dx"],
            "default": "normal",
            "tooltip": "鼠标操作模式",
            "condition": {"param": "operation", "value": "绑定窗口(BindWindow)"}
        },
        "keypad": {
            "label": "键盘模式",
            "type": "select",
            "options": ["normal", "windows", "dx"],
            "default": "normal",
            "tooltip": "键盘操作模式",
            "condition": {"param": "operation", "value": "绑定窗口(BindWindow)"}
        },
        "mode": {
            "label": "工作模式",
            "type": "select",
            "options": ["前台模式", "后台模式"],
            "default": "前台模式",
            "tooltip": "选择前台或后台工作模式",
            "condition": {"param": "operation", "value": "绑定窗口(BindWindow)"}
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
    """执行无忧窗口绑定任务"""
    return execute(params, counters, execution_mode, target_hwnd, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], card_id: Optional[int], stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧窗口绑定任务"""
    
    operation = params.get('operation', '绑定窗口(BindWindow)')
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    logger.info(f"开始执行无忧窗口绑定: 操作={operation}")
    
    try:
        from core.dual_mode_manager import get_dual_mode_manager
        manager = get_dual_mode_manager()
        vu = manager.vu_wrapper
        
        if not vu.is_initialized():
            logger.error("VU插件未初始化")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        result = 0
        
        if operation == '解绑窗口(UnBindWindow)':
            # 解绑窗口
            result = vu.vu.UnBindWindow()
            if result > 0:
                logger.info("窗口解绑成功")
            else:
                logger.error(f"窗口解绑失败")
        
        elif operation == '绑定窗口(BindWindow)':
            # 绑定窗口
            hwnd = params.get('hwnd', 0)
            if not hwnd:
                logger.error("未指定窗口句柄")
                return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
            display = params.get('display', 'normal')
            mouse = params.get('mouse', 'normal')
            keypad = params.get('keypad', 'normal')
            mode_str = params.get('mode', '前台模式')
            mode = 0 if mode_str == '前台模式' else 1
            
            result = vu.vu.BindWindow(hwnd, display, mouse, keypad, mode)
            if result > 0:
                logger.info(f"窗口绑定成功: hwnd={hwnd}, display={display}, mouse={mouse}, keypad={keypad}, mode={mode}")
            else:
                logger.error(f"窗口绑定失败")
        
        if result > 0:
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧窗口绑定时发生异常: {e}", exc_info=True)
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

class VuWindowBindTask:
    """VU窗口绑定任务"""
    
    def __init__(self):
        self.name = "VU窗口绑定"
        self.description = "绑定或解绑窗口进行后台操作"
    
    def execute(self, vu, params: Dict[str, Any]) -> bool:
        """
        执行窗口绑定操作
        
        Args:
            vu: VU插件实例
            params: 参数字典,包含:
                - operation: 操作类型 (bind/unbind)
                - hwnd: 窗口句柄
                - display: 图色模式 (normal/gdi/gdi2/dx/dx2等)
                - mouse: 鼠标模式 (normal/windows/windows2等)
                - keypad: 键盘模式 (normal/windows等)
        """
        try:
            operation = params.get('operation', 'bind')
            hwnd = params.get('hwnd', 0)
            
            if operation == 'unbind':
                # 解绑窗口
                result = vu.UnBindWindow()
                if result == 1:
                    logger.info("窗口解绑成功")
                    return True
                else:
                    logger.error(f"窗口解绑失败: {vu.GetLastError()}")
                    return False
            
            elif operation == 'bind':
                # 绑定窗口
                if not hwnd:
                    logger.error("未指定窗口句柄")
                    return False
                
                display = params.get('display', 'normal')
                mouse = params.get('mouse', 'normal')
                keypad = params.get('keypad', 'normal')
                mode = params.get('mode', 0)  # 0=前台,1=后台
                
                result = vu.BindWindow(hwnd, display, mouse, keypad, mode)
                if result == 1:
                    logger.info(f"窗口绑定成功: hwnd={hwnd}, display={display}, mouse={mouse}, keypad={keypad}")
                    return True
                else:
                    logger.error(f"窗口绑定失败: {vu.GetLastError()}")
                    return False
            
            else:
                logger.error(f"不支持的操作类型: {operation}")
                return False
                
        except Exception as e:
            logger.error(f"窗口绑定操作异常: {e}")
            return False