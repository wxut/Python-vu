#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
截图助手模块 - 使用VU插件进行截图 (性能优化版)
底层实现改为VU插件，保持接口完全兼容TM
优化特性：智能截图缓存
"""

import logging
import numpy as np

logger = logging.getLogger(__name__)

# 导入截图缓存
try:
    from utils.screenshot_cache import get_screenshot_cache
    CACHE_AVAILABLE = True
except ImportError:
    CACHE_AVAILABLE = False
    logger.warning("截图缓存模块不可用")

# --- MODIFIED: 使用VU适配器替代pyautogui ---
try:
    from vu_global import get_global_vu
    from adapters import VUScreenshotAdapter

    # 获取全局VU实例
    _vu = get_global_vu()
    _screenshot_adapter = VUScreenshotAdapter(_vu)
    VU_SCREENSHOT_AVAILABLE = True
    logger.debug("VU 截图功能可用")
except Exception as e:
    VU_SCREENSHOT_AVAILABLE = False
    _screenshot_adapter = None
    logger.warning(f"VU 截图不可用: {e}，截图功能将受限")

# pyautogui作为备用方案
try:
    import pyautogui
    PYAUTOGUI_SCREENSHOT_AVAILABLE = True
    logger.debug("pyautogui 截图功能可用（备用）")
except ImportError:
    PYAUTOGUI_SCREENSHOT_AVAILABLE = False
    logger.warning("pyautogui 不可用")

# 优先使用VU截图
SCREENSHOT_AVAILABLE = VU_SCREENSHOT_AVAILABLE or PYAUTOGUI_SCREENSHOT_AVAILABLE
# --- END MODIFIED ---

# 尝试导入其他截图相关库
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def get_screen_size():
    """获取屏幕尺寸"""
    # --- MODIFIED: 优先使用VU ---
    if VU_SCREENSHOT_AVAILABLE and _screenshot_adapter:
        try:
            return _screenshot_adapter.get_screen_size()
        except Exception as e:
            logger.error(f"VU获取屏幕尺寸失败: {e}")
    # --- END MODIFIED ---

    if PYAUTOGUI_SCREENSHOT_AVAILABLE:
        return pyautogui.size()
    else:
        # 备用方案：使用Windows API
        import ctypes
        screen_width = ctypes.windll.user32.GetSystemMetrics(0)
        screen_height = ctypes.windll.user32.GetSystemMetrics(1)
        return screen_width, screen_height

def take_screenshot(region=None):
    """
    截图功能 - 优先使用VU插件

    Args:
        region: 截图区域 (left, top, width, height)，None表示全屏

    Returns:
        PIL.Image: 截图图像，失败返回None
    """
    # --- MODIFIED: 优先使用VU截图 ---
    if VU_SCREENSHOT_AVAILABLE and _screenshot_adapter:
        try:
            if region:
                logger.debug(f"VU区域截图: {region}")
                screenshot = _screenshot_adapter.take_screenshot(region=region)
            else:
                logger.debug("VU全屏截图")
                screenshot = _screenshot_adapter.take_screenshot()

            if screenshot:
                return screenshot
            else:
                logger.warning("VU截图返回None，尝试使用备用方案")
        except Exception as e:
            logger.error(f"VU截图失败: {e}，尝试使用备用方案")
    # --- END MODIFIED ---

    # 备用方案：使用pyautogui
    if not PYAUTOGUI_SCREENSHOT_AVAILABLE:
        logger.error("VU和pyautogui都不可用，无法截图")
        return None

    try:
        if region:
            logger.debug(f"pyautogui区域截图: {region}")
            screenshot = pyautogui.screenshot(region=region)
        else:
            logger.debug("pyautogui全屏截图")
            screenshot = pyautogui.screenshot()

        return screenshot
    except Exception as e:
        logger.error(f"pyautogui截图失败: {e}")
        return None

def take_screenshot_opencv(region=None, use_cache=True, hwnd=None):
    """
    截图并转换为OpenCV格式 (带缓存优化)

    Args:
        region: 截图区域 (left, top, width, height)，None表示全屏
        use_cache: 是否使用缓存
        hwnd: 窗口句柄（用于缓存键）

    Returns:
        numpy.ndarray: OpenCV格式的图像，失败返回None
    """
    # 尝试从缓存获取
    if use_cache and CACHE_AVAILABLE:
        cache = get_screenshot_cache()
        cached_screenshot = cache.get(hwnd, region, "opencv")
        if cached_screenshot is not None:
            return cached_screenshot
    
    # --- MODIFIED: 优先使用VU的OpenCV截图 ---
    screenshot_cv = None
    if VU_SCREENSHOT_AVAILABLE and _screenshot_adapter and CV2_AVAILABLE:
        try:
            logger.debug("使用VU OpenCV截图")
            screenshot_cv = _screenshot_adapter.take_screenshot_opencv(region=region)
            if screenshot_cv is None:
                logger.warning("VU OpenCV截图返回None，尝试使用备用方案")
        except Exception as e:
            logger.error(f"VU OpenCV截图失败: {e}，尝试使用备用方案")
    # --- END MODIFIED ---

    # 如果VU失败，尝试备用方案
    if screenshot_cv is None:
        if not CV2_AVAILABLE:
            logger.error("opencv-python 不可用，无法转换为OpenCV格式")
            return None

        screenshot_pil = take_screenshot(region)
        if screenshot_pil is None:
            return None

        try:
            # 转换为OpenCV格式 (BGR)
            screenshot_cv = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)
        except Exception as e:
            logger.error(f"转换为OpenCV格式失败: {e}")
            return None
    
    # 缓存截图
    if use_cache and CACHE_AVAILABLE and screenshot_cv is not None:
        cache = get_screenshot_cache()
        cache.put(screenshot_cv, hwnd, region, "opencv")
    
    return screenshot_cv

def take_window_screenshot(hwnd, client_area_only=True):
    """
    截取指定窗口的截图

    Args:
        hwnd: 窗口句柄
        client_area_only: 是否只截取客户区

    Returns:
        PIL.Image: 截图图像，失败返回None
    """
    # --- MODIFIED: 优先使用VU的窗口截图 ---
    if VU_SCREENSHOT_AVAILABLE and _screenshot_adapter:
        try:
            logger.debug(f"使用VU窗口截图: hwnd={hwnd}, client_area_only={client_area_only}")
            screenshot = _screenshot_adapter.take_window_screenshot(hwnd, client_area_only)
            if screenshot:
                return screenshot
            else:
                logger.warning("VU窗口截图返回None，尝试使用备用方案")
        except Exception as e:
            logger.error(f"VU窗口截图失败: {e}，尝试使用备用方案")
    # --- END MODIFIED ---

    try:
        import win32gui
        import win32con

        if client_area_only:
            # 获取客户区坐标
            client_rect = win32gui.GetClientRect(hwnd)
            client_point = win32gui.ClientToScreen(hwnd, (0, 0))

            region = (
                client_point[0],
                client_point[1],
                client_rect[2],
                client_rect[3]
            )
        else:
            # 获取整个窗口坐标
            window_rect = win32gui.GetWindowRect(hwnd)
            region = (
                window_rect[0],
                window_rect[1],
                window_rect[2] - window_rect[0],
                window_rect[3] - window_rect[1]
            )

        return take_screenshot(region)
    except Exception as e:
        logger.error(f"窗口截图失败: {e}")
        return None

def is_screenshot_available():
    """检查截图功能是否可用"""
    # --- MODIFIED: 检查VU或pyautogui ---
    return SCREENSHOT_AVAILABLE
    # --- END MODIFIED ---

def get_screenshot_info():
    """获取截图功能信息"""
    # --- MODIFIED: 添加VU信息 ---
    info = {
        'vu_available': VU_SCREENSHOT_AVAILABLE,
        'pyautogui_available': PYAUTOGUI_SCREENSHOT_AVAILABLE,
        'cv2_available': CV2_AVAILABLE,
        'pil_available': PIL_AVAILABLE,
        'primary_backend': 'VU' if VU_SCREENSHOT_AVAILABLE else 'pyautogui'
    }

    # 尝试获取屏幕大小
    try:
        info['screen_size'] = get_screen_size()
    except:
        info['screen_size'] = None
    # --- END MODIFIED ---

    return info

# 向后兼容的函数名
screenshot = take_screenshot
screenshot_opencv = take_screenshot_opencv

if __name__ == "__main__":
    # 测试截图功能
    print("🔍 测试截图功能")
    print("=" * 50)
    
    info = get_screenshot_info()
    print(f"截图功能信息: {info}")
    
    if is_screenshot_available():
        print("✅ 截图功能可用")
        
        # 测试全屏截图
        screenshot = take_screenshot()
        if screenshot:
            print(f"✅ 全屏截图成功: {screenshot.size}")
        else:
            print("❌ 全屏截图失败")
        
        # 测试OpenCV格式
        if CV2_AVAILABLE:
            screenshot_cv = take_screenshot_opencv()
            if screenshot_cv is not None:
                print(f"✅ OpenCV格式截图成功: {screenshot_cv.shape}")
            else:
                print("❌ OpenCV格式截图失败")
    else:
        print("❌ 截图功能不可用")
