# -*- coding: utf-8 -*-
"""
VU输入适配器

提供TM兼容的鼠标键盘输入接口,底层使用VU插件实现
核心原则: 接口与TM的输入模拟保持一致,内部调用VU的鼠标键盘函数
"""

import logging
import time
from typing import Optional, List

logger = logging.getLogger(__name__)


class VUInputAdapter:
    """VU输入适配器 - 提供TM兼容的鼠标键盘接口"""

    def __init__(self, vu_wrapper):
        """
        初始化输入适配器

        Args:
            vu_wrapper: VUWrapper实例
        """
        self.vu_wrapper = vu_wrapper

        # 导入VU鼠标和键盘操作类
        from core.vu_mouse import VUMouse
        from core.vu_keyboard import VUKeyboard

        self.vu_mouse = VUMouse(vu_wrapper)
        self.vu_keyboard = VUKeyboard(vu_wrapper)

        logger.info("VU输入适配器初始化")

    # ==================== 鼠标操作 ====================

    def mouse_move(self, x: int, y: int) -> bool:
        """
        移动鼠标(TM兼容接口)

        Args:
            x: X坐标
            y: Y坐标

        Returns:
            bool: 成功返回True

        Example:
            adapter.mouse_move(100, 200)
        """
        try:
            result = self.vu_mouse.move_to(x, y)
            logger.debug(f"移动鼠标到: ({x}, {y}), 结果:{result}")
            return result

        except Exception as e:
            logger.error(f"移动鼠标失败: {e}")
            return False

    def mouse_click(self, x: int, y: int, button: str = "left",
                   click_count: int = 1, interval: float = 0.1) -> bool:
        """
        鼠标点击(TM兼容接口)

        与TM的mouse_click接口保持一致

        Args:
            x: X坐标
            y: Y坐标
            button: 按钮类型 "left", "right", "middle"
            click_count: 点击次数
            interval: 点击间隔(秒)

        Returns:
            bool: 成功返回True

        Example:
            # 左键单击
            adapter.mouse_click(100, 200)
            # 右键单击
            adapter.mouse_click(100, 200, button="right")
            # 左键双击
            adapter.mouse_click(100, 200, click_count=2)
        """
        try:
            logger.debug(
                f"鼠标点击: ({x}, {y}), 按钮:{button}, "
                f"次数:{click_count}, 间隔:{interval}"
            )

            # 先移动到目标位置
            self.vu_mouse.move_to(x, y)
            time.sleep(0.05)  # 短暂延迟

            # 根据按钮类型和次数执行点击
            for i in range(click_count):
                if button == "left":
                    result = self.vu_mouse.left_click()
                elif button == "right":
                    result = self.vu_mouse.right_click()
                elif button == "middle":
                    result = self.vu_mouse.middle_click()
                else:
                    logger.warning(f"未知按钮类型: {button}")
                    return False

                if not result:
                    logger.error(f"点击失败: 第{i+1}次")
                    return False

                # 多次点击时添加间隔
                if i < click_count - 1:
                    time.sleep(interval)

            logger.debug("点击成功")
            return True

        except Exception as e:
            logger.error(f"鼠标点击失败: {e}")
            return False

    def mouse_down(self, button: str = "left") -> bool:
        """
        按下鼠标按钮(TM兼容接口)

        Args:
            button: 按钮类型 "left", "right", "middle"

        Returns:
            bool: 成功返回True
        """
        try:
            if button == "left":
                result = self.vu_mouse.left_down()
            elif button == "right":
                result = self.vu_mouse.right_down()
            else:
                logger.warning(f"按下操作不支持: {button}")
                return False

            logger.debug(f"按下鼠标: {button}, 结果:{result}")
            return result

        except Exception as e:
            logger.error(f"按下鼠标失败: {e}")
            return False

    def mouse_up(self, button: str = "left") -> bool:
        """
        释放鼠标按钮(TM兼容接口)

        Args:
            button: 按钮类型 "left", "right", "middle"

        Returns:
            bool: 成功返回True
        """
        try:
            if button == "left":
                result = self.vu_mouse.left_up()
            elif button == "right":
                result = self.vu_mouse.right_up()
            else:
                logger.warning(f"释放操作不支持: {button}")
                return False

            logger.debug(f"释放鼠标: {button}, 结果:{result}")
            return result

        except Exception as e:
            logger.error(f"释放鼠标失败: {e}")
            return False

    def mouse_drag(self, x1: int, y1: int, x2: int, y2: int,
                  duration: float = 0.5, button: str = "left") -> bool:
        """
        鼠标拖拽(TM兼容接口)

        Args:
            x1, y1: 起始坐标
            x2, y2: 结束坐标
            duration: 拖拽持续时间(秒)
            button: 按钮类型

        Returns:
            bool: 成功返回True

        Example:
            adapter.mouse_drag(100, 100, 300, 300, duration=1.0)
        """
        try:
            logger.debug(
                f"鼠标拖拽: ({x1}, {y1}) -> ({x2}, {y2}), "
                f"持续:{duration}秒"
            )

            # 移动到起始位置
            self.vu_mouse.move_to(x1, y1)
            time.sleep(0.1)

            # 按下鼠标
            self.mouse_down(button)
            time.sleep(0.1)

            # 移动到结束位置
            self.vu_mouse.move_to(x2, y2)
            time.sleep(duration)

            # 释放鼠标
            self.mouse_up(button)

            logger.debug("拖拽成功")
            return True

        except Exception as e:
            logger.error(f"鼠标拖拽失败: {e}")
            return False

    def mouse_scroll(self, clicks: int, x: Optional[int] = None,
                    y: Optional[int] = None) -> bool:
        """
        鼠标滚轮(TM兼容接口)

        Args:
            clicks: 滚动量,正数向上,负数向下
            x, y: 滚动位置,None表示当前位置

        Returns:
            bool: 成功返回True

        Example:
            adapter.mouse_scroll(3)  # 向上滚动3格
            adapter.mouse_scroll(-3)  # 向下滚动3格
        """
        try:
            # 如果指定了位置,先移动
            if x is not None and y is not None:
                self.vu_mouse.move_to(x, y)
                time.sleep(0.05)

            result = self.vu_mouse.wheel(clicks)
            logger.debug(f"滚轮滚动: {clicks}, 结果:{result}")
            return result

        except Exception as e:
            logger.error(f"滚轮滚动失败: {e}")
            return False

    # ==================== 键盘操作 ====================

    def keyboard_press(self, key: str, press_count: int = 1,
                      interval: float = 0.1) -> bool:
        """
        按键(TM兼容接口)

        Args:
            key: 按键名称,支持VU的按键码
            press_count: 按键次数
            interval: 按键间隔(秒)

        Returns:
            bool: 成功返回True

        Example:
            adapter.keyboard_press("A")  # 按A键
            adapter.keyboard_press("13")  # 按回车键(键码13)
            adapter.keyboard_press("A", press_count=3)  # 按3次A键
        """
        try:
            logger.debug(
                f"按键: {key}, 次数:{press_count}, 间隔:{interval}"
            )

            for i in range(press_count):
                result = self.vu_keyboard.key_press(key)

                if not result:
                    logger.error(f"按键失败: 第{i+1}次")
                    return False

                # 多次按键时添加间隔
                if i < press_count - 1:
                    time.sleep(interval)

            logger.debug("按键成功")
            return True

        except Exception as e:
            logger.error(f"按键失败: {e}")
            return False

    def keyboard_down(self, key: str) -> bool:
        """
        按下按键(TM兼容接口)

        Args:
            key: 按键名称

        Returns:
            bool: 成功返回True
        """
        try:
            result = self.vu_keyboard.key_down(key)
            logger.debug(f"按下按键: {key}, 结果:{result}")
            return result

        except Exception as e:
            logger.error(f"按下按键失败: {e}")
            return False

    def keyboard_up(self, key: str) -> bool:
        """
        释放按键(TM兼容接口)

        Args:
            key: 按键名称

        Returns:
            bool: 成功返回True
        """
        try:
            result = self.vu_keyboard.key_up(key)
            logger.debug(f"释放按键: {key}, 结果:{result}")
            return result

        except Exception as e:
            logger.error(f"释放按键失败: {e}")
            return False

    def keyboard_type(self, text: str, interval: float = 0.05) -> bool:
        """
        输入文本(TM兼容接口)

        Args:
            text: 要输入的文本
            interval: 字符间隔(秒)

        Returns:
            bool: 成功返回True

        Example:
            adapter.keyboard_type("Hello World")
        """
        try:
            logger.debug(f"输入文本: {text}, 间隔:{interval}")

            # 逐字符输入
            for char in text:
                result = self.vu_keyboard.send_string(char)

                if not result:
                    logger.error(f"输入字符失败: {char}")
                    return False

                time.sleep(interval)

            logger.debug("输入文本成功")
            return True

        except Exception as e:
            logger.error(f"输入文本失败: {e}")
            return False

    def keyboard_hotkey(self, *keys: str) -> bool:
        """
        组合键(TM兼容接口)

        Args:
            *keys: 按键序列

        Returns:
            bool: 成功返回True

        Example:
            adapter.keyboard_hotkey("ctrl", "c")  # Ctrl+C
            adapter.keyboard_hotkey("ctrl", "shift", "esc")  # Ctrl+Shift+Esc
        """
        try:
            logger.debug(f"组合键: {'+'.join(keys)}")

            # 依次按下所有键
            for key in keys:
                self.keyboard_down(key)
                time.sleep(0.05)

            time.sleep(0.1)

            # 依次释放所有键(逆序)
            for key in reversed(keys):
                self.keyboard_up(key)
                time.sleep(0.05)

            logger.debug("组合键成功")
            return True

        except Exception as e:
            logger.error(f"组合键失败: {e}")
            return False


# 导出类
__all__ = ['VUInputAdapter']
