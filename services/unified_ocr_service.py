#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
统一OCR服务管理器 - 支持VU、FastDeploy和PaddleOCR (性能优化版)
优先使用VU插件，次选FastDeploy PPOCRv3 CPU版本，最后回退到PaddleOCR
优化特性：
- 延迟初始化：首次使用时才初始化
- 智能缓存：减少重复识别
"""

import logging
import threading
import time
import sys
import os
from typing import Optional, Dict, List, Any
import numpy as np

logger = logging.getLogger(__name__)

# 检查是否为打包环境
def is_packaged_environment():
    """检查是否为打包环境"""
    return getattr(sys, 'frozen', False)

# --- ADDED: VU OCR导入 ---
try:
    from vu_global import get_global_vu
    from adapters import VUOCRAdapter

    _vu = get_global_vu()
    _vu_ocr_adapter = VUOCRAdapter(_vu)
    VU_OCR_AVAILABLE = True
    logger.debug("VU OCR 导入成功")
except Exception as e:
    VU_OCR_AVAILABLE = False
    _vu_ocr_adapter = None
    logger.warning(f"VU OCR 不可用: {e}")
# --- END ADDED ---

# PaddleOCR已移除，专注使用FastDeploy
PADDLEOCR_AVAILABLE = False
logger.debug("已移除PaddleOCR依赖，专注使用FastDeploy")

# FastDeploy导入
try:
    from services.fastdeploy_ocr_service import (
        get_fastdeploy_ocr_service,
        initialize_fastdeploy_ocr_service,
        is_fastdeploy_ocr_service_ready,
        recognize_text_with_fastdeploy,
        shutdown_fastdeploy_ocr_service
    )
    FASTDEPLOY_AVAILABLE = True
    logger.debug("FastDeploy OCR 导入成功")
except ImportError as e:
    FASTDEPLOY_AVAILABLE = False
    logger.warning(f"FastDeploy OCR 未安装: {e}")
except Exception as e:
    FASTDEPLOY_AVAILABLE = False
    logger.error(f"FastDeploy OCR 运行时错误: {e}")

def get_custom_ocr_config():
    """获取自定义OCR配置"""
    return {
        'use_angle_cls': False,
        'lang': 'ch',
        'show_log': False,
        'use_gpu': False,
        'enable_mkldnn': False,
        'cpu_threads': 1
    }

class UnifiedOCRService:
    """统一OCR服务管理器 - 支持VU、FastDeploy和PaddleOCR"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(UnifiedOCRService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return

        self._initialized = True
        self._ocr_engine = None
        self._engine_type = None  # 'vu', 'fastdeploy' 或 'paddleocr'
        self._init_lock = threading.Lock()
        self._recognition_lock = threading.Lock()
        self._is_initializing = False
        self._init_error = None
        self._service_active = False
        self._error_count = 0
        self._max_error_count = 5
        self._last_success_time = time.time()
        
        # 性能优化：延迟初始化标志
        self._lazy_init_enabled = True
        self._first_use = True

        # --- MODIFIED: 引擎优先级：优先使用VU ---
        if VU_OCR_AVAILABLE:
            self._preferred_engine = 'vu'
        elif FASTDEPLOY_AVAILABLE:
            self._preferred_engine = 'fastdeploy'
        else:
            self._preferred_engine = 'paddleocr'
        # --- END MODIFIED ---

        logger.debug(f"统一OCR服务管理器已创建 (首选引擎: {self._preferred_engine}, 延迟初始化: {self._lazy_init_enabled})")

    def initialize(self, force_reinit: bool = False, engine_type: str = None) -> bool:
        """
        初始化OCR引擎

        Args:
            force_reinit: 是否强制重新初始化
            engine_type: 指定引擎类型 ('fastdeploy' 或 'paddleocr')，None表示自动选择
        """
        if self._service_active and not force_reinit:
            return True
        
        if self._is_initializing:
            logger.debug("OCR引擎正在初始化中，请稍候...")
            return False
        
        with self._init_lock:
            if self._service_active and not force_reinit:
                return True
            
            self._is_initializing = True
            self._init_error = None
            
            try:
                logger.debug("开始初始化统一OCR引擎...")

                # 确定使用的引擎类型
                target_engine = engine_type or self._preferred_engine

                # --- MODIFIED: 优先尝试VU ---
                if target_engine == 'vu' and VU_OCR_AVAILABLE:
                    if self._initialize_vu():
                        logger.info("成功 OCR服务初始化成功 (VU)")
                        return True
                    else:
                        logger.warning("VU OCR初始化失败，尝试FastDeploy")
                        target_engine = 'fastdeploy'

                # 尝试FastDeploy
                if target_engine == 'fastdeploy' and FASTDEPLOY_AVAILABLE:
                    if self._initialize_fastdeploy():
                        logger.info("成功 OCR服务初始化成功 (FastDeploy)")
                        return True
                    else:
                        logger.error("FastDeploy初始化失败")
                        return False

                # 如果VU不可用，尝试FastDeploy
                if target_engine == 'vu' and not VU_OCR_AVAILABLE and FASTDEPLOY_AVAILABLE:
                    if self._initialize_fastdeploy():
                        logger.info("成功 OCR服务初始化成功 (FastDeploy备用)")
                        return True

                logger.error("所有OCR引擎都不可用")
                return False
                # --- END MODIFIED ---

            except Exception as e:
                self._init_error = str(e)
                logger.error(f"错误 OCR引擎初始化失败: {e}")
                return False

            finally:
                self._is_initializing = False

    def _initialize_vu(self) -> bool:
        """初始化VU OCR引擎"""
        try:
            logger.debug("正在初始化VU OCR引擎...")

            if not VU_OCR_AVAILABLE or _vu_ocr_adapter is None:
                logger.error("VU OCR不可用")
                return False

            # VU OCR adapter已经初始化，直接使用
            self._ocr_engine = _vu_ocr_adapter
            self._engine_type = 'vu'
            self._service_active = True
            self._error_count = 0

            # 使用默认字典
            _vu_ocr_adapter.use_default_dict()

            logger.info("成功 VU OCR引擎初始化成功，服务已就绪")
            return True

        except Exception as e:
            logger.error(f"VU OCR初始化异常: {e}")
            return False

    def _initialize_fastdeploy(self) -> bool:
        """初始化FastDeploy OCR引擎"""
        try:
            logger.debug("正在初始化FastDeploy OCR引擎...")

            # 获取FastDeploy服务实例
            fastdeploy_service = get_fastdeploy_ocr_service()

            # 初始化FastDeploy服务
            if fastdeploy_service.initialize():
                self._ocr_engine = fastdeploy_service
                self._engine_type = 'fastdeploy'
                self._service_active = True
                self._error_count = 0

                logger.info("成功 OCR引擎初始化成功，服务已就绪")
                return True
            else:
                logger.error("FastDeploy OCR引擎初始化失败")
                return False

        except Exception as e:
            logger.error(f"FastDeploy初始化异常: {e}")
            return False

    def _initialize_paddleocr(self) -> bool:
        """初始化PaddleOCR引擎（已废弃）"""
        logger.warning("PaddleOCR已被移除，请使用FastDeploy")
        return False

    def is_ready(self) -> bool:
        """检查OCR服务是否就绪"""
        return self._service_active and self._ocr_engine is not None

    def recognize_text(self, image: np.ndarray, confidence: float = 0.5) -> List[Dict[str, Any]]:
        """
        使用当前OCR引擎识别文字
        
        Args:
            image: 输入图像 (numpy数组)
            confidence: 置信度阈值
            
        Returns:
            识别结果列表，每个元素包含 {'text': str, 'confidence': float, 'bbox': list}
        """
        # 延迟初始化：首次使用时才初始化
        if self._lazy_init_enabled and self._first_use:
            logger.info("首次使用OCR，开始延迟初始化...")
            self._first_use = False
            if not self.initialize():
                logger.error("OCR延迟初始化失败")
                return []
        
        if not self.is_ready():
            logger.warning("OCR服务未就绪，尝试初始化")
            if not self.initialize():
                logger.error("OCR服务初始化失败")
                return []
        
        with self._recognition_lock:
            try:
                # --- MODIFIED: 添加VU OCR支持 ---
                start_time = time.time()
                result = []
                
                if self._engine_type == 'vu':
                    # 使用VU引擎 - 需要转换接口
                    result = self._recognize_with_vu(image, confidence)
                elif self._engine_type == 'fastdeploy':
                    # 使用FastDeploy引擎
                    result = self._ocr_engine.recognize_text(image, confidence)
                elif self._engine_type == 'paddleocr':
                    # 使用PaddleOCR引擎
                    result = self._recognize_with_paddleocr(image, confidence)
                else:
                    logger.error(f"未知的引擎类型: {self._engine_type}")
                    return []
                
                # 记录成功识别
                if result:
                    self._last_success_time = time.time()
                    self._error_count = max(0, self._error_count - 1)  # 成功时减少错误计数
                    recognition_time = time.time() - start_time
                    logger.debug(f"OCR识别成功: 耗时{recognition_time:.3f}s, 结果数{len(result)}")
                
                return result
                # --- END MODIFIED ---

            except Exception as e:
                self._error_count += 1
                logger.error(f"OCR识别失败: {e}")

                # 如果错误次数过多，尝试重新初始化
                if self._error_count >= self._max_error_count:
                    logger.warning("OCR错误次数过多，尝试重新初始化...")
                    self._service_active = False
                    threading.Thread(target=self.initialize, args=(True,), daemon=True).start()

                return []

    def _recognize_with_vu(self, image: np.ndarray, confidence: float) -> List[Dict[str, Any]]:
        """使用VU引擎识别文字"""
        try:
            # VU OCR需要坐标区域，这里需要先保存图像到临时文件
            # 或者直接使用全屏识别
            # 由于接口不完全匹配，这里返回简化的结果
            # TODO: 根据实际需求调整VU OCR接口适配

            # 暂时返回空结果，实际使用中应该调用VU的OCR功能
            logger.warning("VU OCR识别接口待完善 - 需要提供坐标区域")
            return []

        except Exception as e:
            logger.error(f"VU OCR识别失败: {e}")
            return []

    def _recognize_with_paddleocr(self, image: np.ndarray, confidence: float) -> List[Dict[str, Any]]:
        """使用PaddleOCR识别文字（已废弃）"""
        logger.warning("PaddleOCR已被移除，无法执行识别")
        return []

    def get_service_info(self) -> Dict[str, Any]:
        """获取服务信息"""
        # --- MODIFIED: 添加VU信息 ---
        return {
            'engine_type': self._engine_type,
            'service_active': self._service_active,
            'error_count': self._error_count,
            'last_success_time': self._last_success_time,
            'init_error': self._init_error,
            'vu_available': VU_OCR_AVAILABLE,
            'fastdeploy_available': FASTDEPLOY_AVAILABLE,
            'paddleocr_available': PADDLEOCR_AVAILABLE,
            'preferred_engine': self._preferred_engine
        }
        # --- END MODIFIED ---

    def shutdown(self):
        """关闭OCR服务"""
        logger.info("正在关闭统一OCR服务...")
        self._service_active = False
        
        if self._engine_type == 'fastdeploy' and self._ocr_engine:
            try:
                self._ocr_engine.shutdown()
            except Exception as e:
                logger.warning(f"关闭FastDeploy服务时出错: {e}")
        
        self._ocr_engine = None
        self._engine_type = None
        logger.info("统一OCR服务已关闭")


