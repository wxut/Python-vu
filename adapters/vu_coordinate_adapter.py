# -*- coding: utf-8 -*-
"""
VU坐标适配器

将TM的CoordinateInfo转换为VU可用的坐标
核心原则: VU适配TM的坐标系统,不改变TM的坐标标准
"""

import logging
from typing import Tuple, Optional
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class CoordinateType(Enum):
    """坐标类型(与TM保持一致)"""
    REFERENCE = "reference"  # 基准坐标
    PHYSICAL = "physical"    # 物理坐标
    LOGICAL = "logical"      # 逻辑坐标


@dataclass
class CoordinateInfo:
    """坐标信息(与TM保持一致)"""
    x: int
    y: int
    width: int = 0
    height: int = 0
    coord_type: CoordinateType = CoordinateType.PHYSICAL
    source_window: Optional[int] = None
    timestamp: float = 0.0


class VUCoordinateAdapter:
    """VU坐标适配器 - 桥接TM坐标系统与VU插件"""

    def __init__(self, vu_wrapper):
        """
        初始化坐标适配器

        Args:
            vu_wrapper: VUWrapper实例
        """
        self.vu = vu_wrapper
        logger.info("VU坐标适配器初始化")

    def tm_coord_to_vu(self, coord_info: CoordinateInfo, hwnd: int = 0) -> Tuple[int, int]:
        """
        将TM坐标转换为VU坐标

        TM: CoordinateInfo对象(可能是基准坐标或物理坐标)
        VU: (x, y) 元组,客户区坐标

        Args:
            coord_info: TM的坐标信息
            hwnd: 窗口句柄

        Returns:
            Tuple[int, int]: VU可用的(x, y)坐标
        """
        try:
            # VU使用客户区坐标,直接返回x, y
            # 注意: 如果coord_info是基准坐标(REFERENCE),
            # 调用者应该先使用TM的denormalize_coordinate转换为物理坐标

            if coord_info.coord_type == CoordinateType.REFERENCE:
                logger.warning(
                    f"坐标类型为REFERENCE,建议先使用TM的坐标系统转换为PHYSICAL"
                )

            logger.debug(
                f"TM坐标转VU: ({coord_info.x}, {coord_info.y}) "
                f"类型:{coord_info.coord_type.value}"
            )

            return (coord_info.x, coord_info.y)

        except Exception as e:
            logger.error(f"坐标转换失败: {e}")
            return (coord_info.x, coord_info.y)

    def vu_coord_to_tm(self, x: int, y: int, hwnd: int = 0,
                       width: int = 0, height: int = 0) -> CoordinateInfo:
        """
        将VU坐标转换为TM坐标

        VU: (x, y) 元组
        TM: CoordinateInfo对象

        Args:
            x: X坐标
            y: Y坐标
            hwnd: 窗口句柄
            width: 宽度(可选)
            height: 高度(可选)

        Returns:
            CoordinateInfo: TM的坐标信息对象
        """
        import time

        try:
            coord_info = CoordinateInfo(
                x=x, y=y,
                width=width, height=height,
                coord_type=CoordinateType.PHYSICAL,
                source_window=hwnd,
                timestamp=time.time()
            )

            logger.debug(
                f"VU坐标转TM: ({x}, {y}) -> CoordinateInfo(PHYSICAL)"
            )

            return coord_info

        except Exception as e:
            logger.error(f"坐标转换失败: {e}")
            # 返回基本的坐标信息
            return CoordinateInfo(x=x, y=y, coord_type=CoordinateType.PHYSICAL)

    def tm_region_to_vu(self, coord_info: CoordinateInfo) -> Tuple[int, int, int, int]:
        """
        将TM区域坐标转换为VU区域坐标

        Args:
            coord_info: TM的坐标信息(包含x, y, width, height)

        Returns:
            Tuple[int, int, int, int]: VU可用的(x1, y1, x2, y2)区域坐标
        """
        try:
            x1 = coord_info.x
            y1 = coord_info.y
            x2 = coord_info.x + coord_info.width
            y2 = coord_info.y + coord_info.height

            logger.debug(
                f"TM区域转VU: ({coord_info.x}, {coord_info.y}, "
                f"{coord_info.width}, {coord_info.height}) -> ({x1}, {y1}, {x2}, {y2})"
            )

            return (x1, y1, x2, y2)

        except Exception as e:
            logger.error(f"区域坐标转换失败: {e}")
            return (coord_info.x, coord_info.y,
                    coord_info.x + coord_info.width,
                    coord_info.y + coord_info.height)

    def vu_region_to_tm(self, x1: int, y1: int, x2: int, y2: int,
                       hwnd: int = 0) -> CoordinateInfo:
        """
        将VU区域坐标转换为TM区域坐标

        Args:
            x1, y1, x2, y2: VU的区域坐标
            hwnd: 窗口句柄

        Returns:
            CoordinateInfo: TM的坐标信息对象(包含width和height)
        """
        import time

        try:
            x = x1
            y = y1
            width = x2 - x1
            height = y2 - y1

            coord_info = CoordinateInfo(
                x=x, y=y,
                width=width, height=height,
                coord_type=CoordinateType.PHYSICAL,
                source_window=hwnd,
                timestamp=time.time()
            )

            logger.debug(
                f"VU区域转TM: ({x1}, {y1}, {x2}, {y2}) -> "
                f"CoordinateInfo({x}, {y}, {width}, {height})"
            )

            return coord_info

        except Exception as e:
            logger.error(f"区域坐标转换失败: {e}")
            return CoordinateInfo(
                x=x1, y=y1,
                width=x2-x1, height=y2-y1,
                coord_type=CoordinateType.PHYSICAL
            )


# 导出类和常量
__all__ = ['VUCoordinateAdapter', 'CoordinateInfo', 'CoordinateType']
