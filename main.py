#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
无忧自动化工具 - 主程序入口（VU插件版本）
支持多窗口任务执行、OCR识别、图像识别等功能
"""

import sys
import os
import json
import logging
import ctypes
from pathlib import Path

# 添加项目根目录到系统路径
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# 默认执行模式
DEFAULT_MODE = "auto"  # "vu", "python", "auto"

def is_admin():
    """检查是否以管理员权限运行"""
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except:
        return False

def load_config():
    """加载配置文件"""
    config_path = Path("config.json")
    default_config = {
        'target_window_title': None,
        'execution_mode': 'foreground_driver',
        'custom_width': 0,
        'custom_height': 0,
        'window_binding_mode': 'single',
        'bound_windows': [],
        'multi_window_delay': 500,
        'start_task_hotkey': 'F9',
        'stop_task_hotkey': 'F10',
        'record_hotkey': 'F12',
        'dual_execution_mode': 'auto',  # 双模式选择: vu/python/auto
        # BindWindowEx 高级绑定参数
        'bind_display': 'normal',
        'bind_mouse': 'normal',
        'bind_keypad': 'normal',
        'bind_public': '',
        'bind_mode_ex': 0,
        'bind_preset': 'FOREGROUND'  # 预设方案名称
    }
    
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                logger.info("配置文件加载成功")
                return {**default_config, **config}
        except Exception as e:
            logger.warning(f"加载配置文件失败: {e}，使用默认配置")
    
    return default_config

def save_config(config):
    """保存配置文件"""
    try:
        with open("config.json", 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        logger.info("配置文件保存成功")
    except Exception as e:
        logger.error(f"保存配置文件失败: {e}")

def load_task_modules():
    """加载任务模块"""
    try:
        from tasks import get_task_modules
        return get_task_modules()
    except Exception as e:
        logger.error(f"加载任务模块失败: {e}")
        return {}

def initialize_vu_plugin(config):
    """初始化并注册VU插件"""
    try:
        import struct
        from core.vu_wrapper import VUWrapper
        
        # 从配置文件读取注册码
        vu_reg = config.get('vu_registration', {})
        reg_code = vu_reg.get('reg_code', '')
        addon_code = vu_reg.get('addon_code', '')
        
        if not reg_code:
            logger.error("[FAIL] 配置文件中未找到VU注册码")
            return None
        
        # 根据Python位数自动选择DLL
        python_bits = struct.calcsize("P") * 8
        dll_name = 'vux64.dll' if python_bits == 64 else 'vu.dll'
        
        logger.info(f"正在初始化VU插件... (Python {python_bits}位, 使用 {dll_name})")
        vu_wrapper = VUWrapper(dll_name)
        
        if vu_wrapper.initialize():
            logger.info("VU插件初始化成功，正在注册...")
            ret = vu_wrapper.vu.Reg(reg_code, addon_code)
            
            if ret == 1:
                logger.info("[OK] VU插件注册成功")
                return vu_wrapper
            else:
                logger.error("[FAIL] VU插件注册失败")
                return None
        else:
            logger.error("[FAIL] VU插件初始化失败")
            return None
            
    except Exception as e:
        logger.error(f"[FAIL] VU插件初始化异常: {e}", exc_info=True)
        return None

def main():
    """主函数"""
    try:
        # 设置DPI感知级别（在创建QApplication之前）
        import os
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
        
        logger.info("=" * 80)
        logger.info("无忧自动化工具启动中...")
        logger.info("=" * 80)
        
        # 检查管理员权限
        if not is_admin():
            logger.warning("[WARN] 程序未以管理员权限运行，部分功能可能受限")
        else:
            logger.info("[OK] 程序已以管理员权限运行")
        
        # 加载配置
        config = load_config()
        
        # 初始化VU插件（可选）
        vu_wrapper = initialize_vu_plugin(config)
        if not vu_wrapper:
            logger.warning("[WARN] VU插件初始化失败，将使用Python模式运行")
            logger.info("[INFO] 程序将以有限功能模式启动（仅支持Python实现的功能）")
        else:
            # 设置全局VU实例
            from core.vu_wrapper import set_vu_wrapper
            from vu_global import init_vu_global
            set_vu_wrapper(vu_wrapper)
            init_vu_global(vu_wrapper)
            logger.info("[OK] VU插件已启用")
        
        # 加载任务模块
        task_modules = load_task_modules()
        
        # 设置图片目录
        images_dir = os.path.join(os.getcwd(), "images")
        os.makedirs(images_dir, exist_ok=True)
        
        # 导入并启动主窗口
        from PySide6.QtWidgets import QApplication
        from PySide6.QtCore import Qt
        from ui.main_window import MainWindow
        
        app = QApplication(sys.argv)
        app.setApplicationName("无忧自动化工具")
        
        # 创建主窗口，传递所有必需参数
        main_window = MainWindow(
            task_modules=task_modules,
            initial_config=config,
            hardware_id="VU_PLUGIN",  # 使用VU插件标识
            license_key="REGISTERED",  # 标记为已注册
            save_config_func=save_config,
            images_dir=images_dir,
            task_state_manager=None
        )
        
        # 初始化双模式管理器
        from core.dual_mode_manager import initialize_dual_mode, set_execution_mode
        
        if vu_wrapper:
            # 有VU插件时，初始化双模式
            if initialize_dual_mode(vu_wrapper):
                logger.info("[OK] 双模式系统初始化成功")
                # 从配置加载执行模式
                config_mode = config.get('dual_execution_mode', DEFAULT_MODE)
                set_execution_mode(config_mode)
                logger.info(f"[OK] 执行模式设置为: {config_mode}")
            else:
                logger.warning("[WARN] 双模式系统初始化失败，仅支持Python模式")
            
            # 将VU实例存储到主窗口（保持向后兼容）
            main_window.vu_wrapper = vu_wrapper
        else:
            # 没有VU插件时，强制使用Python模式
            set_execution_mode('python')
            logger.info("[INFO] 无VU插件，强制使用Python模式")
            main_window.vu_wrapper = None
        
        main_window.show()
        
        logger.info("[OK] 主窗口已启动")
        
        return app.exec()
        
    except Exception as e:
        logger.error(f"程序启动失败: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())