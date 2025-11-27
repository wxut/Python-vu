# -*- coding: utf-8 -*-
"""
VU截图适配器

提供TM兼容的截图接口,底层使用VU插件实现
核心原则: 接口与TM的screenshot_helper保持一致,内部调用VU的Capture函数
"""

import logging
from typing import Optional, Tuple

logger = logging.getLogger(__name__)

# 尝试导入numpy
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    logger.warning("numpy不可用,部分功能受限")


class VUScreenshotAdapter:
    """VU截图适配器 - 提供TM兼容的截图接口"""

    def __init__(self, vu_wrapper):
        """
        初始化截图适配器

        Args:
            vu_wrapper: VUWrapper实例
        """
        self.vu_wrapper = vu_wrapper

        # 导入VU图像操作类(截图功能)
        from core.vu_image import VUImage
        self.vu_image = VUImage(vu_wrapper)

        logger.info("VU截图适配器初始化")

    def take_screenshot(self, region: Optional[Tuple[int, int, int, int]] = None) -> Optional[object]:
        """
        截图功能(TM兼容接口)

        与TM的take_screenshot接口保持一致
        返回PIL.Image对象

        Args:
            region: 截图区域 (x1, y1, x2, y2),None表示全屏

        Returns:
            Optional[PIL.Image]: 截图图像,失败返回None

        Example:
            # 全屏截图
            img = adapter.take_screenshot()
            # 区域截图
            img = adapter.take_screenshot(region=(0, 0, 800, 600))
        """
        try:
            import tempfile
            import os
            from PIL import Image

            # 创建临时文件
            temp_file = tempfile.mktemp(suffix=".bmp")

            logger.debug(f"截图: 区域:{region}, 临时文件:{temp_file}")

            # 使用VU的Capture截图
            if region:
                x1, y1, x2, y2 = region
                result = self.vu_image.capture_to_file(x1, y1, x2, y2, temp_file)
            else:
                # 全屏截图 - 获取屏幕大小
                width, height = self.vu_wrapper.get_screen_size()
                result = self.vu_image.capture_to_file(0, 0, width, height, temp_file)

            if result and os.path.exists(temp_file):
                # 加载为PIL Image
                screenshot = Image.open(temp_file)
                # 转换为RGB模式(如果需要)
                if screenshot.mode != 'RGB':
                    screenshot = screenshot.convert('RGB')

                # 删除临时文件
                try:
                    os.remove(temp_file)
                except Exception:
                    pass

                logger.debug("截图成功")
                return screenshot
            else:
                logger.error("截图失败: VU Capture返回失败")
                return None

        except Exception as e:
            logger.error(f"截图失败: {e}")
            return None

    def take_screenshot_opencv(self, region: Optional[Tuple[int, int, int, int]] = None) -> Optional[object]:
        """
        截图并转换为OpenCV格式(TM兼容接口)

        与TM的take_screenshot_opencv接口保持一致
        返回OpenCV格式的numpy数组(BGR)

        Args:
            region: 截图区域 (x1, y1, x2, y2),None表示全屏

        Returns:
            Optional[np.ndarray]: OpenCV格式的图像(BGR),失败返回None

        Example:
            img_cv = adapter.take_screenshot_opencv(region=(100, 100, 500, 500))
            if img_cv is not None:
                # 可以直接用于OpenCV处理
                cv2.imwrite("screenshot.png", img_cv)
        """
        try:
            import cv2

            # 先获取PIL格式截图
            screenshot_pil = self.take_screenshot(region)
            if screenshot_pil is None:
                return None

            # 转换为OpenCV格式(BGR)
            screenshot_np = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)

            logger.debug("截图转换为OpenCV格式成功")
            return screenshot_np

        except Exception as e:
            logger.error(f"截图转换为OpenCV格式失败: {e}")
            return None

    def take_window_screenshot(self, hwnd: int, client_area_only: bool = True) -> Optional[object]:
        """
        截取窗口(TM兼容接口)

        Args:
            hwnd: 窗口句柄
            client_area_only: 是否只截取客户区

        Returns:
            Optional[PIL.Image]: 截图图像,失败返回None

        Example:
            img = adapter.take_window_screenshot(hwnd, client_area_only=True)
        """
        try:
            import ctypes
            from ctypes import wintypes
            from PIL import Image
            import tempfile
            import os

            user32 = ctypes.windll.user32

            # 获取窗口信息
            if client_area_only:
                # 客户区截图
                rect = wintypes.RECT()
                user32.GetClientRect(hwnd, ctypes.byref(rect))
                width = rect.right - rect.left
                height = rect.bottom - rect.top
                x1, y1, x2, y2 = 0, 0, width, height
            else:
                # 整个窗口截图
                rect = wintypes.RECT()
                user32.GetWindowRect(hwnd, ctypes.byref(rect))
                width = rect.right - rect.left
                height = rect.bottom - rect.top
                x1, y1, x2, y2 = 0, 0, width, height

            logger.debug(
                f"截取窗口: hwnd={hwnd}, 客户区={client_area_only}, "
                f"大小=({width}, {height})"
            )

            # 绑定窗口(如果还没绑定)
            if self.vu_wrapper.hwnd != hwnd:
                self.vu_wrapper.bind_window(hwnd)

            # 使用VU截图
            temp_file = tempfile.mktemp(suffix=".bmp")
            result = self.vu_image.capture_to_file(x1, y1, x2, y2, temp_file)

            if result and os.path.exists(temp_file):
                screenshot = Image.open(temp_file)
                if screenshot.mode != 'RGB':
                    screenshot = screenshot.convert('RGB')

                # 删除临时文件
                try:
                    os.remove(temp_file)
                except Exception:
                    pass

                logger.debug("窗口截图成功")
                return screenshot
            else:
                logger.error("窗口截图失败")
                return None

        except Exception as e:
            logger.error(f"窗口截图失败: {e}")
            return None

    def get_screen_size(self) -> Tuple[int, int]:
        """
        获取屏幕尺寸(TM兼容接口)

        Returns:
            Tuple[int, int]: (宽度, 高度)

        Example:
            width, height = adapter.get_screen_size()
            print(f"屏幕大小: {width}x{height}")
        """
        try:
            width, height = self.vu_wrapper.get_screen_size()
            logger.debug(f"屏幕大小: {width}x{height}")
            return width, height

        except Exception as e:
            logger.error(f"获取屏幕大小失败: {e}")
            # 返回默认值
            return 1920, 1080

    def save_screenshot(self, image, file_path: str) -> bool:
        """
        保存截图(TM兼容接口)

        Args:
            image: PIL.Image对象或numpy数组
            file_path: 保存路径

        Returns:
            bool: 成功返回True

        Example:
            img = adapter.take_screenshot()
            adapter.save_screenshot(img, "screenshot.png")
        """
        try:
            from PIL import Image

            if NUMPY_AVAILABLE:
                import cv2
                if isinstance(image, np.ndarray):
                    # OpenCV格式
                    cv2.imwrite(file_path, image)
                    logger.debug(f"保存截图(OpenCV): {file_path}")
                    return True

            if isinstance(image, Image.Image):
                # PIL格式
                image.save(file_path)
                logger.debug(f"保存截图(PIL): {file_path}")
                return True
            else:
                logger.error(f"不支持的图像类型: {type(image)}")
                return False

        except Exception as e:
            logger.error(f"保存截图失败: {e}")
            return False


# 导出类
__all__ = ['VUScreenshotAdapter']
