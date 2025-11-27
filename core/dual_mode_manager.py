# -*- coding: utf-8 -*-
"""
双模式管理器 - 统一管理VU插件和Python实现的切换
"""

import logging
from typing import Optional, Literal

logger = logging.getLogger(__name__)

# 模式类型
ModeType = Literal["vu", "python", "auto"]


class DualModeManager:
    """双模式管理器 - 管理VU插件和Python实现的切换"""
    
    def __init__(self):
        self.current_mode: ModeType = "auto"  # 默认自动模式
        self.vu_available = False
        self.vu_wrapper = None
        
        # 适配器实例
        self.input_adapter = None
        self.image_adapter = None
        self.ocr_adapter = None
        self.screenshot_adapter = None
        self.coordinate_adapter = None
        
    def initialize(self, vu_wrapper) -> bool:
        """
        初始化双模式管理器
        
        Args:
            vu_wrapper: VUWrapper实例
            
        Returns:
            bool: 初始化是否成功
        """
        try:
            self.vu_wrapper = vu_wrapper
            self.vu_available = vu_wrapper.is_initialized()
            
            if self.vu_available:
                # 初始化所有适配器
                from adapters.vu_input_adapter import VUInputAdapter
                from adapters.vu_image_adapter import VUImageAdapter
                from adapters.vu_ocr_adapter import VUOCRAdapter
                from adapters.vu_screenshot_adapter import VUScreenshotAdapter
                from adapters.vu_coordinate_adapter import VUCoordinateAdapter
                
                self.input_adapter = VUInputAdapter(vu_wrapper)
                self.image_adapter = VUImageAdapter(vu_wrapper)
                self.ocr_adapter = VUOCRAdapter(vu_wrapper)
                self.screenshot_adapter = VUScreenshotAdapter(vu_wrapper)
                self.coordinate_adapter = VUCoordinateAdapter(vu_wrapper)
                
                logger.info("✅ 双模式管理器初始化成功 (VU插件可用)")
                return True
            else:
                logger.warning("⚠️ VU插件不可用，仅支持Python模式")
                return False
                
        except Exception as e:
            logger.error(f"❌ 双模式管理器初始化失败: {e}")
            self.vu_available = False
            return False
    
    def set_mode(self, mode: ModeType) -> None:
        """
        设置当前模式
        
        Args:
            mode: 模式类型 ("vu", "python", "auto")
        """
        if mode not in ["vu", "python", "auto"]:
            logger.warning(f"无效的模式: {mode}，保持当前模式: {self.current_mode}")
            return
            
        if mode == "vu" and not self.vu_available:
            logger.warning("VU插件不可用，无法切换到VU模式，保持当前模式")
            return
            
        self.current_mode = mode
        logger.info(f"✅ 模式已切换到: {mode}")
    
    def get_mode(self) -> ModeType:
        """获取当前模式"""
        return self.current_mode
    
    def should_use_vu(self) -> bool:
        """
        判断是否应该使用VU插件
        
        Returns:
            bool: 是否使用VU插件
        """
        if self.current_mode == "vu":
            return self.vu_available
        elif self.current_mode == "python":
            return False
        else:  # auto模式
            return self.vu_available
    
    def get_input_adapter(self):
        """获取输入适配器"""
        return self.input_adapter if self.should_use_vu() else None
    
    def get_image_adapter(self):
        """获取图像适配器"""
        return self.image_adapter if self.should_use_vu() else None
    
    def get_ocr_adapter(self):
        """获取OCR适配器"""
        return self.ocr_adapter if self.should_use_vu() else None
    
    def get_screenshot_adapter(self):
        """获取截图适配器"""
        return self.screenshot_adapter if self.should_use_vu() else None
    
    def get_coordinate_adapter(self):
        """获取坐标适配器"""
        return self.coordinate_adapter if self.should_use_vu() else None


# 全局双模式管理器实例
_dual_mode_manager: Optional[DualModeManager] = None


def get_dual_mode_manager() -> DualModeManager:
    """获取全局双模式管理器实例"""
    global _dual_mode_manager
    if _dual_mode_manager is None:
        _dual_mode_manager = DualModeManager()
    return _dual_mode_manager


def initialize_dual_mode(vu_wrapper) -> bool:
    """
    初始化双模式系统
    
    Args:
        vu_wrapper: VUWrapper实例
        
    Returns:
        bool: 初始化是否成功
    """
    manager = get_dual_mode_manager()
    return manager.initialize(vu_wrapper)


def set_execution_mode(mode: ModeType) -> None:
    """
    设置执行模式
    
    Args:
        mode: 模式类型 ("vu", "python", "auto")
    """
    manager = get_dual_mode_manager()
    manager.set_mode(mode)


def get_execution_mode() -> ModeType:
    """获取当前执行模式"""
    manager = get_dual_mode_manager()
    return manager.get_mode()


# 导出
__all__ = [
    'DualModeManager',
    'ModeType',
    'get_dual_mode_manager',
    'initialize_dual_mode',
    'set_execution_mode',
    'get_execution_mode'
]