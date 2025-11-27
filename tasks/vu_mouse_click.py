# -*- coding: utf-8 -*-
"""
无忧鼠标点击任务模块
使用VU插件实现鼠标操作
"""

import logging
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧鼠标点击"
TASK_NAME = "无忧鼠标点击"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "coordinate_x": {
            "label": "X坐标",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "点击位置的X坐标"
        },
        "coordinate_y": {
            "label": "Y坐标",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "点击位置的Y坐标"
        },
        "coordinate_selector_tool": {
            "label": "坐标获取工具",
            "type": "button",
            "button_text": "点击获取坐标",
            "tooltip": "点击后可以在目标窗口中选择坐标位置",
            "widget_hint": "coordinate_selector"
        },
        "action_type": {
            "label": "操作类型",
            "type": "select",
            "options": ["移动并点击", "仅移动", "仅点击", "按下", "释放", "滚轮"],
            "default": "移动并点击",
            "tooltip": "选择鼠标操作类型"
        },
        "move_mode": {
            "label": "移动方式",
            "type": "select",
            "options": ["绝对移动(MoveTo)", "相对移动(MoveR)", "扩展移动(MoveToEx)"],
            "default": "绝对移动(MoveTo)",
            "tooltip": "选择鼠标移动方式",
            "condition": {"param": "action_type", "value": ["移动并点击", "仅移动"]}
        },
        "move_width": {
            "label": "移动宽度",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "MoveToEx的宽度参数",
            "condition": {"param": "move_mode", "value": "扩展移动(MoveToEx)"}
        },
        "move_height": {
            "label": "移动高度",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "MoveToEx的高度参数",
            "condition": {"param": "move_mode", "value": "扩展移动(MoveToEx)"}
        },
        "button_action": {
            "label": "按钮操作",
            "type": "select",
            "options": ["单击", "双击", "按下", "释放"],
            "default": "单击",
            "tooltip": "选择按钮操作方式",
            "condition": {"param": "action_type", "value": ["移动并点击", "仅点击", "按下", "释放"]}
        },
        "button": {
            "label": "鼠标按钮",
            "type": "select",
            "options": ["左键", "右键", "中键"],
            "default": "左键",
            "tooltip": "选择要操作的鼠标按钮",
            "condition": {"param": "action_type", "value": ["移动并点击", "仅点击", "按下", "释放"]}
        },
        "wheel_direction": {
            "label": "滚轮方向",
            "type": "select",
            "options": ["向上", "向下"],
            "default": "向下",
            "tooltip": "选择滚轮滚动方向",
            "condition": {"param": "action_type", "value": "滚轮"}
        },
        "wheel_count": {
            "label": "滚动次数",
            "type": "int",
            "default": 1,
            "min": 1,
            "max": 10,
            "tooltip": "滚轮滚动次数",
            "condition": {"param": "action_type", "value": "滚轮"}
        },
        "enable_real_mouse": {
            "label": "启用真实鼠标",
            "type": "bool",
            "default": False,
            "tooltip": "启用真实鼠标模式（更接近人工操作）"
        },
        "mouse_delay": {
            "label": "鼠标延迟(ms)",
            "type": "int",
            "default": 10,
            "min": 0,
            "max": 1000,
            "tooltip": "真实鼠标模式下的延迟时间",
            "condition": {"param": "enable_real_mouse", "value": True}
        },
        "mouse_step": {
            "label": "鼠标步长",
            "type": "int",
            "default": 5,
            "min": 1,
            "max": 50,
            "tooltip": "真实鼠标模式下的移动步长",
            "condition": {"param": "enable_real_mouse", "value": True}
        },
        "---next_step_delay---": {"type": "separator", "label": "下一步延迟执行"},
        "enable_next_step_delay": {
            "label": "启用下一步延迟执行",
            "type": "bool",
            "default": False,
            "tooltip": "勾选后，执行完当前操作会等待指定时间再执行下一步"
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
            "tooltip": "点击成功后的操作"
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
            "tooltip": "点击失败后的操作"
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

def _perform_mouse_move(vu, move_mode: str, x: int, y: int, width: int = 0, height: int = 0) -> bool:
    """执行鼠标移动操作"""
    if move_mode == '绝对移动(MoveTo)':
        return vu.vu.MoveTo(x, y) > 0
    elif move_mode == '相对移动(MoveR)':
        return vu.vu.MoveR(x, y) > 0
    elif move_mode == '扩展移动(MoveToEx)':
        return vu.vu.MoveToEx(x, y, width, height) > 0
    return False


def _perform_button_action(vu, button_action: str, button: str) -> bool:
    """执行鼠标按钮操作"""
    button_methods = {
        '单击': {'左键': 'LeftClick', '右键': 'RightClick', '中键': 'MiddleClick'},
        '按下': {'左键': 'LeftDown', '右键': 'RightDown', '中键': 'MiddleDown'},
        '释放': {'左键': 'LeftUp', '右键': 'RightUp', '中键': 'MiddleUp'},
        '双击': {'左键': 'LeftDoubleClick'}
    }
    
    if button_action == '双击':
        return vu.vu.LeftDoubleClick() > 0
    
    if button_action in button_methods and button in button_methods[button_action]:
        method_name = button_methods[button_action][button]
        return getattr(vu.vu, method_name)() > 0
    
    return False


def execute_task(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
                target_hwnd: Optional[int], window_region: Optional[tuple], card_id: Optional[int],
                get_image_data=None, **kwargs) -> Tuple[bool, str, Optional[int]]:
    """执行无忧鼠标点击任务"""
    return execute(params, counters, execution_mode, target_hwnd, card_id, kwargs.get('stop_checker'))


def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], card_id: Optional[int], stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧鼠标点击任务"""
    
    action_type = params.get('action_type', '移动并点击')
    enable_real_mouse = params.get('enable_real_mouse', False)
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    logger.info(f"开始执行无忧鼠标操作: 类型={action_type}, 按钮={params.get('button', '左键')}, 操作={params.get('button_action', '单击')}")
    
    try:
        from core.dual_mode_manager import get_dual_mode_manager
        manager = get_dual_mode_manager()
        vu = manager.vu_wrapper
        
        if not vu.is_initialized():
            logger.error("VU插件未初始化")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        if enable_real_mouse:
            vu.vu.EnableRealMouse(1, params.get('mouse_delay', 10), params.get('mouse_step', 5))
        
        success = True
        
        # 执行移动操作
        if action_type in ['移动并点击', '仅移动']:
            success = _perform_mouse_move(vu, params.get('move_mode', '绝对移动(MoveTo)'),
                                         params.get('coordinate_x', 0), params.get('coordinate_y', 0),
                                         params.get('move_width', 0), params.get('move_height', 0))
            if not success:
                logger.error("鼠标移动失败")
                if enable_real_mouse:
                    vu.vu.EnableRealMouse(0, 0, 0)
                return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        # 执行按钮操作
        if action_type in ['移动并点击', '仅点击', '按下', '释放']:
            success = _perform_button_action(vu, params.get('button_action', '单击'), params.get('button', '左键'))
            if not success:
                logger.error("鼠标按钮操作失败")
                if enable_real_mouse:
                    vu.vu.EnableRealMouse(0, 0, 0)
                return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        # 执行滚轮操作
        if action_type == '滚轮':
            wheel_method = vu.vu.WheelUp if params.get('wheel_direction', '向下') == '向上' else vu.vu.WheelDown
            for _ in range(params.get('wheel_count', 1)):
                if not wheel_method() > 0:
                    logger.error("滚轮操作失败")
                    if enable_real_mouse:
                        vu.vu.EnableRealMouse(0, 0, 0)
                    return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        if enable_real_mouse:
            vu.vu.EnableRealMouse(0, 0, 0)
        
        logger.info("无忧鼠标操作成功")
        
        if params.get('enable_next_step_delay', False):
            _handle_next_step_delay(params, stop_checker)
        
        return _handle_success(on_success_action, success_jump_id, card_id)
        
    except Exception as e:
        logger.error(f"执行无忧鼠标操作时发生异常: {e}", exc_info=True)
        if enable_real_mouse:
            try:
                vu.vu.EnableRealMouse(0, 0, 0)
            except Exception:
                pass
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