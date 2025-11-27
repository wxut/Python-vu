# -*- coding: utf-8 -*-
"""
VU图像处理高级任务模块
提供图片加载、颜色获取、数据处理等功能
"""

import logging
from typing import Dict, Any, Optional, Tuple
from core.vu_image import VUImage
from core.vu_wrapper import VUWrapper

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧图像处理"
TASK_NAME = "无忧图像处理"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "operation": {
            "label": "操作类型",
            "type": "select",
            "options": ["加载图片", "释放图片", "获取图片尺寸", "获取像素颜色", "比较颜色", "获取屏幕数据", "获取屏幕BMP数据"],
            "default": "加载图片",
            "tooltip": "选择图像处理操作"
        },
        "pic_path": {
            "label": "图片路径",
            "type": "text",
            "default": "",
            "tooltip": "图片文件路径",
            "condition": {"param": "operation", "value": "加载图片"}
        },
        "handle": {
            "label": "图片句柄",
            "type": "int",
            "default": -1,
            "tooltip": "图片句柄ID",
            "condition": {"param": "operation", "value": ["释放图片", "获取图片尺寸"]}
        },
        "x": {
            "label": "X坐标",
            "type": "int",
            "default": 0,
            "tooltip": "X坐标位置",
            "condition": {"param": "operation", "value": ["获取像素颜色", "比较颜色"]}
        },
        "y": {
            "label": "Y坐标",
            "type": "int",
            "default": 0,
            "tooltip": "Y坐标位置",
            "condition": {"param": "operation", "value": ["获取像素颜色", "比较颜色"]}
        },
        "color": {
            "label": "颜色值",
            "type": "text",
            "default": "FFFFFF",
            "tooltip": "RGB颜色值(十六进制)",
            "condition": {"param": "operation", "value": "比较颜色"}
        },
        "threshold": {
            "label": "阈值",
            "type": "float",
            "default": 0.9,
            "min": 0.0,
            "max": 1.0,
            "step": 0.01,
            "decimals": 2,
            "tooltip": "颜色比较阈值",
            "condition": {"param": "operation", "value": "比较颜色"}
        },
        "x1": {
            "label": "左上X",
            "type": "int",
            "default": 0,
            "tooltip": "区域左上角X坐标",
            "condition": {"param": "operation", "value": ["获取屏幕数据", "获取屏幕BMP数据"]}
        },
        "y1": {
            "label": "左上Y",
            "type": "int",
            "default": 0,
            "tooltip": "区域左上角Y坐标",
            "condition": {"param": "operation", "value": ["获取屏幕数据", "获取屏幕BMP数据"]}
        },
        "x2": {
            "label": "右下X",
            "type": "int",
            "default": 100,
            "tooltip": "区域右下角X坐标",
            "condition": {"param": "operation", "value": ["获取屏幕数据", "获取屏幕BMP数据"]}
        },
        "y2": {
            "label": "右下Y",
            "type": "int",
            "default": 100,
            "tooltip": "区域右下角Y坐标",
            "condition": {"param": "operation", "value": ["获取屏幕数据", "获取屏幕BMP数据"]}
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
    """执行无忧图像处理任务"""
    return execute(params, counters, execution_mode, target_hwnd, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], card_id: Optional[int], stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧图像处理任务"""
    
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    try:
        image_advanced = VUImageAdvanced()
        result = image_advanced.execute(params)
        
        if result.get('success', False):
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧图像处理时发生异常: {e}", exc_info=True)
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

class VUImageAdvanced:
    """VU图像处理高级任务执行器"""
    
    def __init__(self):
        """初始化图像处理器"""
        self.vu_wrapper = VUWrapper()
        self.image = VUImage(self.vu_wrapper)
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行图像处理任务
        
        Args:
            params: 任务参数
                - operation: 操作类型
                - 其他参数根据操作类型而定
                
        Returns:
            执行结果字典
        """
        operation = params.get('operation', '')
        
        try:
            if operation == 'load_pic':
                pic_path = params.get('pic_path', '')
                handle = self.image.load_pic(pic_path)
                return {'success': handle > 0, 'handle': handle}
            
            elif operation == 'free_pic':
                handle = params.get('handle', -1)
                return {'success': self.image.free_pic(handle)}
            
            elif operation == 'get_pic_size':
                handle = params.get('handle', -1)
                size = self.image.get_pic_size(handle)
                return {'success': size is not None, 'size': size}
            
            elif operation == 'get_pixel_color':
                x = params.get('x', 0)
                y = params.get('y', 0)
                color = self.image.get_pixel_color(x, y)
                return {'success': bool(color), 'color': color}
            
            elif operation == 'cmp_color':
                x = params.get('x', 0)
                y = params.get('y', 0)
                color = params.get('color', '')
                threshold = params.get('threshold', 0.9)
                result = self.image.cmp_color(x, y, color, threshold)
                return {'success': True, 'match': result}
            
            elif operation == 'get_screen_data':
                x1 = params.get('x1', 0)
                y1 = params.get('y1', 0)
                x2 = params.get('x2', 0)
                y2 = params.get('y2', 0)
                data = self.image.get_screen_data(x1, y1, x2, y2)
                return {'success': data is not None, 'data': data}
            
            elif operation == 'get_screen_data_bmp':
                x1 = params.get('x1', 0)
                y1 = params.get('y1', 0)
                x2 = params.get('x2', 0)
                y2 = params.get('y2', 0)
                data = self.image.get_screen_data_bmp(x1, y1, x2, y2)
                return {'success': data is not None, 'data': data}
            
            else:
                return {'success': False, 'error': f'未知操作: {operation}'}
        
        except Exception as e:
            logger.error(f"图像处理失败: {e}")
            return {'success': False, 'error': str(e)}


def create_task():
    """创建任务实例"""
    return VUImageAdvanced()