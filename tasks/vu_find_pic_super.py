# -*- coding: utf-8 -*-
"""
VU超级找图任务模块
支持AiFindPicSuper - 可查找缩放和旋转的图片
"""
from typing import Dict, Any, Optional, List, Tuple
import logging

logger = logging.getLogger(__name__)

from .task_utils import handle_next_step_delay as _handle_next_step_delay

TASK_TYPE = "无忧超级找图"
TASK_NAME = "无忧超级找图"

def get_params_definition() -> Dict[str, Dict[str, Any]]:
    """获取参数定义"""
    return {
        "pic_names": {
            "label": "图片文件名",
            "type": "text",
            "default": "",
            "tooltip": "图片文件名,多个用|分隔,如: pic1.bmp|pic2.bmp"
        },
        "sim": {
            "label": "相似度",
            "type": "float",
            "default": 0.9,
            "min": 0.1,
            "max": 1.0,
            "step": 0.01,
            "decimals": 2,
            "tooltip": "图片匹配相似度(0.1-1.0)"
        },
        "det_mode": {
            "label": "检测模式",
            "type": "select",
            "options": ["标准模式", "高精度模式", "高速度模式"],
            "default": "标准模式",
            "tooltip": "选择检测模式"
        },
        "is_bin": {
            "label": "二值化",
            "type": "bool",
            "default": False,
            "tooltip": "是否使用二值化处理"
        },
        "auto_click": {
            "label": "自动点击",
            "type": "bool",
            "default": False,
            "tooltip": "找到图片后自动点击"
        },
        "click_offset_x": {
            "label": "点击偏移X",
            "type": "int",
            "default": 0,
            "tooltip": "点击位置的X偏移量",
            "condition": {"param": "auto_click", "value": True}
        },
        "click_offset_y": {
            "label": "点击偏移Y",
            "type": "int",
            "default": 0,
            "tooltip": "点击位置的Y偏移量",
            "condition": {"param": "auto_click", "value": True}
        },
        "---next_step_delay---": {"type": "separator", "label": "下一步延迟执行"},
        "enable_next_step_delay": {
            "label": "启用下一步延迟执行",
            "type": "bool",
            "default": False,
            "tooltip": "勾选后,执行完当前操作会等待指定时间再执行下一步"
        },
        "delay_mode": {
            "label": "延迟模式",
            "type": "select",
            "options": ["固定延迟", "随机延迟"],
            "default": "固定延迟",
            "tooltip": "选择固定延迟时间还是随机延迟时间",
            "condition": {"param": "enable_next_step_delay", "value": True}
        },
        "fixed_delay": {
            "label": "固定延迟 (秒)",
            "type": "float",
            "default": 1.0,
            "min": 0.0,
            "max": 3600.0,
            "step": 0.1,
            "decimals": 2,
            "tooltip": "设置固定的延迟时间",
            "condition": {"param": "delay_mode", "value": "固定延迟"}
        },
        "min_delay": {
            "label": "最小延迟 (秒)",
            "type": "float",
            "default": 0.5,
            "min": 0.0,
            "max": 3600.0,
            "step": 0.1,
            "decimals": 2,
            "tooltip": "设置随机延迟的最小值",
            "condition": {"param": "delay_mode", "value": "随机延迟"}
        },
        "max_delay": {
            "label": "最大延迟 (秒)",
            "type": "float",
            "default": 2.0,
            "min": 0.0,
            "max": 3600.0,
            "step": 0.1,
            "decimals": 2,
            "tooltip": "设置随机延迟的最大值",
            "condition": {"param": "delay_mode", "value": "随机延迟"}
        },
        "---post_execute---": {"type": "separator", "label": "执行后操作"},
        "on_success": {
            "label": "成功后操作",
            "type": "select",
            "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"],
            "default": "执行下一步",
            "tooltip": "找到图片后的操作"
        },
        "success_jump_target_id": {
            "label": "成功跳转目标ID",
            "type": "int",
            "default": 0,
            "min": 0,
            "widget_hint": "card_selector",
            "condition": {"param": "on_success", "value": "跳转到步骤"}
        },
        "on_failure": {
            "label": "失败后操作",
            "type": "select",
            "options": ["继续执行本步骤", "执行下一步", "跳转到步骤", "停止工作流"],
            "default": "执行下一步",
            "tooltip": "未找到图片后的操作"
        },
        "failure_jump_target_id": {
            "label": "失败跳转目标ID",
            "type": "int",
            "default": 0,
            "min": 0,
            "widget_hint": "card_selector",
            "condition": {"param": "on_failure", "value": "跳转到步骤"}
        }
    }

def execute_task(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
                target_hwnd: Optional[int], window_region: Optional[tuple], card_id: Optional[int],
                get_image_data=None, **kwargs) -> Tuple[bool, str, Optional[int]]:
    """执行无忧超级找图任务"""
    return execute(params, counters, execution_mode, target_hwnd, window_region, card_id, kwargs.get('stop_checker'))

