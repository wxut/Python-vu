# -*- coding: utf-8 -*-
"""
多窗口中控系统

支持多个窗口的并行/串行任务执行
"""

import threading
import time
from typing import Dict, Any, List, Callable

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from core.vu_wrapper import VUWrapper


class WindowInfo:
    """窗口信息类"""

    def __init__(self, hwnd, title="", wrapper=None):
        self.hwnd = hwnd
        self.title = title
        self.wrapper = wrapper
        self.status = 'idle'  # idle, running, error, stopped
        self.last_result = None
        self.last_error = None
        self.task_count = 0

    def __repr__(self):
        return f"WindowInfo(hwnd={self.hwnd}, title='{self.title}', status={self.status})"


class MultiWindowController:
    """多窗口中控系统

    功能：
    - 管理多个窗口的VU实例
    - 支持并行/串行任务执行
    - 提供窗口状态监控
    - 支持任务结果收集
    """

    def __init__(self):
        self.windows: Dict[int, WindowInfo] = {}
        self.active_window = None
        self.lock = threading.Lock()

    def add_window(self, hwnd, title="", bind_mode="normal"):
        """添加窗口到中控

        Args:
            hwnd: 窗口句柄
            title: 窗口标题
            bind_mode: 绑定模式

        Returns:
            bool: 成功返回True
        """
        with self.lock:
            if hwnd in self.windows:
                print(f"[多窗口中控] 窗口{hwnd}已存在")
                return False

            try:
                # 创建VU实例
                wrapper = VUWrapper()
                if not wrapper.initialize():
                    print(f"[多窗口中控] 初始化VU失败 (hwnd={hwnd})")
                    return False

                # 绑定窗口
                if not wrapper.bind_window(hwnd, bind_mode):
                    print(f"[多窗口中控] 绑定窗口失败 (hwnd={hwnd})")
                    wrapper.cleanup()
                    return False

                # 添加到管理列表
                window_info = WindowInfo(hwnd, title, wrapper)
                self.windows[hwnd] = window_info

                print(f"[多窗口中控] 添加窗口成功: {window_info}")
                return True

            except Exception as e:
                print(f"[多窗口中控] 添加窗口异常: {e}")
                import traceback
                traceback.print_exc()
                return False

    def remove_window(self, hwnd):
        """移除窗口"""
        with self.lock:
            if hwnd not in self.windows:
                return False

            try:
                window_info = self.windows[hwnd]
                if window_info.wrapper:
                    window_info.wrapper.cleanup()

                del self.windows[hwnd]
                print(f"[多窗口中控] 移除窗口: hwnd={hwnd}")
                return True

            except Exception as e:
                print(f"[多窗口中控] 移除窗口异常: {e}")
                return False

    def remove_all_windows(self):
        """移除所有窗口"""
        with self.lock:
            for hwnd in list(self.windows.keys()):
                self.remove_window(hwnd)

    def get_window(self, hwnd) -> WindowInfo:
        """获取窗口信息"""
        return self.windows.get(hwnd)

    def get_all_windows(self) -> List[WindowInfo]:
        """获取所有窗口"""
        return list(self.windows.values())

    def execute_task_on_window(self, hwnd, task_func: Callable, *args, **kwargs):
        """在指定窗口执行任务

        Args:
            hwnd: 窗口句柄
            task_func: 任务函数，接收VUWrapper作为第一个参数
            *args, **kwargs: 传递给任务函数的参数

        Returns:
            任务函数的返回值

        Example:
            def my_task(vu_wrapper, x, y):
                vu_mouse = VUMouse(vu_wrapper)
                vu_mouse.click_at(x, y)
                return True

            result = controller.execute_task_on_window(hwnd, my_task, 100, 200)
        """
        if hwnd not in self.windows:
            print(f"[多窗口中控] 窗口{hwnd}不存在")
            return None

        window_info = self.windows[hwnd]
        window_info.status = 'running'
        window_info.last_error = None

        try:
            result = task_func(window_info.wrapper, *args, **kwargs)
            window_info.status = 'idle'
            window_info.last_result = result
            window_info.task_count += 1
            return result

        except Exception as e:
            window_info.status = 'error'
            window_info.last_error = str(e)
            print(f"[多窗口中控] 任务执行异常 (hwnd={hwnd}): {e}")
            import traceback
            traceback.print_exc()
            return None

    def execute_task_on_all_windows(self, task_func: Callable, parallel=True, *args, **kwargs):
        """在所有窗口执行任务

        Args:
            task_func: 任务函数
            parallel: True=并行执行，False=串行执行
            *args, **kwargs: 传递给任务函数的参数

        Returns:
            dict: {hwnd: result}
        """
        results = {}

        if parallel:
            # 并行执行
            threads = []

            def run_task(hwnd):
                results[hwnd] = self.execute_task_on_window(hwnd, task_func, *args, **kwargs)

            for hwnd in self.windows:
                t = threading.Thread(target=run_task, args=(hwnd,))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

        else:
            # 串行执行
            for hwnd in self.windows:
                results[hwnd] = self.execute_task_on_window(hwnd, task_func, *args, **kwargs)

        return results

    def get_window_status(self, hwnd):
        """获取窗口状态"""
        if hwnd in self.windows:
            return self.windows[hwnd].status
        return None

    def get_all_status(self):
        """获取所有窗口状态"""
        return {hwnd: info.status for hwnd, info in self.windows.items()}

    def wait_all_idle(self, timeout=30):
        """等待所有窗口空闲"""
        start_time = time.time()

        while time.time() - start_time < timeout:
            all_idle = all(info.status == 'idle' for info in self.windows.values())
            if all_idle:
                return True
            time.sleep(0.1)

        return False

    def get_statistics(self):
        """获取统计信息"""
        return {
            'total_windows': len(self.windows),
            'idle_windows': sum(1 for info in self.windows.values() if info.status == 'idle'),
            'running_windows': sum(1 for info in self.windows.values() if info.status == 'running'),
            'error_windows': sum(1 for info in self.windows.values() if info.status == 'error'),
            'total_tasks': sum(info.task_count for info in self.windows.values())
        }

    def cleanup(self):
        """清理所有资源"""
        self.remove_all_windows()


# 使用示例
if __name__ == "__main__":
    from core.vu_mouse import VUMouse
    from core.vu_image import VUImage

    # 创建多窗口中控
    controller = MultiWindowController()

    # 定义任务函数
    def click_task(vu_wrapper, x, y):
        """点击任务"""
        mouse = VUMouse(vu_wrapper)
        mouse.click_at(x, y)
        return True

    def find_image_task(vu_wrapper, pic_name):
        """找图任务"""
        image = VUImage(vu_wrapper)
        pos = image.find_pic(pic_name)
        if pos:
            mouse = VUMouse(vu_wrapper)
            mouse.click_at(*pos)
            return True
        return False

    # 添加窗口（假设窗口句柄）
    # controller.add_window(123456, "窗口1")
    # controller.add_window(789012, "窗口2")

    # 并行执行任务
    # results = controller.execute_task_on_all_windows(click_task, parallel=True, x=100, y=200)
    # print(f"并行执行结果: {results}")

    # 串行执行任务
    # results = controller.execute_task_on_all_windows(find_image_task, parallel=False, pic_name="button.bmp")
    # print(f"串行执行结果: {results}")

    # 获取统计信息
    # stats = controller.get_statistics()
    # print(f"统计信息: {stats}")

    # 清理
    controller.cleanup()
