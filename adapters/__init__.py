# -*- coding: utf-8 -*-
"""
WY项目适配层

将VU插件适配到TM项目的接口标准
"""

from .vu_coordinate_adapter import VUCoordinateAdapter, CoordinateInfo, CoordinateType
from .vu_image_adapter import VUImageAdapter
from .vu_ocr_adapter import VUOCRAdapter
from .vu_input_adapter import VUInputAdapter
from .vu_screenshot_adapter import VUScreenshotAdapter

__all__ = [
    'VUCoordinateAdapter',
    'CoordinateInfo',
    'CoordinateType',
    'VUImageAdapter',
    'VUOCRAdapter',
    'VUInputAdapter',
    'VUScreenshotAdapter'
]
