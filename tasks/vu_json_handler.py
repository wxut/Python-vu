# -*- coding: utf-8 -*-
"""
VU JSON处理任务模块
提供JSON读写和数据处理功能
"""

import logging
from typing import Dict, Any, Optional, Tuple
from core.vu_json import VUJson
from core.vu_wrapper import VUWrapper

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧JSON处理"
TASK_NAME = "无忧JSON处理"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "operation": {
            "label": "操作类型",
            "type": "select",
            "options": ["读取JSON", "写入JSON"],
            "default": "读取JSON",
            "tooltip": "选择JSON操作类型"
        },
        "json_str": {
            "label": "JSON字符串",
            "type": "text",
            "default": "",
            "tooltip": "要读取的JSON字符串",
            "condition": {"param": "operation", "value": "读取JSON"}
        },
        "keys": {
            "label": "读取的键",
            "type": "text",
            "default": "",
            "tooltip": "要读取的键名,多个用逗号分隔",
            "condition": {"param": "operation", "value": "读取JSON"}
        },
        "data": {
            "label": "数据",
            "type": "text",
            "default": "{}",
            "tooltip": "要写入的数据(JSON格式)",
            "condition": {"param": "operation", "value": "写入JSON"}
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
    """执行无忧JSON处理任务"""
    return execute(params, counters, execution_mode, target_hwnd, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], card_id: Optional[int], stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧JSON处理任务"""
    
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    try:
        json_handler = VUJsonHandler()
        
        # 处理keys参数
        if params.get('operation') == '读取JSON' and 'keys' in params:
            keys_str = params.get('keys', '')
            if keys_str:
                params['keys'] = [k.strip() for k in keys_str.split(',')]
            else:
                params['keys'] = []
        
        result = json_handler.execute(params)
        
        if result.get('success', False):
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧JSON处理时发生异常: {e}", exc_info=True)
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

class VUJsonHandler:
    """VU JSON处理任务执行器"""
    
    def __init__(self):
        """初始化JSON处理器"""
        self.vu_wrapper = VUWrapper()
        self.json_handler = VUJson(self.vu_wrapper)
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行JSON处理任务
        
        Args:
            params: 任务参数
                - operation: 操作类型 (read/write)
                - json_str: JSON字符串 (读取时)
                - data: 数据字典 (写入时)
                - keys: 要读取的键列表 (读取时)
                
        Returns:
            执行结果字典
        """
        operation = params.get('operation', 'read')
        
        try:
            if operation == 'read':
                return self._read_json(params)
            elif operation == 'write':
                return self._write_json(params)
            else:
                return {'success': False, 'error': f'未知操作: {operation}'}
        except Exception as e:
            logger.error(f"JSON处理失败: {e}")
            return {'success': False, 'error': str(e)}
    
    def _read_json(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """读取JSON数据"""
        json_str = params.get('json_str', '')
        keys = params.get('keys', [])
        
        if not json_str:
            return {'success': False, 'error': 'JSON字符串为空'}
        
        handle = self.json_handler.read_input(json_str)
        if handle <= 0:
            return {'success': False, 'error': 'JSON解析失败'}
        
        result_data = {}
        for key in keys:
            # 尝试获取字符串
            str_value = self.json_handler.read_get_str(handle, key)
            if str_value is not None:
                result_data[key] = str_value
                continue
            
            # 尝试获取数值
            num_value = self.json_handler.read_get_num(handle, key)
            if num_value is not None:
                result_data[key] = num_value
        
        self.json_handler.release_handle(handle)
        
        return {
            'success': True,
            'data': result_data
        }
    
    def _write_json(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """写入JSON数据"""
        data = params.get('data', {})
        
        if not data:
            return {'success': False, 'error': '数据为空'}
        
        handle = self.json_handler.write_create_obj()
        if handle <= 0:
            return {'success': False, 'error': '创建JSON对象失败'}
        
        for key, value in data.items():
            if isinstance(value, str):
                self.json_handler.write_add_str(handle, key, value)
            elif isinstance(value, (int, float)):
                self.json_handler.write_add_num(handle, key, value)
        
        json_str = self.json_handler.write_output(handle)
        self.json_handler.release_handle(handle)
        
        if json_str:
            return {
                'success': True,
                'json_str': json_str
            }
        else:
            return {'success': False, 'error': 'JSON输出失败'}


def create_task():
    """创建任务实例"""
    return VUJsonHandler()