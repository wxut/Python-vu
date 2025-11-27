# -*- coding: utf-8 -*-
"""
VU图像适配器

提供TM兼容的图像识别接口,底层使用VU插件实现
核心原则: 接口与TM保持一致,内部调用VU的FindPic/FindColor等函数
"""

import logging
from typing import Optional, Tuple, List

logger = logging.getLogger(__name__)


class VUImageAdapter:
    """VU图像适配器 - 提供TM兼容的图像识别接口"""

    def __init__(self, vu_wrapper):
        """
        初始化图像适配器

        Args:
            vu_wrapper: VUWrapper实例
        """
        self.vu_wrapper = vu_wrapper

        # 导入VU图像操作类
        from core.vu_image import VUImage
        self.vu_image = VUImage(vu_wrapper)

        logger.info("VU图像适配器初始化")

    def find_image(self, image_path: str, region: Optional[Tuple[int, int, int, int]] = None,
                   threshold: float = 0.9, delta_color: str = "000000") -> Optional[Tuple[int, int]]:
        """
        查找图片(TM兼容接口)

        与TM的image_operations.find_image_cv接口保持一致
        底层使用VU的FindPic实现

        Args:
            image_path: 图片路径
            region: 搜索区域 (x1, y1, x2, y2),None表示全屏
            threshold: 相似度阈值 (0.0-1.0),TM使用0-1范围
            delta_color: 颜色偏色,格式"RRGGBB",默认"000000"

        Returns:
            Optional[Tuple[int, int]]: 找到返回(x, y),未找到返回None

        Example:
            # TM调用方式
            pos = adapter.find_image("button.bmp", region=(0, 0, 800, 600), threshold=0.9)
            if pos:
                x, y = pos
                print(f"找到图片在: ({x}, {y})")
        """
        try:
            # TM和VU都使用0-1范围的浮点数相似度,无需转换
            logger.debug(
                f"查找图片: {image_path}, 区域:{region}, 相似度:{threshold}"
            )

            # 调用VU的FindPic (threshold参数为0-1浮点数)
            if region:
                x1, y1, x2, y2 = region
                pos = self.vu_image.find_pic(
                    image_path, region=(x1, y1, x2, y2),
                    threshold=threshold
                )
            else:
                pos = self.vu_image.find_pic(
                    image_path,
                    threshold=threshold
                )

            if pos:
                logger.debug(f"找到图片: {pos}")
                return pos
            else:
                logger.debug("未找到图片")
                return None

        except Exception as e:
            logger.error(f"查找图片失败: {e}")
            return None

    def find_all_images(self, image_path: str, region: Optional[Tuple[int, int, int, int]] = None,
                       threshold: float = 0.9, delta_color: str = "000000") -> List[Tuple[int, int]]:
        """
        查找所有图片(TM兼容接口)

        与TM的find_all_images接口保持一致
        底层使用VU的FindPicEx实现

        Args:
            image_path: 图片路径
            region: 搜索区域 (x1, y1, x2, y2),None表示全屏
            threshold: 相似度阈值 (0.0-1.0)
            delta_color: 颜色偏色,格式"RRGGBB"

        Returns:
            List[Tuple[int, int]]: 找到的所有位置列表 [(x1, y1), (x2, y2), ...]

        Example:
            positions = adapter.find_all_images("icon.bmp", threshold=0.85)
            print(f"找到 {len(positions)} 个匹配")
        """
        try:
            # TM和VU都使用0-1范围的浮点数相似度,无需转换
            logger.debug(
                f"查找所有图片: {image_path}, 区域:{region}, 相似度:{threshold}"
            )

            # 调用VU的FindPicEx (threshold参数为0-1浮点数)
            if region:
                x1, y1, x2, y2 = region
                positions = self.vu_image.find_pic_ex(
                    image_path, region=(x1, y1, x2, y2),
                    threshold=threshold
                )
            else:
                positions = self.vu_image.find_pic_ex(
                    image_path,
                    threshold=threshold
                )

            logger.debug(f"找到 {len(positions)} 个匹配位置")
            return positions

        except Exception as e:
            logger.error(f"查找所有图片失败: {e}")
            return []

    def find_color(self, color: str, region: Optional[Tuple[int, int, int, int]] = None,
                   threshold: float = 0.9) -> Optional[Tuple[int, int]]:
        """
        查找颜色(TM兼容接口)

        与TM的颜色查找接口保持一致
        底层使用VU的FindColor实现

        Args:
            color: 颜色值,格式"RRGGBB"
            region: 搜索区域 (x1, y1, x2, y2),None表示全屏
            threshold: 相似度阈值 (0.0-1.0)

        Returns:
            Optional[Tuple[int, int]]: 找到返回(x, y),未找到返回None

        Example:
            pos = adapter.find_color("FF0000", region=(0, 0, 800, 600))  # 查找红色
        """
        try:
            # TM和VU都使用0-1范围的浮点数相似度,无需转换
            logger.debug(
                f"查找颜色: {color}, 区域:{region}, 相似度:{threshold}"
            )

            # 调用VU的FindColor (threshold参数为0-1浮点数)
            if region:
                x1, y1, x2, y2 = region
                pos = self.vu_image.find_color(
                    color, region=(x1, y1, x2, y2), threshold=threshold
                )
            else:
                pos = self.vu_image.find_color(color, threshold=threshold)

            if pos:
                logger.debug(f"找到颜色: {pos}")
                return pos
            else:
                logger.debug("未找到颜色")
                return None

        except Exception as e:
            logger.error(f"查找颜色失败: {e}")
            return None

    def find_all_colors(self, color: str, region: Optional[Tuple[int, int, int, int]] = None,
                       threshold: float = 0.9) -> List[Tuple[int, int]]:
        """
        查找所有颜色(TM兼容接口)

        底层使用VU的FindColorEx实现

        Args:
            color: 颜色值,格式"RRGGBB"
            region: 搜索区域 (x1, y1, x2, y2),None表示全屏
            threshold: 相似度阈值 (0.0-1.0)

        Returns:
            List[Tuple[int, int]]: 找到的所有位置列表
        """
        try:
            # TM和VU都使用0-1范围的浮点数相似度,无需转换
            logger.debug(
                f"查找所有颜色: {color}, 区域:{region}, 相似度:{threshold}"
            )

            # 调用VU的FindColorEx (threshold参数为0-1浮点数)
            if region:
                x1, y1, x2, y2 = region
                positions = self.vu_image.find_color_ex(
                    color, region=(x1, y1, x2, y2), threshold=threshold
                )
            else:
                positions = self.vu_image.find_color_ex(color, threshold=threshold)

            logger.debug(f"找到 {len(positions)} 个匹配颜色")
            return positions

        except Exception as e:
            logger.error(f"查找所有颜色失败: {e}")
            return []

    def get_pixel_color(self, x: int, y: int) -> Optional[str]:
        """
        获取像素颜色(TM兼容接口)

        Args:
            x: X坐标
            y: Y坐标

        Returns:
            Optional[str]: 颜色值,格式"RRGGBB",失败返回None

        Example:
            color = adapter.get_pixel_color(100, 100)
            print(f"坐标(100, 100)的颜色: {color}")
        """
        try:
            color = self.vu_image.get_pixel_color(x, y)
            logger.debug(f"获取像素颜色: ({x}, {y}) -> {color}")
            return color

        except Exception as e:
            logger.error(f"获取像素颜色失败: {e}")
            return None

    def capture_region(self, region: Tuple[int, int, int, int], save_path: Optional[str] = None) -> bool:
        """
        截取区域(TM兼容接口)

        Args:
            region: 截图区域 (x1, y1, x2, y2)
            save_path: 保存路径,None表示不保存

        Returns:
            bool: 成功返回True

        Example:
            success = adapter.capture_region((0, 0, 800, 600), "screenshot.bmp")
        """
        try:
            x1, y1, x2, y2 = region

            if save_path:
                # 使用VU的Capture保存到文件
                result = self.vu_image.capture_to_file(x1, y1, x2, y2, save_path)
                logger.debug(f"截图保存: {save_path}, 结果:{result}")
                return result
            else:
                # 仅截图不保存
                # VU的Capture需要文件路径,这里使用临时文件
                import tempfile
                import os
                temp_file = tempfile.mktemp(suffix=".bmp")
                result = self.vu_image.capture_to_file(x1, y1, x2, y2, temp_file)

                # 删除临时文件
                try:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                except Exception:
                    pass

                return result

        except Exception as e:
            logger.error(f"截取区域失败: {e}")
            return False

    def compare_images(self, image1_path: str, image2_path: str, threshold: float = 0.9) -> bool:
        """
        比较两个图片是否相似(TM兼容接口)

        Args:
            image1_path: 图片1路径
            image2_path: 图片2路径
            threshold: 相似度阈值 (0.0-1.0)

        Returns:
            bool: 相似返回True

        Example:
            is_similar = adapter.compare_images("img1.bmp", "img2.bmp", 0.95)
        """
        try:
            # VU的CmpPic函数
            vu_threshold = threshold * 100
            vu_similarity = str(int(vu_threshold))

            result = self.vu_image.compare_pic(image1_path, image2_path, vu_similarity)
            logger.debug(f"比较图片: {result}")
            return result

        except Exception as e:
            logger.error(f"比较图片失败: {e}")
            return False


# 导出类
__all__ = ['VUImageAdapter']
