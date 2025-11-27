# -*- coding: utf-8 -*-
"""
VU异常体系

统一的异常定义,方便错误处理和调试
"""


class VUException(Exception):
    """VU基础异常

    所有VU相关异常的基类
    """
    def __init__(self, message: str, details: dict = None):
        """
        Args:
            message: 错误消息
            details: 错误详情字典
        """
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self):
        if self.details:
            details_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{self.message} ({details_str})"
        return self.message


class VUInitError(VUException):
    """VU初始化错误

    VU插件初始化失败时抛出
    """
    def __init__(self, message: str = "VU初始化失败", details: dict = None):
        super().__init__(message, details)


class VUNotInitializedError(VUException):
    """VU未初始化错误

    在VU未初始化时调用方法时抛出
    """
    def __init__(self, message: str = "VU未初始化,请先调用initialize()", details: dict = None):
        super().__init__(message, details)


class VUBindError(VUException):
    """VU绑定窗口错误

    绑定窗口失败时抛出
    """
    def __init__(self, message: str = "绑定窗口失败", hwnd: int = None):
        details = {'hwnd': hwnd} if hwnd else None
        super().__init__(message, details)


class VUUnbindError(VUException):
    """VU解绑窗口错误

    解绑窗口失败时抛出
    """
    def __init__(self, message: str = "解绑窗口失败", details: dict = None):
        super().__init__(message, details)


class VUImageError(VUException):
    """VU图像操作错误

    图像操作相关错误的基类
    """
    pass


class VUImageNotFoundError(VUImageError):
    """图片未找到错误

    查找图片文件不存在时抛出
    """
    def __init__(self, image_path: str):
        message = f"图片文件不存在: {image_path}"
        details = {'image_path': image_path}
        super().__init__(message, details)


class VUImageSearchError(VUImageError):
    """图片搜索错误

    图片搜索过程中发生错误时抛出
    """
    def __init__(self, message: str = "图片搜索失败", image_path: str = None):
        details = {'image_path': image_path} if image_path else None
        super().__init__(message, details)


class VUColorError(VUException):
    """VU颜色操作错误

    颜色操作相关错误的基类
    """
    pass


class VUInvalidColorError(VUColorError):
    """无效颜色错误

    颜色格式不正确时抛出
    """
    def __init__(self, color: str):
        message = f"无效的颜色格式: {color}"
        details = {'color': color}
        super().__init__(message, details)


class VUColorSearchError(VUColorError):
    """颜色搜索错误

    颜色搜索过程中发生错误时抛出
    """
    def __init__(self, message: str = "颜色搜索失败", color: str = None):
        details = {'color': color} if color else None
        super().__init__(message, details)


class VUOCRError(VUException):
    """VU OCR错误

    OCR操作相关错误的基类
    """
    pass


class VUOCRRecognitionError(VUOCRError):
    """OCR识别错误

    OCR识别失败时抛出
    """
    def __init__(self, message: str = "OCR识别失败", region: tuple = None):
        details = {'region': region} if region else None
        super().__init__(message, details)


class VUOCRDictError(VUOCRError):
    """OCR字典错误

    OCR字典加载或设置失败时抛出
    """
    def __init__(self, message: str = "OCR字典操作失败", dict_path: str = None):
        details = {'dict_path': dict_path} if dict_path else None
        super().__init__(message, details)


class VUInputError(VUException):
    """VU输入操作错误

    输入操作(鼠标/键盘)相关错误的基类
    """
    pass


class VUMouseError(VUInputError):
    """鼠标操作错误

    鼠标操作失败时抛出
    """
    def __init__(self, message: str = "鼠标操作失败", operation: str = None):
        details = {'operation': operation} if operation else None
        super().__init__(message, details)


class VUKeyboardError(VUInputError):
    """键盘操作错误

    键盘操作失败时抛出
    """
    def __init__(self, message: str = "键盘操作失败", operation: str = None):
        details = {'operation': operation} if operation else None
        super().__init__(message, details)


class VUScreenshotError(VUException):
    """截图错误

    截图操作失败时抛出
    """
    def __init__(self, message: str = "截图失败", region: tuple = None):
        details = {'region': region} if region else None
        super().__init__(message, details)


class VUCoordinateError(VUException):
    """坐标错误

    坐标相关错误的基类
    """
    pass


class VUInvalidCoordinateError(VUCoordinateError):
    """无效坐标错误

    坐标超出有效范围时抛出
    """
    def __init__(self, coord: tuple, screen_size: tuple = None):
        message = f"无效的坐标: {coord}"
        details = {'coord': coord, 'screen_size': screen_size}
        super().__init__(message, details)


class VUInvalidRegionError(VUCoordinateError):
    """无效区域错误

    区域坐标不正确时抛出
    """
    def __init__(self, region: tuple):
        message = f"无效的区域: {region}"
        details = {'region': region}
        super().__init__(message, details)


class VUWindowError(VUException):
    """窗口操作错误

    窗口操作相关错误的基类
    """
    pass


class VUWindowNotFoundError(VUWindowError):
    """窗口未找到错误

    指定窗口不存在时抛出
    """
    def __init__(self, hwnd: int = None, title: str = None):
        if hwnd:
            message = f"窗口未找到: hwnd={hwnd}"
            details = {'hwnd': hwnd}
        elif title:
            message = f"窗口未找到: title={title}"
            details = {'title': title}
        else:
            message = "窗口未找到"
            details = None
        super().__init__(message, details)


class VUTimeoutError(VUException):
    """超时错误

    操作超时时抛出
    """
    def __init__(self, message: str = "操作超时", timeout: float = None):
        details = {'timeout': timeout} if timeout else None
        super().__init__(message, details)


class VUConfigError(VUException):
    """配置错误

    配置无效或加载失败时抛出
    """
    def __init__(self, message: str = "配置错误", config_key: str = None):
        details = {'config_key': config_key} if config_key else None
        super().__init__(message, details)


# 导出所有异常类
__all__ = [
    # 基础异常
    'VUException',

    # 初始化相关
    'VUInitError',
    'VUNotInitializedError',

    # 绑定相关
    'VUBindError',
    'VUUnbindError',

    # 图像相关
    'VUImageError',
    'VUImageNotFoundError',
    'VUImageSearchError',

    # 颜色相关
    'VUColorError',
    'VUInvalidColorError',
    'VUColorSearchError',

    # OCR相关
    'VUOCRError',
    'VUOCRRecognitionError',
    'VUOCRDictError',

    # 输入相关
    'VUInputError',
    'VUMouseError',
    'VUKeyboardError',

    # 截图相关
    'VUScreenshotError',

    # 坐标相关
    'VUCoordinateError',
    'VUInvalidCoordinateError',
    'VUInvalidRegionError',

    # 窗口相关
    'VUWindowError',
    'VUWindowNotFoundError',

    # 其他
    'VUTimeoutError',
    'VUConfigError',
]
