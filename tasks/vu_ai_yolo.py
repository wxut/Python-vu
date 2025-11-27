# -*- coding: utf-8 -*-
"""
VU AI YOLO检测任务模块
提供YOLO目标检测和语音处理功能
"""

import logging
from typing import Dict, Any, Optional, Tuple
from core.vu_ai import VUAi
from core.vu_wrapper import VUWrapper

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧AI YOLO"
TASK_NAME = "无忧AI YOLO"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "operation": {
            "label": "操作类型",
            "type": "select",
            "options": ["设置YOLO模型", "YOLO检测", "设置语音模型", "语音识别(ASR)", "语音合成(TTS)"],
            "default": "YOLO检测",
            "tooltip": "选择AI操作类型"
        },
        "model_path": {
            "label": "模型路径",
            "type": "text",
            "default": "",
            "tooltip": "AI模型文件路径",
            "condition": {"param": "operation", "value": ["设置YOLO模型", "设置语音模型"]}
        },
        "image_path": {
            "label": "图片路径",
            "type": "text",
            "default": "",
            "tooltip": "要检测的图片路径",
            "condition": {"param": "operation", "value": "YOLO检测"}
        },
        "confidence": {
            "label": "置信度",
            "type": "float",
            "default": 0.5,
            "min": 0.0,
            "max": 1.0,
            "step": 0.01,
            "decimals": 2,
            "tooltip": "检测置信度阈值",
            "condition": {"param": "operation", "value": "YOLO检测"}
        },
        "audio_path": {
            "label": "音频路径",
            "type": "text",
            "default": "",
            "tooltip": "音频文件路径",
            "condition": {"param": "operation", "value": "语音识别(ASR)"}
        },
        "text": {
            "label": "文本内容",
            "type": "text",
            "default": "",
            "tooltip": "要合成的文本",
            "condition": {"param": "operation", "value": "语音合成(TTS)"}
        },
        "output_path": {
            "label": "输出路径",
            "type": "text",
            "default": "",
            "tooltip": "输出文件路径",
            "condition": {"param": "operation", "value": "语音合成(TTS)"}
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
    """执行无忧AI YOLO任务"""
    return execute(params, counters, execution_mode, target_hwnd, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], card_id: Optional[int], stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧AI YOLO任务"""
    
    operation = params.get('operation', 'YOLO检测')
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    logger.info(f"开始执行无忧AI YOLO: 操作={operation}")
    
    try:
        ai_yolo = VUAiYolo()
        result = ai_yolo.execute(params)
        
        if result.get('success', False):
            logger.info(f"AI操作成功: {result}")
            
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            logger.error(f"AI操作失败: {result.get('error', '未知错误')}")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧AI YOLO时发生异常: {e}", exc_info=True)
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

class VUAiYolo:
    """VU AI YOLO任务执行器"""
    
    def __init__(self):
        """初始化AI功能"""
        self.vu_wrapper = VUWrapper()
        self.ai = VUAi(self.vu_wrapper)
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行AI任务
        
        Args:
            params: 任务参数
                - operation: 操作类型 (yolo_detect/snd_asr/snd_tts)
                - 其他参数根据操作类型而定
                
        Returns:
            执行结果字典
        """
        operation = params.get('operation', '')
        
        try:
            # YOLO检测
            if operation == 'yolo_set_model':
                model_path = params.get('model_path', '')
                success = self.ai.yolo_set_model(model_path)
                return {'success': success, 'model_path': model_path}
            
            elif operation == 'yolo_detect':
                image_path = params.get('image_path', '')
                confidence = params.get('confidence', 0.5)
                objects = self.ai.yolo_detect_objects(image_path, confidence)
                return {
                    'success': True,
                    'count': len(objects),
                    'objects': objects
                }
            
            # 语音识别
            elif operation == 'snd_set_model':
                model_path = params.get('model_path', '')
                success = self.ai.snd_set_model(model_path)
                return {'success': success, 'model_path': model_path}
            
            elif operation == 'snd_asr':
                audio_path = params.get('audio_path', '')
                text = self.ai.snd_asr(audio_path)
                return {
                    'success': text is not None,
                    'text': text
                }
            
            elif operation == 'snd_tts':
                text = params.get('text', '')
                output_path = params.get('output_path', '')
                success = self.ai.snd_tts(text, output_path)
                return {
                    'success': success,
                    'output_path': output_path
                }
            
            else:
                return {'success': False, 'error': f'未知操作: {operation}'}
        
        except Exception as e:
            logger.error(f"AI任务执行失败: {e}")
            return {'success': False, 'error': str(e)}


def create_task():
    """创建任务实例"""
    return VUAiYolo()