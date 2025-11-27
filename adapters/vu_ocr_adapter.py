# -*- coding: utf-8 -*-
"""
VU OCR适配器

提供TM兼容的OCR接口,底层使用VU插件实现
核心原则: 接口与TM的unified_ocr_service保持一致,内部调用VU的OCR函数
"""

import logging
from typing import Optional, Tuple, List, Dict, Any

logger = logging.getLogger(__name__)


class VUOCRAdapter:
    """VU OCR适配器 - 提供TM兼容的OCR接口"""

    def __init__(self, vu_wrapper):
        """
        初始化OCR适配器

        Args:
            vu_wrapper: VUWrapper实例
        """
        self.vu_wrapper = vu_wrapper

        # 导入VU OCR操作类
        from core.vu_ocr import VUOCR
        self.vu_ocr = VUOCR(vu_wrapper)

        logger.info("VU OCR适配器初始化")

    def recognize_text(self, x1: int, y1: int, x2: int, y2: int,
                      color: str = "FFFFFF-000000",
                      threshold: float = 0.9) -> Optional[str]:
        """
        识别文本(TM兼容接口)

        与TM的recognize_text_with_unified_service接口保持一致
        底层使用VU的Ocr实现

        Args:
            x1, y1, x2, y2: OCR识别区域
            color: 颜色格式,格式"前景色-背景色",如"FFFFFF-000000"
            threshold: 相似度阈值 (0.0-1.0)

        Returns:
            Optional[str]: 识别的文本,失败返回None

        Example:
            # TM调用方式
            text = adapter.recognize_text(100, 100, 300, 150, "FFFFFF-000000")
            if text:
                print(f"识别文本: {text}")
        """
        try:
            # VU的Ocr使用0-1范围的浮点数
            vu_sim = threshold

            logger.debug(
                f"识别文本: 区域({x1},{y1},{x2},{y2}), "
                f"颜色:{color}, 相似度:{vu_sim}"
            )

            # 调用VU的Ocr (参数名是sim,不是similarity)
            text = self.vu_ocr.recognize_text(
                x1, y1, x2, y2,
                color_format=color,
                sim=vu_sim
            )

            if text:
                logger.debug(f"识别结果: {text}")
                return text
            else:
                logger.debug("未识别到文本")
                return None

        except Exception as e:
            logger.error(f"识别文本失败: {e}")
            return None

    def recognize_text_with_result(self, x1: int, y1: int, x2: int, y2: int,
                                   color: str = "FFFFFF-000000",
                                   threshold: float = 0.9) -> Dict[str, Any]:
        """
        识别文本并返回详细结果(TM兼容接口)

        返回格式与TM的FastDeploy OCR结果保持一致

        Args:
            x1, y1, x2, y2: OCR识别区域
            color: 颜色格式
            threshold: 相似度阈值 (0.0-1.0)

        Returns:
            Dict[str, Any]: 识别结果字典
            {
                'success': bool,  # 是否成功
                'text': str,      # 识别的文本
                'boxes': List,    # 文本框坐标
                'scores': List    # 置信度
            }

        Example:
            result = adapter.recognize_text_with_result(100, 100, 300, 150)
            if result['success']:
                print(f"文本: {result['text']}, 置信度: {result['scores']}")
        """
        try:
            # 调用基本识别
            text = self.recognize_text(x1, y1, x2, y2, color, threshold)

            if text:
                # 构造TM兼容的结果格式
                result = {
                    'success': True,
                    'text': text,
                    'boxes': [],  # VU不提供详细坐标,返回空列表
                    'scores': [threshold]  # 使用输入阈值作为置信度
                }
                return result
            else:
                return {
                    'success': False,
                    'text': '',
                    'boxes': [],
                    'scores': []
                }

        except Exception as e:
            logger.error(f"识别文本失败: {e}")
            return {
                'success': False,
                'text': '',
                'boxes': [],
                'scores': [],
                'error': str(e)
            }

    def find_text(self, text: str, x1: int, y1: int, x2: int, y2: int,
                 color: str = "FFFFFF-000000",
                 threshold: float = 0.9) -> Optional[Tuple[int, int]]:
        """
        查找文本位置(TM兼容接口)

        底层使用VU的FindStr实现

        Args:
            text: 要查找的文本
            x1, y1, x2, y2: 搜索区域
            color: 颜色格式
            threshold: 相似度阈值 (0.0-1.0)

        Returns:
            Optional[Tuple[int, int]]: 找到返回(x, y),未找到返回None

        Example:
            pos = adapter.find_text("确定", 0, 0, 800, 600)
            if pos:
                print(f"找到文本在: {pos}")
        """
        try:
            # 转换相似度
            vu_threshold = threshold * 100
            vu_similarity = str(int(vu_threshold))

            logger.debug(
                f"查找文本: '{text}', 区域({x1},{y1},{x2},{y2}), "
                f"相似度:{vu_similarity}"
            )

            # 调用VU的FindStr
            pos = self.vu_ocr.find_str(
                x1, y1, x2, y2, text,
                color_format=color,
                similarity=vu_similarity
            )

            if pos:
                logger.debug(f"找到文本: {pos}")
                return pos
            else:
                logger.debug("未找到文本")
                return None

        except Exception as e:
            logger.error(f"查找文本失败: {e}")
            return None

    def find_all_text(self, text: str, x1: int, y1: int, x2: int, y2: int,
                     color: str = "FFFFFF-000000",
                     threshold: float = 0.9) -> List[Tuple[int, int]]:
        """
        查找所有文本位置(TM兼容接口)

        底层使用VU的FindStrEx实现

        Args:
            text: 要查找的文本
            x1, y1, x2, y2: 搜索区域
            color: 颜色格式
            threshold: 相似度阈值 (0.0-1.0)

        Returns:
            List[Tuple[int, int]]: 找到的所有位置列表

        Example:
            positions = adapter.find_all_text("按钮", 0, 0, 800, 600)
            print(f"找到 {len(positions)} 个匹配")
        """
        try:
            # 转换相似度
            vu_threshold = threshold * 100
            vu_similarity = str(int(vu_threshold))

            logger.debug(
                f"查找所有文本: '{text}', 区域({x1},{y1},{x2},{y2})"
            )

            # 调用VU的FindStrEx
            positions = self.vu_ocr.find_str_ex(
                x1, y1, x2, y2, text,
                color_format=color,
                similarity=vu_similarity
            )

            logger.debug(f"找到 {len(positions)} 个匹配文本")
            return positions

        except Exception as e:
            logger.error(f"查找所有文本失败: {e}")
            return []

    def recognize_region_with_boxes(self, x1: int, y1: int, x2: int, y2: int,
                                   color: str = "FFFFFF-000000") -> List[Dict[str, Any]]:
        """
        识别区域内所有文本并返回文本框(TM兼容接口)

        与TM的FastDeploy OCR返回格式保持一致

        Args:
            x1, y1, x2, y2: OCR识别区域
            color: 颜色格式

        Returns:
            List[Dict[str, Any]]: 文本框列表
            [
                {
                    'text': str,        # 文本内容
                    'box': List[Tuple], # 文本框坐标 [(x1,y1), (x2,y2), ...]
                    'score': float      # 置信度
                },
                ...
            ]

        Example:
            boxes = adapter.recognize_region_with_boxes(0, 0, 800, 600)
            for box in boxes:
                print(f"文本: {box['text']}, 位置: {box['box']}")
        """
        try:
            # VU的基本OCR不提供详细文本框坐标
            # 这里提供简化实现,返回整体识别结果

            text = self.recognize_text(x1, y1, x2, y2, color)

            if text:
                # 构造TM兼容格式
                boxes = [{
                    'text': text,
                    'box': [(x1, y1), (x2, y1), (x2, y2), (x1, y2)],
                    'score': 0.9
                }]
                return boxes
            else:
                return []

        except Exception as e:
            logger.error(f"识别区域文本框失败: {e}")
            return []

    def set_ocr_dict(self, dict_path: str) -> bool:
        """
        设置OCR字典(TM兼容接口)

        底层使用VU的SetDict实现

        Args:
            dict_path: 字典文件路径

        Returns:
            bool: 成功返回True

        Example:
            success = adapter.set_ocr_dict("custom_dict.txt")
        """
        try:
            result = self.vu_ocr.set_dict(dict_path)
            logger.debug(f"设置OCR字典: {dict_path}, 结果:{result}")
            return result

        except Exception as e:
            logger.error(f"设置OCR字典失败: {e}")
            return False

    def use_default_dict(self) -> bool:
        """
        使用默认字典(TM兼容接口)

        底层使用VU的UseDict实现

        Returns:
            bool: 成功返回True
        """
        try:
            result = self.vu_ocr.use_default_dict()
            logger.debug(f"使用默认字典, 结果:{result}")
            return result

        except Exception as e:
            logger.error(f"使用默认字典失败: {e}")
            return False


# 导出类
__all__ = ['VUOCRAdapter']
