# -*- coding: utf-8 -*-
"""
任务模块包初始化
"""

# 导入所有任务模块
from . import (
    click_coordinate,
    conditional_control,
    delay_task,
    find_color_task,
    find_image_and_click,
    keyboard_input,
    ldplayer_app_manager,
    mouse_click_simulation,
    mouse_scroll,
    mumu_app_manager,
    ocr_region_recognition,
    optimized_multi_image_click,
    parallel_image_recognition,
    rotate_view_task,
    start_task,
    task_module,
    vu_mouse_click,
    vu_find_pic_ex,
    vu_find_color_ex,
    vu_find_multi_color,
    vu_find_shape,
    vu_ai_find_pic,
    vu_find_color_block,
    vu_find_color,
    vu_ocr,
    vu_capture,
    vu_keyboard,
    vu_window_bind,
    vu_find_pic_super,
    vu_save_pic,
    vu_json_handler,
    vu_window_manager,
    vu_image_advanced,
    vu_memory_ops,
    vu_ai_yolo
)

# 任务模块映射字典
TASK_MODULES = {
    '点击坐标': click_coordinate,
    '条件控制': conditional_control,
    '延时': delay_task,
    '找色': find_color_task,
    '找图点击': find_image_and_click,
    '键盘输入': keyboard_input,
    '雷电应用管理': ldplayer_app_manager,
    '鼠标点击': mouse_click_simulation,
    '鼠标滚轮': mouse_scroll,
    'MuMu应用管理': mumu_app_manager,
    'OCR区域识别': ocr_region_recognition,
    '多图识别点击': optimized_multi_image_click,
    '并行图像识别': parallel_image_recognition,
    '旋转视角': rotate_view_task,
    '开始': start_task,
    '任务模块': task_module,
    '无忧鼠标点击': vu_mouse_click,
    'VU找图Ex': vu_find_pic_ex,
    'VU找色Ex': vu_find_color_ex,
    '无忧找色': vu_find_color,
    'VU多色查找': vu_find_multi_color,
    'VU形状查找': vu_find_shape,
    'VU AI找图': vu_ai_find_pic,
    'VU色块查找': vu_find_color_block,
    '无忧OCR识别': vu_ocr,
    '无忧截图': vu_capture,
    '无忧键盘操作': vu_keyboard,
    '无忧窗口绑定': vu_window_bind,
    '无忧超级找图': vu_find_pic_super,
    '无忧图像保存': vu_save_pic,
    '无忧JSON处理': vu_json_handler,
    '无忧窗口管理': vu_window_manager,
    '无忧图像处理': vu_image_advanced,
    '无忧内存操作': vu_memory_ops,
    '无忧AI YOLO': vu_ai_yolo
}

def get_available_tasks():
    """返回所有可用的任务类型列表"""
    return list(TASK_MODULES.keys())

def get_task_modules():
    """返回任务模块字典"""
    return TASK_MODULES

__all__ = ['TASK_MODULES', 'get_available_tasks', 'get_task_modules']