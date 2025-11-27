# -*- coding: utf-8 -*-
"""
VU AI功能核心模块
提供YOLO检测、语音识别等AI功能
"""

import logging
from typing import Optional, List, Dict, Any
from core.vu_wrapper import VUWrapper

logger = logging.getLogger(__name__)


class VUAi:
    """VU AI功能核心类"""
    
    def __init__(self, vu_wrapper: VUWrapper):
        """
        初始化AI功能
        
        Args:
            vu_wrapper: VU核心包装器实例
        """
        self.vu = vu_wrapper
        self._yolo_model = None
        self._snd_model = None
    
    # ==================== YOLO检测 ====================
    
    def yolo_set_model(self, model_path: str) -> bool:
        """
        设置YOLO模型
        
        Args:
            model_path: 模型文件路径
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("AiYoloSetModel", model_path)
            if result == 1:
                self._yolo_model = model_path
                logger.info(f"YOLO模型设置成功: {model_path}")
            return result == 1
        except Exception as e:
            logger.error(f"设置YOLO模型失败: {e}")
            return False
    
    def yolo_detect_objects(self, image_path: str, confidence: float = 0.5) -> List[Dict[str, Any]]:
        """
        YOLO目标检测
        
        Args:
            image_path: 图片路径
            confidence: 置信度阈值 (0.0-1.0)
            
        Returns:
            检测结果列表,每个元素包含: {class, confidence, x, y, width, height}
        """
        try:
            result = self.vu.call_api("AiYoloDetectObjects", image_path, confidence)
            if result:
                objects = []
                for item in result.split('|'):
                    if ',' in item:
                        parts = item.split(',')
                        if len(parts) >= 6:
                            objects.append({
                                'class': parts[0],
                                'confidence': float(parts[1]),
                                'x': int(parts[2]),
                                'y': int(parts[3]),
                                'width': int(parts[4]),
                                'height': int(parts[5])
                            })
                return objects
            return []
        except Exception as e:
            logger.error(f"YOLO检测失败: {e}")
            return []
    
    # ==================== 语音识别 ====================
    
    def snd_set_model(self, model_path: str) -> bool:
        """
        设置语音模型
        
        Args:
            model_path: 模型文件路径
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("SndSetModel", model_path)
            if result == 1:
                self._snd_model = model_path
                logger.info(f"语音模型设置成功: {model_path}")
            return result == 1
        except Exception as e:
            logger.error(f"设置语音模型失败: {e}")
            return False
    
    def snd_asr(self, audio_path: str) -> Optional[str]:
        """
        语音识别(ASR)
        
        Args:
            audio_path: 音频文件路径
            
        Returns:
            识别的文本,失败返回None
        """
        try:
            text = self.vu.call_api("SndAsr", audio_path)
            return text if text else None
        except Exception as e:
            logger.error(f"语音识别失败: {e}")
            return None
    
    def snd_tts(self, text: str, output_path: str) -> bool:
        """
        语音合成(TTS)
        
        Args:
            text: 要合成的文本
            output_path: 输出音频文件路径
            
        Returns:
            成功返回True
        """
        try:
            result = self.vu.call_api("SndTts", text, output_path)
            return result == 1
        except Exception as e:
            logger.error(f"语音合成失败: {e}")
            return False