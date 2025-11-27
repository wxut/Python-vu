"""窗口过滤工具 - 过滤无效窗口和应用程序自身窗口"""
import os
import logging

logger = logging.getLogger(__name__)

try:
    import win32gui
    import win32process
    WIN32_AVAILABLE = True
except ImportError:
    WIN32_AVAILABLE = False
    logger.warning("win32gui 不可用，窗口过滤功能受限")


def is_valid_target_window(hwnd: int) -> bool:
    """
    检查窗口是否是有效的目标窗口
    
    Args:
        hwnd: 窗口句柄
        
    Returns:
        bool: 窗口是否有效
    """
    if not WIN32_AVAILABLE or not hwnd:
        return False
    
    try:
        # 排除自己的窗口
        current_pid = os.getpid()
        _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
        if window_pid == current_pid:
            logger.debug(f"过滤自身窗口 (PID: {current_pid})")
            return False
        
        # 排除不可见窗口
        if not win32gui.IsWindowVisible(hwnd):
            logger.debug(f"过滤不可见窗口 (HWND: {hwnd})")
            return False
        
        # 排除无标题窗口
        title = win32gui.GetWindowText(hwnd)
        if not title or len(title.strip()) == 0:
            logger.debug(f"过滤无标题窗口 (HWND: {hwnd})")
            return False
        
        # 排除特定的系统窗口标题
        excluded_titles = [
            "Program Manager",
            "运行中的应用程序",
            "Default IME",
            "MSCTFIME UI",
            "Microsoft Text Input Application"
        ]
        if title in excluded_titles:
            logger.debug(f"过滤系统窗口: {title}")
            return False
        
        return True
        
    except Exception as e:
        logger.warning(f"检查窗口有效性失败 (HWND: {hwnd}): {e}")
        return False