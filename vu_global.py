# -*- coding: utf-8 -*-
"""
VU全局实例管理模块

提供全局VU实例访问,用于向后兼容旧的任务模块
"""

import logging

logger = logging.getLogger(__name__)

# 全局VU实例
_global_vu = None
_global_vu_wrapper = None


def init_vu_global(vu_wrapper):
    """
    初始化全局VU实例
    
    Args:
        vu_wrapper: VUWrapper实例
    """
    global _global_vu, _global_vu_wrapper
    _global_vu_wrapper = vu_wrapper
    if vu_wrapper and vu_wrapper.vu:
        _global_vu = vu_wrapper.vu
        logger.info("全局VU实例已初始化")
    else:
        logger.warning("VU实例初始化失败")


def get_vu():
    """
    获取全局VU实例
    
    Returns:
        VU实例,如果未初始化则返回None
    """
    return _global_vu


def get_vu_wrapper():
    """
    获取全局VUWrapper实例
    
    Returns:
        VUWrapper实例,如果未初始化则返回None
    """
    return _global_vu_wrapper


# 为了向后兼容,导出vu对象
vu = property(lambda self: get_vu())


class VUGlobal:
    """VU全局访问类,提供属性访问"""
    
    @property
    def vu(self):
        """获取VU实例"""
        return get_vu()
    
    def __getattr__(self, name):
        """代理所有属性访问到VU实例"""
        vu_instance = get_vu()
        if vu_instance:
            return getattr(vu_instance, name)
        raise AttributeError(f"VU实例未初始化,无法访问属性: {name}")


# 创建全局实例供导入使用
vu = VUGlobal()


__all__ = ['vu', 'init_vu_global', 'get_vu', 'get_vu_wrapper', 'VUGlobal']
