# -*- coding: utf-8 -*-
"""
VU配置管理

统一管理VU插件的配置
"""

import os
import json
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class VUConfig:
    """VU配置

    统一管理VU插件的所有配置项
    """

    # ==================== DLL配置 ====================
    dll_path: str = 'vux64.dll'
    """VU DLL文件路径"""

    dll_dir: Optional[str] = None
    """DLL所在目录,None表示当前目录"""

    # ==================== 绑定配置 ====================
    # BindWindow 简单绑定模式（向后兼容）
    bind_mode: str = 'normal'
    """窗口绑定模式: normal, dx, dx2, dx3, gdi, gdi2, ..."""

    # BindWindowEx 高级绑定参数
    bind_display: str = 'normal'
    """屏幕颜色获取方式: normal(前台截屏), gdi(GDI模式), dx(DirectX模式)"""

    bind_mouse: str = 'normal'
    """鼠标仿真模式: normal(前台), windows(Windows消息), dx.state|dx.raw|dx.input|dx.position|dx.focus(DX组合)"""

    bind_keypad: str = 'normal'
    """键盘仿真模式: normal(前台), windows(Windows消息), dx.state|dx.raw|dx.input(DX组合)"""

    bind_public: str = ''
    """公共属性: public.hide.dll(隐藏VU插件), public.memory.drv(内核方式执行内存操作), 多个用|连接"""

    bind_mode_ex: int = 0
    """绑定模式: 0(推荐,后台效果最好), 1(驱动级后台键鼠), 2(VT模式后台键鼠,仅Intel)"""

    bind_preset: str = 'FOREGROUND'
    """预设绑定方案: FOREGROUND, BACKGROUND_BASIC, BACKGROUND_DX, BACKGROUND_DX_FULL, DRIVER_HIDDEN, DRIVER_FULL, VT_MODE, custom"""

    # ==================== 截图配置 ====================
    screenshot_format: str = 'bmp'
    """截图格式: bmp, jpg, png"""

    screenshot_quality: int = 100
    """截图质量 (1-100)"""

    screenshot_cache_enabled: bool = False
    """是否启用截图缓存"""

    # ==================== OCR配置 ====================
    ocr_dict: str = 'default'
    """OCR字典: default, 或自定义字典路径"""

    ocr_similarity: float = 0.9
    """OCR默认相似度 (0.0-1.0)"""

    ocr_color_format: str = "FFFFFF-000000"
    """OCR默认颜色格式: 前景色-背景色"""

    # ==================== 图像识别配置 ====================
    image_similarity: float = 0.9
    """图像识别默认相似度 (0.0-1.0)"""

    image_delta_color: str = "000000"
    """图像识别默认颜色偏差"""

    image_find_type: int = 0
    """图像查找类型: 0-从左到右从上到下, 1-从左到右从下到上, ..."""

    # ==================== 颜色识别配置 ====================
    color_similarity: float = 0.9
    """颜色识别默认相似度 (0.0-1.0)"""

    color_find_type: int = 0
    """颜色查找类型"""

    # ==================== 输入配置 ====================
    mouse_delay: int = 30
    """鼠标操作延迟(毫秒)"""

    keypad_delay: int = 30
    """键盘操作延迟(毫秒)"""

    input_timeout: int = 5000
    """输入操作超时(毫秒)"""

    # ==================== 执行模式配置 ====================
    execution_mode: str = 'auto'
    """执行模式: vu(强制VU插件), python(强制Python), auto(自动选择,VU优先)"""

    # ==================== 性能配置 ====================
    cache_enabled: bool = True
    """是否启用缓存"""

    cache_size: int = 100
    """缓存大小"""

    thread_pool_size: int = 4
    """线程池大小"""

    # ==================== 日志配置 ====================
    log_level: str = 'INFO'
    """日志级别: DEBUG, INFO, WARNING, ERROR"""

    log_to_file: bool = False
    """是否记录到文件"""

    log_file_path: str = 'wy.log'
    """日志文件路径"""

    # ==================== 调试配置 ====================
    debug_mode: bool = False
    """调试模式"""

    verbose: bool = False
    """详细输出"""

    @classmethod
    def from_file(cls, config_file: str) -> 'VUConfig':
        """从配置文件加载

        Args:
            config_file: 配置文件路径(JSON格式)

        Returns:
            VUConfig: 配置对象

        Example:
            config = VUConfig.from_file('vu_config.json')
        """
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return cls(**data)
        except FileNotFoundError:
            # 文件不存在,返回默认配置
            return cls()
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            return cls()

    def to_file(self, config_file: str):
        """保存到配置文件

        Args:
            config_file: 配置文件路径(JSON格式)

        Example:
            config.to_file('vu_config.json')
        """
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(asdict(self), f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存配置文件失败: {e}")

    def update(self, **kwargs):
        """更新配置

        Args:
            **kwargs: 要更新的配置项

        Example:
            config.update(image_similarity=0.95, ocr_similarity=0.9)
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"警告: 未知的配置项 '{key}'")

    def reset_to_default(self):
        """重置为默认配置"""
        default = VUConfig()
        for key in asdict(default).keys():
            setattr(self, key, getattr(default, key))

    def get_dll_full_path(self) -> str:
        """获取DLL完整路径

        Returns:
            str: DLL完整路径
        """
        if self.dll_dir:
            return os.path.join(self.dll_dir, self.dll_path)
        return self.dll_path

    def validate(self) -> bool:
        """验证配置有效性

        Returns:
            bool: 配置是否有效
        """
        # 检查相似度范围
        if not (0.0 <= self.image_similarity <= 1.0):
            print("错误: image_similarity必须在0.0-1.0之间")
            return False

        if not (0.0 <= self.ocr_similarity <= 1.0):
            print("错误: ocr_similarity必须在0.0-1.0之间")
            return False

        if not (0.0 <= self.color_similarity <= 1.0):
            print("错误: color_similarity必须在0.0-1.0之间")
            return False

        # 检查质量范围
        if not (1 <= self.screenshot_quality <= 100):
            print("错误: screenshot_quality必须在1-100之间")
            return False

        return True

    def __str__(self) -> str:
        """字符串表示"""
        lines = ["VUConfig:"]
        for key, value in asdict(self).items():
            lines.append(f"  {key}: {value}")
        return "\n".join(lines)


# 全局默认配置实例
DEFAULT_CONFIG = VUConfig()


# 导出
__all__ = ['VUConfig', 'DEFAULT_CONFIG']


# ==================== 预设绑定方案 ====================

class VUBindPresets:
    """VU插件预设绑定方案
    
    提供常用的窗口绑定配置预设，方便快速配置
    """
    
    # 前台模式（默认）
    FOREGROUND = {
        'display': 'normal',
        'mouse': 'normal',
        'keypad': 'normal',
        'public': '',
        'mode': 0,
        'description': '前台模式 - 适用于前台操作，兼容性最好'
    }
    
    # 后台模式（基础）
    BACKGROUND_BASIC = {
        'display': 'gdi',
        'mouse': 'windows',
        'keypad': 'windows',
        'public': '',
        'mode': 0,
        'description': '后台模式（基础） - 使用GDI和Windows消息，适用于大多数窗口'
    }
    
    # 后台模式（DirectX）
    BACKGROUND_DX = {
        'display': 'dx',
        'mouse': 'dx.state|dx.input',
        'keypad': 'dx.state|dx.input',
        'public': '',
        'mode': 0,
        'description': '后台模式（DirectX） - 使用DirectX模式，兼容性较强'
    }
    
    # 后台模式（完整DX）
    BACKGROUND_DX_FULL = {
        'display': 'dx',
        'mouse': 'dx.state|dx.raw|dx.input|dx.position|dx.focus',
        'keypad': 'dx.state|dx.raw|dx.input',
        'public': '',
        'mode': 0,
        'description': '后台模式（完整DX） - 使用完整DirectX功能，后台效果最好'
    }
    
    # 驱动级后台（隐藏DLL）
    DRIVER_HIDDEN = {
        'display': 'dx',
        'mouse': 'dx.state|dx.raw|dx.input|dx.position|dx.focus',
        'keypad': 'dx.state|dx.raw|dx.input',
        'public': 'public.hide.dll',
        'mode': 1,
        'description': '驱动级后台（隐藏DLL） - 使用驱动级键鼠，隐藏VU插件，避免检测'
    }
    
    # 驱动级后台（完整形态）
    DRIVER_FULL = {
        'display': 'dx',
        'mouse': 'dx.state|dx.raw|dx.input|dx.position|dx.focus',
        'keypad': 'dx.state|dx.raw|dx.input',
        'public': 'public.hide.dll|public.memory.drv',
        'mode': 1,
        'description': '驱动级后台（完整形态） - 使用驱动级键鼠和内存操作，最强后台能力'
    }
    
    # VT模式后台（Intel处理器）
    VT_MODE = {
        'display': 'dx',
        'mouse': 'dx.state|dx.raw|dx.input|dx.position|dx.focus',
        'keypad': 'dx.state|dx.raw|dx.input',
        'public': 'public.hide.dll|public.memory.drv',
        'mode': 2,
        'description': 'VT模式后台 - 强制使用VT模式，仅限Intel处理器'
    }
    
    @classmethod
    def get_preset(cls, name: str) -> dict:
        """获取预设方案
        
        Args:
            name: 预设名称（FOREGROUND, BACKGROUND_BASIC, BACKGROUND_DX, 
                  BACKGROUND_DX_FULL, DRIVER_HIDDEN, DRIVER_FULL, VT_MODE）
        
        Returns:
            dict: 预设配置字典
        
        Example:
            preset = VUBindPresets.get_preset('BACKGROUND_DX_FULL')
            vu.bind_window_ex(hwnd, **preset)
        """
        return getattr(cls, name, cls.FOREGROUND).copy()
    
    @classmethod
    def list_presets(cls) -> list:
        """列出所有可用的预设方案
        
        Returns:
            list: 预设名称和描述的列表
        
        Example:
            for name, desc in VUBindPresets.list_presets():
                print(f"{name}: {desc}")
        """
        presets = []
        for attr_name in dir(cls):
            if attr_name.isupper() and not attr_name.startswith('_'):
                preset = getattr(cls, attr_name)
                if isinstance(preset, dict) and 'description' in preset:
                    presets.append((attr_name, preset['description']))
        return presets


# 导出
__all__ = ['VUConfig', 'DEFAULT_CONFIG', 'VUBindPresets']