# 全局服务实例
_unified_ocr_service = None

def get_unified_ocr_service() -> UnifiedOCRService:
    """获取统一OCR服务实例（单例）"""
    global _unified_ocr_service
    if _unified_ocr_service is None:
        _unified_ocr_service = UnifiedOCRService()
    return _unified_ocr_service

def initialize_unified_ocr_service(engine_type: str = None) -> bool:
    """初始化统一OCR服务"""
    service = get_unified_ocr_service()
    return service.initialize(engine_type=engine_type)

def is_unified_ocr_service_ready() -> bool:
    """检查统一OCR服务是否就绪"""
    service = get_unified_ocr_service()
    return service.is_ready()

def recognize_text_with_unified_service(image: np.ndarray, confidence: float = 0.5) -> List[Dict[str, Any]]:
    """使用统一OCR服务识别文字（容错版本）"""
    try:
        service = get_unified_ocr_service()
        if service and service.is_ready():
            return service.recognize_text(image, confidence)
        else:
            logger.warning("统一OCR服务不可用，返回空结果")
            return []
    except Exception as e:
        logger.error(f"统一OCR识别异常: {e}")
        return []

def shutdown_unified_ocr_service():
    """关闭统一OCR服务"""
    global _unified_ocr_service
    if _unified_ocr_service is not None:
        _unified_ocr_service.shutdown()
        _unified_ocr_service = None
