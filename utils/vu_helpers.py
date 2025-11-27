# -*- coding: utf-8 -*-
"""
VU工具函数

统一的辅助函数,避免代码重复
"""

import ctypes
from typing import Tuple, List, Optional

def create_coord_pointers(x1: int, y1: int, x2: int, y2: int) -> Tuple:
    """
    创建坐标指针(避免重复代码)

    Args:
        x1, y1, x2, y2: 坐标值

    Returns:
        Tuple: (x1_ptr, y1_ptr, x2_ptr, y2_ptr) 指针元组

    Example:
        x1_ptr, y1_ptr, x2_ptr, y2_ptr = create_coord_pointers(0, 0, 800, 600)
        ret = vu.FindPic(x1_ptr, y1_ptr, x2_ptr, y2_ptr, ...)
    """
    return (
        ctypes.pointer(ctypes.c_long(x1)),
        ctypes.pointer(ctypes.c_long(y1)),
        ctypes.pointer(ctypes.c_long(x2)),
        ctypes.pointer(ctypes.c_long(y2))
    )


def create_result_pointers() -> Tuple:
    """
    创建结果指针

    Returns:
        Tuple: (x, y, x_ptr, y_ptr) x和y是c_long对象,x_ptr和y_ptr是指针

    Example:
        x, y, x_ptr, y_ptr = create_result_pointers()
        ret = vu.FindPic(..., x_ptr, y_ptr)
        if ret > 0:
            print(f"找到: ({x.value}, {y.value})")
    """
    x = ctypes.c_long(0)
    y = ctypes.c_long(0)
    return x, y, ctypes.pointer(x), ctypes.pointer(y)


def threshold_to_sim(threshold: float) -> float:
    """
    TM阈值转VU相似度(0-1 -> 0-1)

    Args:
        threshold: TM的相似度阈值 (0.0-1.0)

    Returns:
        float: VU的相似度 (0.0-1.0)

    Example:
        sim = threshold_to_sim(0.9)  # 0.9
    """
    return max(0.0, min(1.0, threshold))


def threshold_to_percent(threshold: float) -> int:
    """
    阈值转百分比(0-1 -> 0-100)

    Args:
        threshold: 相似度阈值 (0.0-1.0)

    Returns:
        int: 百分比 (0-100)

    Example:
        percent = threshold_to_percent(0.9)  # 90
    """
    return int(max(0.0, min(1.0, threshold)) * 100)


def parse_vu_coords(result_str: str) -> List[Tuple[int, int]]:
    """
    解析VU返回的坐标字符串

    Args:
        result_str: VU返回的坐标字符串,格式"x1,y1,index|x2,y2,index|..."

    Returns:
        List[Tuple[int, int]]: 坐标列表 [(x1, y1), (x2, y2), ...]

    Example:
        coords = parse_vu_coords("100,200,0|300,400,1")
        # 返回: [(100, 200), (300, 400)]
    """
    coords = []
    if result_str:
        for item in result_str.split('|'):
            if ',' in item:
                parts = item.split(',')
                if len(parts) >= 2:
                    try:
                        x = int(parts[0])
                        y = int(parts[1])
                        coords.append((x, y))
                    except ValueError:
                        continue
    return coords


def validate_region(region: Optional[Tuple[int, int, int, int]],
                   screen_width: int, screen_height: int) -> Tuple[int, int, int, int]:
    """
    验证并修正区域坐标

    Args:
        region: 区域坐标 (x1, y1, x2, y2) 或 None
        screen_width: 屏幕宽度
        screen_height: 屏幕高度

    Returns:
        Tuple[int, int, int, int]: 验证后的区域坐标

    Example:
        region = validate_region((0, 0, 2000, 2000), 1920, 1080)
        # 返回: (0, 0, 1920, 1080)
    """
    if region is None:
        return (0, 0, screen_width, screen_height)

    x1, y1, x2, y2 = region

    # 修正坐标
    x1 = max(0, min(x1, screen_width))
    y1 = max(0, min(y1, screen_height))
    x2 = max(x1, min(x2, screen_width))
    y2 = max(y1, min(y2, screen_height))

    return (x1, y1, x2, y2)


