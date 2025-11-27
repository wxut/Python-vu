# -*- coding: utf-8 -*-
"""
VU内存操作任务模块
提供内存读写、查找功能
"""

import logging
from typing import Dict, Any, Optional, Tuple
from core.vu_memory import VUMemory
from core.vu_wrapper import VUWrapper

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧内存操作"
TASK_NAME = "无忧内存操作"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "operation": {
            "label": "操作类型",
            "type": "select",
            "options": ["读取整数", "读取浮点数", "读取双精度", "读取字符串", "读取数据",
                       "写入整数", "写入浮点数", "写入双精度", "写入字符串", "写入数据",
                       "查找整数", "查找浮点数", "查找双精度", "查找字符串", "查找数据"],
            "default": "读取整数",
            "tooltip": "选择内存操作类型"
        },
        "address": {
            "label": "内存地址",
            "type": "text",
            "default": "0",
            "tooltip": "内存地址(十六进制或十进制)",
            "condition": {"param": "operation", "value": ["读取整数", "读取浮点数", "读取双精度", "读取字符串", "读取数据",
                                                          "写入整数", "写入浮点数", "写入双精度", "写入字符串", "写入数据"]}
        },
        "value": {
            "label": "数值",
            "type": "text",
            "default": "0",
            "tooltip": "要写入或查找的数值",
            "condition": {"param": "operation", "value": ["写入整数", "写入浮点数", "写入双精度", "写入字符串",
                                                          "查找整数", "查找浮点数", "查找双精度", "查找字符串"]}
        },
        "type_code": {
            "label": "类型码",
            "type": "int",
            "default": 0,
            "min": 0,
            "max": 7,
            "tooltip": "数据类型码(0-7)",
            "condition": {"param": "operation", "value": ["读取整数", "写入整数", "查找整数"]}
        },
        "length": {
            "label": "长度",
            "type": "int",
            "default": 0,
            "min": 0,
            "tooltip": "数据长度",
            "condition": {"param": "operation", "value": ["读取字符串", "读取数据"]}
        },
        "encoding": {
            "label": "编码",
            "type": "select",
            "options": ["utf-8", "gbk", "ascii"],
            "default": "utf-8",
            "tooltip": "字符串编码",
            "condition": {"param": "operation", "value": ["读取字符串", "写入字符串", "查找字符串"]}
        },
        "start": {
            "label": "起始地址",
            "type": "text",
            "default": "0",
            "tooltip": "查找起始地址",
            "condition": {"param": "operation", "value": ["查找整数", "查找浮点数", "查找双精度", "查找字符串", "查找数据"]}
        },
        "end": {
            "label": "结束地址",
            "type": "text",
            "default": "0",
            "tooltip": "查找结束地址",
            "condition": {"param": "operation", "value": ["查找整数", "查找浮点数", "查找双精度", "查找字符串", "查找数据"]}
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
    """执行无忧内存操作任务"""
    return execute(params, counters, execution_mode, target_hwnd, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], card_id: Optional[int], stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧内存操作任务"""
    
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    try:
        memory_ops = VUMemoryOps()
        
        # 转换地址参数
        if 'address' in params:
            addr_str = params['address']
            params['address'] = int(addr_str, 16) if addr_str.startswith('0x') else int(addr_str)
        
        if 'start' in params:
            start_str = params['start']
            params['start'] = int(start_str, 16) if start_str.startswith('0x') else int(start_str)
        
        if 'end' in params:
            end_str = params['end']
            params['end'] = int(end_str, 16) if end_str.startswith('0x') else int(end_str)
        
        result = memory_ops.execute(params)
        
        if result.get('success', False):
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧内存操作时发生异常: {e}", exc_info=True)
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

class VUMemoryOps:
    """VU内存操作任务执行器"""
    
    def __init__(self):
        """初始化内存操作器"""
        self.vu_wrapper = VUWrapper()
        self.memory = VUMemory(self.vu_wrapper)
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行内存操作任务
        
        Args:
            params: 任务参数
                - operation: 操作类型 (read_int/write_int/find_int等)
                - address: 内存地址
                - value: 要写入或查找的值
                - 其他参数根据操作类型而定
                
        Returns:
            执行结果字典
        """
        operation = params.get('operation', '')
        
        try:
            # 读取操作
            if operation == 'read_int':
                return self._read_int(params)
            elif operation == 'read_float':
                return self._read_float(params)
            elif operation == 'read_double':
                return self._read_double(params)
            elif operation == 'read_string':
                return self._read_string(params)
            elif operation == 'read_data':
                return self._read_data(params)
            
            # 写入操作
            elif operation == 'write_int':
                return self._write_int(params)
            elif operation == 'write_float':
                return self._write_float(params)
            elif operation == 'write_double':
                return self._write_double(params)
            elif operation == 'write_string':
                return self._write_string(params)
            elif operation == 'write_data':
                return self._write_data(params)
            
            # 查找操作
            elif operation == 'find_int':
                return self._find_int(params)
            elif operation == 'find_float':
                return self._find_float(params)
            elif operation == 'find_double':
                return self._find_double(params)
            elif operation == 'find_string':
                return self._find_string(params)
            elif operation == 'find_data':
                return self._find_data(params)
            
            else:
                return {'success': False, 'error': f'未知操作: {operation}'}
        
        except Exception as e:
            logger.error(f"内存操作失败: {e}")
            return {'success': False, 'error': str(e)}
    
    # ==================== 读取操作实现 ====================
    
    def _read_int(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """读取整数"""
        address = params.get('address', 0)
        type_code = params.get('type_code', 0)
        
        value = self.memory.read_int(address, type_code)
        return {
            'success': value is not None,
            'value': value,
            'address': hex(address)
        }
    
    def _read_float(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """读取浮点数"""
        address = params.get('address', 0)
        
        value = self.memory.read_float(address)
        return {
            'success': value is not None,
            'value': value,
            'address': hex(address)
        }
    
    def _read_double(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """读取双精度"""
        address = params.get('address', 0)
        
        value = self.memory.read_double(address)
        return {
            'success': value is not None,
            'value': value,
            'address': hex(address)
        }
    
    def _read_string(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """读取字符串"""
        address = params.get('address', 0)
        length = params.get('length', 0)
        encoding = params.get('encoding', 'utf-8')
        
        value = self.memory.read_string(address, length, encoding)
        return {
            'success': value is not None,
            'value': value,
            'address': hex(address)
        }
    
    def _read_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """读取原始数据"""
        address = params.get('address', 0)
        length = params.get('length', 0)
        
        data = self.memory.read_data(address, length)
        return {
            'success': data is not None,
            'data': data,
            'address': hex(address)
        }
    
    # ==================== 写入操作实现 ====================
    
    def _write_int(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """写入整数"""
        address = params.get('address', 0)
        value = params.get('value', 0)
        type_code = params.get('type_code', 0)
        
        success = self.memory.write_int(address, value, type_code)
        return {
            'success': success,
            'address': hex(address),
            'value': value
        }
    
    def _write_float(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """写入浮点数"""
        address = params.get('address', 0)
        value = params.get('value', 0.0)
        
        success = self.memory.write_float(address, value)
        return {
            'success': success,
            'address': hex(address),
            'value': value
        }
    
    def _write_double(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """写入双精度"""
        address = params.get('address', 0)
        value = params.get('value', 0.0)
        
        success = self.memory.write_double(address, value)
        return {
            'success': success,
            'address': hex(address),
            'value': value
        }
    
    def _write_string(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """写入字符串"""
        address = params.get('address', 0)
        value = params.get('value', '')
        encoding = params.get('encoding', 'utf-8')
        
        success = self.memory.write_string(address, value, encoding)
        return {
            'success': success,
            'address': hex(address),
            'value': value
        }
    
    def _write_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """写入原始数据"""
        address = params.get('address', 0)
        data = params.get('data', b'')
        
        success = self.memory.write_data(address, data)
        return {
            'success': success,
            'address': hex(address),
            'length': len(data)
        }
    
    # ==================== 查找操作实现 ====================
    
    def _find_int(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """查找整数"""
        start = params.get('start', 0)
        end = params.get('end', 0)
        value = params.get('value', 0)
        type_code = params.get('type_code', 0)
        
        addresses = self.memory.find_int(start, end, value, type_code)
        return {
            'success': True,
            'count': len(addresses),
            'addresses': [hex(addr) for addr in addresses]
        }
    
    def _find_float(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """查找浮点数"""
        start = params.get('start', 0)
        end = params.get('end', 0)
        value = params.get('value', 0.0)
        
        addresses = self.memory.find_float(start, end, value)
        return {
            'success': True,
            'count': len(addresses),
            'addresses': [hex(addr) for addr in addresses]
        }
    
    def _find_double(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """查找双精度"""
        start = params.get('start', 0)
        end = params.get('end', 0)
        value = params.get('value', 0.0)
        
        addresses = self.memory.find_double(start, end, value)
        return {
            'success': True,
            'count': len(addresses),
            'addresses': [hex(addr) for addr in addresses]
        }
    
    def _find_string(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """查找字符串"""
        start = params.get('start', 0)
        end = params.get('end', 0)
        value = params.get('value', '')
        encoding = params.get('encoding', 'utf-8')
        
        addresses = self.memory.find_string(start, end, value, encoding)
        return {
            'success': True,
            'count': len(addresses),
            'addresses': [hex(addr) for addr in addresses]
        }
    
    def _find_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """查找原始数据"""
        start = params.get('start', 0)
        end = params.get('end', 0)
        data = params.get('data', b'')
        
        addresses = self.memory.find_data(start, end, data)
        return {
            'success': True,
            'count': len(addresses),
            'addresses': [hex(addr) for addr in addresses]
        }


def create_task():
    """创建任务实例"""
    return VUMemoryOps()