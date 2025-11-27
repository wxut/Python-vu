# -*- coding: utf-8 -*-
"""
VU插件核心包装器

提供VU插件的统一初始化、清理和基础功能
"""

import sys
import os
import ctypes
import logging
from typing import Optional, Tuple

logger = logging.getLogger(__name__)

# 简化导入逻辑
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

try:
    from vusoft import vusoft
except ImportError as e:
    raise ImportError(f"无法导入vusoft库，请确保vusoft.py在项目根目录: {e}")


# 全局VUWrapper实例
_global_vu_wrapper: Optional['VUWrapper'] = None


def get_vu_wrapper() -> Optional['VUWrapper']:
    """获取全局VUWrapper实例"""
    return _global_vu_wrapper


def set_vu_wrapper(wrapper: 'VUWrapper') -> None:
    """设置全局VUWrapper实例"""
    global _global_vu_wrapper
    _global_vu_wrapper = wrapper


class VUWrapper:
    """VU插件统一包装器

    提供VU插件的核心功能：
    - 初始化和清理
    - 窗口绑定
    - 版本信息
    - 错误处理
    """

    def __init__(self, dll_path: str = 'vux64.dll'):
        """初始化VU包装器

        Args:
            dll_path: VU插件DLL路径，默认为'vux64.dll'
        """
        self.dll_path = dll_path
        self.vu: Optional[vusoft] = None
        self.obj: Optional[int] = None
        self.hwnd: int = 0  # 当前绑定的窗口句柄
        self.bind_mode: str = "normal"  # 绑定模式
        self.initialized: bool = False

    def initialize(self) -> int:
        """初始化VU插件

        Returns:
            int: 对象句柄，失败返回0

        Example:
            wrapper = VUWrapper()
            obj = wrapper.initialize()
            if obj:
                print("初始化成功")
        """
        if self.initialized and self.obj:
            logger.info("VU插件已初始化")
            return self.obj

        try:
            self.vu = vusoft(self.dll_path)
            self.obj = self.vu.Create()

            if self.obj:
                self.initialized = True
                version = self.vu.Ver()
                logger.info(f"VU插件初始化成功 (对象句柄: {self.obj}, 版本: {version})")
                return self.obj
            
            logger.error("VU插件初始化失败: Create()返回0")
            return 0

        except Exception as e:
            logger.error(f"VU插件初始化异常: {e}", exc_info=True)
            return 0

    def cleanup(self) -> bool:
        """清理VU插件资源

        Returns:
            bool: 成功返回True

        Example:
            wrapper.cleanup()
        """
        if not self.initialized:
            return True

        try:
            if self.hwnd:
                self.unbind_window()

            if self.vu and self.obj:
                self.vu.Delete()
                logger.info("VU插件资源已清理")

            self.obj = None
            self.vu = None
            self.initialized = False
            return True

        except Exception as e:
            logger.error(f"VU插件清理异常: {e}")
            return False

    def is_initialized(self) -> bool:
        """检查是否已初始化

        Returns:
            bool: 已初始化返回True
        """
        return self.initialized and self.obj is not None

    def bind_window(self, hwnd: int, mode: str = "normal") -> bool:
        """绑定窗口（简单模式，向后兼容）

        Args:
            hwnd: 窗口句柄
            mode: 绑定模式，支持：
                  - "normal": 普通模式（前台）
                  - "gdi": GDI模式
                  - "gdi2": GDI2模式
                  - "dx": DirectX模式
                  - "dx2": DirectX2模式

        Returns:
            bool: 成功返回True

        Example:
            hwnd = win32gui.FindWindow(None, "窗口标题")
            if wrapper.bind_window(hwnd, "normal"):
                print("绑定成功")
        """
        if not self.is_initialized():
            logger.warning("VU插件未初始化，无法绑定窗口")
            return False

        try:
            ret = self.vu.BindWindow(hwnd, mode)
            if ret:
                self.hwnd = hwnd
                self.bind_mode = mode
                logger.info(f"绑定窗口成功 (hwnd: {hwnd}, mode: {mode})")
                return True
            else:
                logger.error(f"绑定窗口失败 (hwnd: {hwnd}, mode: {mode})")
                return False

        except Exception as e:
            logger.error(f"绑定窗口异常: {e}")
            return False

    def bind_window_ex(self, hwnd: int, display: str = "normal", mouse: str = "normal",
                       keypad: str = "normal", public: str = "", mode: int = 0) -> int:
        """绑定窗口（高级模式，支持完整参数）

        Args:
            hwnd: 窗口句柄
            display: 屏幕颜色获取方式
                    - "normal": 正常模式（前台截屏）
                    - "gdi": GDI模式
                    - "dx": DirectX模式
            mouse: 鼠标仿真模式
                   - "normal": 正常模式（前台鼠标）
                   - "windows": Windows消息模式
                   - "dx.state|dx.raw|dx.input|dx.position|dx.focus": DX模式组合
            keypad: 键盘仿真模式
                    - "normal": 正常模式（前台键盘）
                    - "windows": Windows消息模式
                    - "dx.state|dx.raw|dx.input": DX模式组合
            public: 公共属性
                    - "public.hide.dll": 隐藏VU插件
                    - "public.memory.drv": 内核方式执行内存操作
                    - 多个属性用"|"连接
            mode: 绑定模式
                  - 0: 推荐模式（后台效果最好）
                  - 1: 驱动级后台键鼠
                  - 2: VT模式后台键鼠（仅Intel处理器）

        Returns:
            int: 0-失败, 1-成功, 2-伪绑定成功

        Example:
            # 前台模式
            ret = wrapper.bind_window_ex(hwnd, "normal", "normal", "normal", "", 0)
            
            # 后台模式
            ret = wrapper.bind_window_ex(hwnd, "dx", "dx.state|dx.raw|dx.input", "dx.state|dx.raw|dx.input", "", 0)
            
            # 驱动级后台（隐藏DLL + 内存驱动）
            ret = wrapper.bind_window_ex(hwnd, "dx", "dx.state|dx.raw|dx.input|dx.position|dx.focus",
                                        "dx.state|dx.raw|dx.input", "public.hide.dll|public.memory.drv", 1)
        """
        if not self.is_initialized():
            logger.warning("VU插件未初始化，无法绑定窗口")
            return 0

        try:
            ret = self.vu.BindWindowEx(hwnd, display, mouse, keypad, public, mode)
            
            if ret == 1:
                self.hwnd = hwnd
                self.bind_mode = f"ex(display={display},mouse={mouse},keypad={keypad},mode={mode})"
                logger.info(f"绑定窗口成功 (hwnd: {hwnd})")
                logger.debug(f"  display: {display}")
                logger.debug(f"  mouse: {mouse}")
                logger.debug(f"  keypad: {keypad}")
                logger.debug(f"  public: {public}")
                logger.debug(f"  mode: {mode}")
                return 1
            elif ret == 2:
                self.hwnd = hwnd
                self.bind_mode = f"ex_pseudo(display={display},mouse={mouse},keypad={keypad},mode={mode})"
                logger.warning(f"伪绑定窗口成功 (hwnd: {hwnd})")
                logger.warning("  注意: 实际绑定参数可能与设置不同")
                return 2
            else:
                logger.error(f"绑定窗口失败 (hwnd: {hwnd})")
                # 获取错误信息
                try:
                    error_code = self.vu.GetLastError()
                    logger.error(f"  错误码: {error_code}")
                except Exception:
                    pass
                return 0

        except Exception as e:
            logger.error(f"绑定窗口异常: {e}", exc_info=True)
            return 0

    def unbind_window(self) -> bool:
        """解除窗口绑定

        Returns:
            bool: 成功返回True

        Example:
            wrapper.unbind_window()
        """
        if not self.is_initialized():
            return True

        try:
            if self.hwnd:
                ret = self.vu.UnBindWindow()
                if ret:
                    logger.info(f"解除窗口绑定 (hwnd: {self.hwnd})")
                    self.hwnd = 0
                    self.bind_mode = "normal"
                    return True
            return True

        except Exception as e:
            logger.error(f"解除绑定异常: {e}")
            return False

    def get_bound_window(self) -> Tuple[int, str]:
        """获取当前绑定的窗口

        Returns:
            tuple: (hwnd, mode)
        """
        return (self.hwnd, self.bind_mode)

    def get_version(self) -> str:
        """获取VU插件版本

        Returns:
            str: 版本号
        """
        if not self.is_initialized() or not self.vu:
            return ""

        try:
            return self.vu.Ver()
        except Exception as e:
            logger.error(f"获取版本失败: {e}")
            return ""

    def get_screen_size(self) -> Tuple[int, int]:
        """获取屏幕大小

        Returns:
            tuple: (width, height)
        """
        if not self.is_initialized() or not self.vu:
            return (0, 0)

        try:
            width = self.vu.GetScreenWidth()
            height = self.vu.GetScreenHeight()
            return (width, height)
        except Exception as e:
            logger.error(f"获取屏幕大小失败: {e}")
            return (0, 0)

    def delay(self, milliseconds: int) -> None:
        """延迟

        Args:
            milliseconds: 延迟毫秒数

        Example:
            wrapper.delay(1000)  # 延迟1秒
        """
        if self.is_initialized() and self.vu:
            try:
                self.vu.Delay(milliseconds)
            except Exception as e:
                logger.error(f"延迟失败: {e}")

    def __enter__(self):
        """支持with语句"""
        self.initialize()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """支持with语句"""
        self.cleanup()
        return False

    def __del__(self):
        """析构函数，确保资源清理"""
        self.cleanup()


# 使用示例
if __name__ == "__main__":
    # 基础使用
    wrapper = VUWrapper()

    if wrapper.initialize():
        logger.info("初始化成功")

        # 获取版本
        version = wrapper.get_version()
        logger.info(f"版本: {version}")

        # 获取屏幕大小
        width, height = wrapper.get_screen_size()
        logger.info(f"屏幕: {width}x{height}")

        # 清理
        wrapper.cleanup()

    logger.info("\n使用with语句:")
    # 使用with语句（推荐）
    with VUWrapper() as vu:
        logger.info(f"版本: {vu.get_version()}")
        logger.info(f"屏幕: {vu.get_screen_size()}")