def format_color(color: str) -> str:
    """
    格式化颜色值

    Args:
        color: 颜色字符串,可能带#前缀或不带

    Returns:
        str: 格式化后的颜色(大写,无#)

    Example:
        color = format_color("#ff0000")  # "FF0000"
        color = format_color("ff0000")   # "FF0000"
    """
    color = color.strip()
    if color.startswith('#'):
        color = color[1:]
    return color.upper()


def is_valid_color(color: str) -> bool:
    """
    验证颜色格式

    Args:
        color: 颜色字符串

    Returns:
        bool: 是否有效

    Example:
        is_valid_color("FF0000")  # True
        is_valid_color("GGGGGG")  # False
    """
    color = format_color(color)
    if len(color) != 6:
        return False
    try:
        int(color, 16)
        return True
    except ValueError:
        return False


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    RGB转十六进制颜色

    Args:
        r, g, b: RGB值 (0-255)

    Returns:
        str: 十六进制颜色 "RRGGBB"

    Example:
        color = rgb_to_hex(255, 0, 0)  # "FF0000"
    """
    return f"{r:02X}{g:02X}{b:02X}"


def hex_to_rgb(color: str) -> Tuple[int, int, int]:
    """
    十六进制颜色转RGB

    Args:
        color: 十六进制颜色 "RRGGBB" 或 "#RRGGBB"

    Returns:
        Tuple[int, int, int]: (r, g, b)

    Example:
        r, g, b = hex_to_rgb("FF0000")  # (255, 0, 0)
    """
    color = format_color(color)
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    return (r, g, b)


def merge_regions(regions: List[Tuple[int, int, int, int]]) -> Tuple[int, int, int, int]:
    """
    合并多个区域为一个包含所有区域的最小区域

    Args:
        regions: 区域列表 [(x1, y1, x2, y2), ...]

    Returns:
        Tuple[int, int, int, int]: 合并后的区域

    Example:
        merged = merge_regions([(0, 0, 100, 100), (50, 50, 150, 150)])
        # 返回: (0, 0, 150, 150)
    """
    if not regions:
        return (0, 0, 0, 0)

    x1_min = min(r[0] for r in regions)
    y1_min = min(r[1] for r in regions)
    x2_max = max(r[2] for r in regions)
    y2_max = max(r[3] for r in regions)

    return (x1_min, y1_min, x2_max, y2_max)


def region_contains_point(region: Tuple[int, int, int, int], x: int, y: int) -> bool:
    """
    判断点是否在区域内

    Args:
        region: 区域 (x1, y1, x2, y2)
        x, y: 点坐标

    Returns:
        bool: 是否在区域内

    Example:
        contains = region_contains_point((0, 0, 100, 100), 50, 50)  # True
    """
    x1, y1, x2, y2 = region
    return x1 <= x <= x2 and y1 <= y <= y2


def region_intersects(region1: Tuple[int, int, int, int],
                     region2: Tuple[int, int, int, int]) -> bool:
    """
    判断两个区域是否相交

    Args:
        region1, region2: 两个区域

    Returns:
        bool: 是否相交

    Example:
        intersects = region_intersects((0, 0, 100, 100), (50, 50, 150, 150))  # True
    """
    x1_1, y1_1, x2_1, y2_1 = region1
    x1_2, y1_2, x2_2, y2_2 = region2

    return not (x2_1 < x1_2 or x2_2 < x1_1 or y2_1 < y1_2 or y2_2 < y1_1)


def calculate_region_area(region: Tuple[int, int, int, int]) -> int:
    """
    计算区域面积

    Args:
        region: 区域 (x1, y1, x2, y2)

    Returns:
        int: 面积(像素)

    Example:
        area = calculate_region_area((0, 0, 100, 100))  # 10000
    """
    x1, y1, x2, y2 = region
    return (x2 - x1) * (y2 - y1)


# 导出所有函数
__all__ = [
    'create_coord_pointers',
    'create_result_pointers',
    'threshold_to_sim',
    'threshold_to_percent',
    'parse_vu_coords',
    'validate_region',
    'format_color',
    'is_valid_color',
    'rgb_to_hex',
    'hex_to_rgb',
    'merge_regions',
    'region_contains_point',
    'region_intersects',
    'calculate_region_area'
]