def execute(params: Dict[str, Any], counters: Dict[str, int], execution_mode: str,
           target_hwnd: Optional[int], window_region: Optional[tuple], card_id: Optional[int],
           stop_checker=None) -> Tuple[bool, str, Optional[int]]:
    """执行无忧超级找图任务"""
    
    pic_names = params.get('pic_names', '')
    sim = params.get('sim', 0.9)
    det_mode_str = params.get('det_mode', '标准模式')
    is_bin = 1 if params.get('is_bin', False) else 0
    auto_click = params.get('auto_click', False)
    click_offset_x = params.get('click_offset_x', 0)
    click_offset_y = params.get('click_offset_y', 0)
    on_success_action = params.get('on_success', '执行下一步')
    success_jump_id = params.get('success_jump_target_id')
    on_failure_action = params.get('on_failure', '执行下一步')
    failure_jump_id = params.get('failure_jump_target_id')
    
    # 转换检测模式
    det_mode_map = {"标准模式": 0, "高精度模式": 1, "高速度模式": 2}
    det_mode = det_mode_map.get(det_mode_str, 0)
    
    logger.info(f"开始执行无忧超级找图: 图片={pic_names}, 相似度={sim}")
    
    try:
        from core.dual_mode_manager import get_dual_mode_manager
        manager = get_dual_mode_manager()
        vu = manager.vu_wrapper
        
        if not vu.is_initialized():
            logger.error("VU插件未初始化")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        if not pic_names:
            logger.error("未指定图片文件")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
        
        # 获取搜索区域
        if window_region:
            x1, y1, x2, y2 = window_region
        else:
            width, height = vu.vu.GetScreenSize()
            x1, y1, x2, y2 = 0, 0, width, height
        
        # 执行超级找图
        intX, intY = 0, 0
        result = vu.vu.AiFindPicSuper(x1, y1, x2, y2, pic_names, sim, det_mode, is_bin, intX, intY)
        
        if result >= 0 and intX >= 0 and intY >= 0:
            logger.info(f"找到图片: index={result}, 位置=({intX},{intY})")
            
            # 如果需要点击
            if auto_click:
                click_x = intX + click_offset_x
                click_y = intY + click_offset_y
                vu.vu.MoveTo(click_x, click_y)
                vu.vu.LeftClick()
                logger.info(f"已点击位置: ({click_x},{click_y})")
            
            if params.get('enable_next_step_delay', False):
                _handle_next_step_delay(params, stop_checker)
            
            return _handle_success(on_success_action, success_jump_id, card_id)
        else:
            logger.warning(f"未找到图片: {pic_names}")
            return _handle_failure(on_failure_action, failure_jump_id, card_id)
            
    except Exception as e:
        logger.error(f"执行无忧超级找图时发生异常: {e}", exc_info=True)
        return _handle_failure(on_failure_action, failure_jump_id, card_id)

def _handle_success(action: str, jump_id: Optional[int], card_id: Optional[int]) -> Tuple[bool, str, Optional[int]]:
    """处理成功情况"""
    if action == '跳转到步骤':
        return True, '跳转到步骤', jump_id
    elif action == '停止工作流':
        return True, '停止工作流', None
    elif action == '继续执行本步骤':
        return True, '继续执行本步骤', card_id
    else:
        return True, '执行下一步', None

def _handle_failure(action: str, jump_id: Optional[int], card_id: Optional[int]) -> Tuple[bool, str, Optional[int]]:
    """处理失败情况"""
    if action == '跳转到步骤':
        return False, '跳转到步骤', jump_id
    elif action == '停止工作流':
        return False, '停止工作流', None
    elif action == '继续执行本步骤':
        return False, '继续执行本步骤', card_id
    else:
        return False, '执行下一步', None

def _get_search_region(vu, window_region: Optional[Tuple[int, int, int, int]]) -> Tuple[int, int, int, int]:
    """获取搜索区域"""
    if window_region:
        return window_region
    width, height = vu.GetScreenSize()
    return (0, 0, width, height)

class VuFindPicSuperTask:
    """VU超级找图任务 - 支持缩放和旋转"""
    
    def __init__(self):
        self.name = "VU超级找图"
        self.description = "使用AI超级找图,支持缩放和旋转的图片查找"
    
    def execute(self, vu, params: Dict[str, Any]) -> bool:
        """
        执行超级找图
        
        Args:
            vu: VU插件实例
            params: 参数字典,包含:
                - pic_names: 图片文件名列表或字符串
                - sim: 相似度 (0.1-1.0)
                - window_region: 搜索区域 (x1,y1,x2,y2)
                - det_mode: 检测模式 (0=标准,1=高精度,2=高速度)
                - is_bin: 是否二值化 (0=否,1=是)
                - click_offset: 点击偏移 (x,y)
        """
        try:
            pic_names = params.get('pic_names', [])
            if isinstance(pic_names, str):
                pic_names = pic_names.split('|')
            
            if not pic_names:
                logger.error("未指定图片文件")
                return False
            
            # 组合图片名称
            pic_name_str = '|'.join(pic_names)
            
            sim = params.get('sim', 0.9)
            window_region = params.get('window_region')
            det_mode = params.get('det_mode', 0)  # 0=标准,1=高精度,2=高速度
            is_bin = params.get('is_bin', 0)  # 是否二值化
            click_offset = params.get('click_offset', (0, 0))
            
            # 获取搜索区域
            x1, y1, x2, y2 = _get_search_region(vu, window_region)
            
            # 执行超级找图
            intX, intY = 0, 0
            result = vu.AiFindPicSuper(x1, y1, x2, y2, pic_name_str, sim, det_mode, is_bin, intX, intY)
            
            if result >= 0 and intX >= 0 and intY >= 0:
                logger.info(f"找到图片: index={result}, 位置=({intX},{intY})")
                
                # 如果需要点击
                if params.get('auto_click', False):
                    click_x = intX + click_offset[0]
                    click_y = intY + click_offset[1]
                    vu.MoveTo(click_x, click_y)
                    vu.LeftClick()
                    logger.info(f"已点击位置: ({click_x},{click_y})")
                
                return True
            else:
                logger.warning(f"未找到图片: {pic_name_str}")
                return False
                
        except Exception as e:
            logger.error(f"超级找图异常: {e}")
            return False