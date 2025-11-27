# -*- coding: utf-8 -*-
"""
WY项目核心层 - VU插件封装

提供VU插件的统一调用接口
"""

from .vu_wrapper import VUWrapper
from .vu_image import VUImage
from .vu_mouse import VUMouse
from .vu_keyboard import VUKeyboard
from .vu_ocr import VUOCR
from .vu_window import VUWindow

__all__ = [
    'VUWrapper',
    'VUImage',
    'VUMouse',
    'VUKeyboard',
    'VUOCR',
    'VUWindow'
]
