# -*- coding: utf-8 -*-
"""
VU插件 Python 完整调用库 v2.0
这是一套优秀的stdcall调用框架
本套代码的主要功能是使python更容易调用stdcall的标准插件接口
具有接口代码容易编写,执行效率基本不受影响的特点.
这套代码的核心思想是将c语言的数据类型与python的基本数据类型能够智能转换
在调用c语言的函数时,将python的基本数据类型转换为c语言的数据类型
在接收c语言的返回值时,将c语言的数据类型转换为python的基本数据类型
无忧开发组将其应用于多个项目,并经过了多年的验证,稳定性非常好
现将这套代码开源,希望能够帮助到更多的人
我们的官方网址:http://www.voouer.com
作者: 大大大大大师
联系方式:QQ7891634
完整实现: Claude 4.0 Sonnet
日期: 2025年11月10日
版本: v2.0 - 优化版，包含详细文档和示例
"""

import ctypes
import os
import functools
from pathlib import Path
from typing import Any, Tuple, Optional


def convert_arg(arg, arg_type, encoding='gbk'):
    """将Python参数转换为ctypes类型"""
    # 检查是否为POINTER类型 (如 POINTER(c_long))
    # 注意: c_void_p也有_type_属性,但它的_type_是字符串'P',而POINTER的_type_是类型
    if hasattr(arg_type, '_type_') and isinstance(arg_type._type_, type):  # 是真正的POINTER类型
        # 如果参数已经是指针类型,直接返回
        if isinstance(arg, ctypes._Pointer):
            return arg
        # 如果参数是ctypes变量(如 c_long(0)),使用byref返回其指针
        if isinstance(arg, ctypes._SimpleCData):
            return ctypes.byref(arg)
        # 如果是Python原生类型,先创建ctypes变量,再返回其指针
        base_type = arg_type._type_
        c_var = base_type(arg)
        return ctypes.byref(c_var)

    # 如果已经是ctypes类型（非POINTER），直接返回
    if isinstance(arg, ctypes._SimpleCData):
        return arg

    # 根据目标类型进行转换
    if arg_type == ctypes.c_char_p:
        # 字符串转换为bytes
        if isinstance(arg, str):
            return ctypes.c_char_p(arg.encode(encoding))
        elif isinstance(arg, bytes):
            return arg
        else:
            return ctypes.c_char_p(str(arg).encode(encoding))

    elif arg_type == ctypes.c_wchar_p:
        # 字符串转换为unicode
        if isinstance(arg, str):
            return ctypes.c_wchar_p(arg)
        else:
            return ctypes.c_wchar_p(str(arg))

    elif arg_type == ctypes.c_int:
        return ctypes.c_int(arg)

    elif arg_type == ctypes.c_long:
        return ctypes.c_long(arg)

    elif arg_type == ctypes.c_longlong:
        return ctypes.c_longlong(arg)

    elif arg_type == ctypes.c_void_p:
        # 处理指针类型
        if isinstance(arg, int):
            return ctypes.c_void_p(arg)
        elif hasattr(arg, 'value'):
            return ctypes.c_void_p(arg.value)
        else:
            return ctypes.c_void_p(arg)

    elif arg_type == ctypes.c_float:
        return ctypes.c_float(arg)

    elif arg_type == ctypes.c_double:
        return ctypes.c_double(arg)

    elif arg_type == ctypes.c_bool:
        return ctypes.c_bool(arg)

    elif arg_type == ctypes.c_uint:
        return ctypes.c_uint(arg)

    elif arg_type == ctypes.c_ulong:
        return ctypes.c_ulong(arg)

    elif arg_type == ctypes.c_ulonglong:
        return ctypes.c_ulonglong(arg)

    elif arg_type == ctypes.c_byte:
        return ctypes.c_byte(arg)

    elif arg_type == ctypes.c_ubyte:
        return ctypes.c_ubyte(arg)

    elif arg_type == ctypes.c_short:
        return ctypes.c_short(arg)

    elif arg_type == ctypes.c_ushort:
        return ctypes.c_ushort(arg)

    # 默认返回参数本身
    return arg


def convert_res(value, value_type, encoding='utf-8'):
    """将ctypes值转换为Python基本类型"""
    # 如果已经是Python基本类型，直接返回
    if isinstance(value, (int, float, bool, str, complex, list, tuple, dict, set, frozenset, bytearray, memoryview)):
        return value

    # 如果value是None，直接返回
    if value is None:
        return None

    # 根据类型进行转换
    if value_type == ctypes.c_char_p:
        # c_char_p 返回的是 bytes，需要解码
        if value is not None:
            try:
                return value.decode(encoding)
            except:
                return value.decode('gbk')
        return None

    elif value_type == ctypes.c_wchar_p:
        # c_wchar_p 返回的是 str
        return str(value) if value else None

    elif value_type == ctypes.c_void_p:
        # c_void_p 返回的是整数地址
        return value if isinstance(value, int) else (value.value if value else None)

    elif hasattr(value, 'value'):
        # 其他有value属性的ctypes类型
        return value.value

    # 对于其他情况，直接返回值
    return value


def call_dll_func(self: "vusoft", dll_func, israw, *args: tuple):
    """调用DLL函数"""
    if not israw:
        args = (self.m_obj,) + args

    # 将参数转换为ctypes类型
    ctypes_args = [convert_arg(arg, arg_type, encoding='gbk') for arg, arg_type in zip(args, dll_func.argtypes)]
    ctypes_args = tuple(ctypes_args)

    # 调用DLL函数
    res = dll_func(*ctypes_args)
    # 将返回值转换为Python类型
    ret = convert_res(res, dll_func.restype, encoding='utf-8')
    return ret


def cls_function(israw=False, restype=None, arg_types: list = []):
    """DLL函数调用装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self: "vusoft", *args: tuple):
            # 获取DLL函数
            dll_func = self.m_funcs.get(func.__name__, None)
            if dll_func:
                return call_dll_func(self, dll_func, israw, *args)

            # 静态函数不加Obj前缀
            if israw:
                dll_func = getattr(self.dll, func.__name__)
            else:
                dll_func = getattr(self.dll, "Obj" + func.__name__)

            # 设置返回值类型
            if restype:
                dll_func.restype = restype
            # 设置参数类型
            if israw:
                dll_func.argtypes = arg_types
                # 保存函数到字典
                self.m_funcs[func.__name__] = dll_func
                # 调用函数
                return call_dll_func(self, dll_func, israw, *args)
            elif arg_types:
                dll_func.argtypes = [ctypes.c_void_p] + arg_types
            else:
                dll_func.argtypes = [ctypes.c_void_p]
            # 保存函数到字典
            self.m_funcs[func.__name__] = dll_func
            # 调用函数
            return call_dll_func(self, dll_func, israw, *args)
        return wrapper
    return decorator


class vusoft:
    """VU插件Python调用类

    这是VU插件的主要接口类，封装了所有插件功能。

    使用步骤:
        1. 创建vusoft对象: vu = vusoft('vux64.dll')
        2. 创建VU对象: vu.Create()
        3. (可选)注册插件: vu.Reg(reg_code, "")
        4. 调用各种功能函数
        5. 清理资源: vu.Delete()

    Example:
        ```python
        from vusoftmax import vusoft
        import ctypes

        # 初始化
        vu = vusoft('vux64.dll')
        vu.Create()

        # 使用功能
        version = vu.Ver()
        print(f"版本: {version}")

        # 清理
        vu.Delete()
        ```
    """

    def __init__(self, dll_path):
        """初始化VU插件

        Args:
            dll_path: vux64.dll的路径(支持相对路径和绝对路径)
        """
        # 转换为绝对路径以避免加载问题
        if not os.path.isabs(dll_path):
            dll_path = str(Path(dll_path).resolve())

        self.dll = ctypes.WinDLL(dll_path)
        self.m_obj = ctypes.c_void_p(0)
        self.m_funcs = {}

    def Create(self) -> int:
        """创建VU对象

        Returns:
            对象句柄（整数）

        Example:
            ```python
            obj = vu.Create()
            print(f"对象句柄: {obj}")
            ```
        """
        if self.m_obj.value:  # 检查value而不是对象本身
            return self.m_obj.value
        self.dll.ObjCreate.restype = ctypes.c_void_p
        self.dll.ObjCreate.argtypes = [ctypes.c_void_p]
        obj_handle = self.dll.ObjCreate(self.m_obj)
        self.m_obj = ctypes.c_void_p(obj_handle)  # 正确地创建c_void_p对象
        return self.m_obj.value

    def Delete(self) -> int:
        """删除VU对象，释放资源

        Returns:
            1表示成功

        Example:
            ```python
            vu.Delete()
            ```
        """
        if not self.m_obj:
            return 0

        self.dll.ObjDelete.restype = ctypes.c_longlong
        self.dll.ObjDelete.argtypes = [ctypes.c_void_p]
        res: ctypes.c_longlong = self.dll.ObjDelete(self.m_obj)
        self.m_obj = ctypes.c_void_p(0)
        return convert_res(res, ctypes.c_longlong)

    # ==================== 插件功能函数 ====================

    # ==================== 基础功能 ====================

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def Ver(self):
        """获取插件版本号

        Returns:
            版本号字符串，如 "10.251025"

        Example:
            # 获取版本号
            version = vu.Ver()
            print(f"VU插件版本: {version}")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def Reg(self, reg_code, ver_info):
        """注册插件

        Args:
            reg_code: 注册码字符串
            ver_info: 版本信息（通常传空字符串""）

        Returns:
            1表示成功，0表示失败

        Example:
            # 注册插件
            reg_code = "YOUR_REG_CODE"
            ret = vu.Reg(reg_code, "")
            if ret == 1:
                print("注册成功")
            else:
                print("注册失败")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def RegUrl(self, server_url):
        """RegUrl函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetID(self):
        """GetID函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def SetPath(self, path):
        """SetPath函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetPath(self):
        """GetPath函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetLastError(self):
        """GetLastError函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_longlong, ctypes.c_long])
    def Crypt(self, mode, key, data, in_out_Len):
        """Crypt函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def SetDisplayInput(self, mode):
        """SetDisplayInput函数
        """
        pass

    # ==================== 窗口绑定 ====================

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def BindWindowEx(self, hwnd, display, mouse, keypad, _public, mode):
        """BindWindowEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def UnBindWindow(self):
        """UnBindWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetBindWindow(self):
        """GetBindWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def IsBind(self, hwnd):
        """IsBind函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SwitchBindWindow(self, hwnd):
        """SwitchBindWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def LockInput(self, lock):
        """LockInput函数
        """
        pass

    # ==================== 鼠标操作 ====================

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def EnableRealMouse(self, enable, mousedelay, mousestep):
        """EnableRealMouse函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetCursorPos(self, x, y):
        """获取鼠标当前坐标

        Args:
            x: ctypes.c_long对象，用于接收X坐标
            y: ctypes.c_long对象，用于接收Y坐标

        Returns:
            1表示成功，0表示失败

        Example:
            # 获取鼠标位置
            x = ctypes.c_long(0)
            y = ctypes.c_long(0)
            ret = vu.GetCursorPos(x, y)
            if ret:
                print(f"鼠标位置: ({x.value}, {y.value})")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetCursorSpot(self, x, y):
        """GetCursorSpot函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetCursorShape(self):
        """GetCursorShape函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def LeftClick(self):
        """鼠标左键单击

        Returns:
            1表示成功，0表示失败

        Example:
            # 左键单击
            vu.LeftClick()
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def LeftDoubleClick(self):
        """LeftDoubleClick函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def LeftDown(self):
        """LeftDown函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def LeftUp(self):
        """LeftUp函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def MiddleClick(self):
        """MiddleClick函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def MiddleDown(self):
        """MiddleDown函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def MiddleUp(self):
        """MiddleUp函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def RightClick(self):
        """RightClick函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def RightDown(self):
        """RightDown函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def RightUp(self):
        """RightUp函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def WheelDown(self):
        """WheelDown函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def WheelUp(self):
        """WheelUp函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def MoveR(self, rx, ry):
        """MoveR函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def MoveTo(self, x, y):
        """移动鼠标到指定坐标

        Args:
            x: X坐标
            y: Y坐标

        Returns:
            1表示成功，0表示失败

        Example:
            # 移动鼠标到(100, 200)
            ret = vu.MoveTo(100, 200)
            if ret:
                print("鼠标已移动")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long])
    def MoveToEx(self, x, y, w, h):
        """MoveToEx函数
        """
        pass

    # ==================== 键盘操作 ====================

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def GetKeyState(self, vk_code):
        """GetKeyState函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def WaitKey(self, vk_code, time_out):
        """WaitKey函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def KeyDown(self, vk_code):
        """KeyDown函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def KeyUp(self, vk_code):
        """KeyUp函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def KeyDownChar(self, key_str):
        """KeyDownChar函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def KeyUpChar(self, key_str):
        """KeyUpChar函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def KeyPress(self, vk_code):
        """按下并释放指定按键

        Args:
            vk_code: vk_code参数

        Returns:
            1表示成功，0表示失败

        Example:
            # 按下回车键 (VK_RETURN = 13)
            vu.KeyPress(13)
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def KeyPressChar(self, key_str):
        """KeyPressChar函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def KeyPressStr(self, key_str, delay):
        """输入字符串

        Args:
            key_str: key_str参数
            delay: delay参数

        Returns:
            1表示成功，0表示失败

        Example:
            # 输入文本
            vu.KeyPressStr("Hello World")
        """
        pass

    # ==================== 窗口操作 ====================

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def EnumWindow(self, hParent, title, class_name, filter):
        """EnumWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def FindWindow(self, class_name, title):
        """查找窗口

        Args:
            class_name: 窗口类名（可为空）
            title: 窗口标题（可为空）

        Returns:
            窗口句柄，失败返回0

        Example:
            # 查找记事本窗口
            hwnd = vu.FindWindow("", "无标题 - 记事本")
            if hwnd > 0:
                print(f"找到窗口: {hwnd}")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def FindWindowByProcess(self, process_name, class_name, title):
        """FindWindowByProcess函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def FindWindowByProcessId(self, pid, class_name, title):
        """FindWindowByProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def FindWindowEx(self, hParent, class_name, title):
        """FindWindowEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetClientRect(self, hwnd, x1, y1, x2, y2):
        """GetClientRect函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetClientSize(self, hwnd, width, height):
        """GetClientSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetMousePointWindow(self):
        """GetMousePointWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetPointWindow(self, x, y):
        """GetPointWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def GetSpecialWindow(self, flag):
        """GetSpecialWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetWindowTitle(self, hwnd):
        """GetWindowTitle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetWindowRect(self, hwnd, x1, y1, x2, y2):
        """获取窗口矩形区域

        Args:
            hwnd: 窗口句柄
            x1: ctypes.c_long对象，接收左上角X
            y1: ctypes.c_long对象，接收左上角Y
            x2: ctypes.c_long对象，接收右下角X
            y2: ctypes.c_long对象，接收右下角Y

        Returns:
            1表示成功，0表示失败

        Example:
            # 获取窗口位置
            x1, y1 = ctypes.c_long(0), ctypes.c_long(0)
            x2, y2 = ctypes.c_long(0), ctypes.c_long(0)
            ret = vu.GetWindowRect(hwnd, x1, y1, x2, y2)
            if ret:
                print(f"窗口区域: ({x1.value},{y1.value})-({x2.value},{y2.value})")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def GetWindowState(self, hwnd, flag):
        """GetWindowState函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def SetWindowSize(self, hwnd, width, height):
        """SetWindowSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def SetWindowState(self, hwnd, flag):
        """SetWindowState函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def SetWindowText(self, hwnd, title):
        """SetWindowText函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetProcessInfo(self, pid):
        """GetProcessInfo函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def EnumProcess(self, name):
        """EnumProcess函数
        """
        pass

    # ==================== 图像识别 ====================

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def Capture(self, x1, y1, x2, y2, file):
        """截图到内存

        Args:
            x1: 左上角X坐标
            y1: 左上角Y坐标
            x2: 右下角X坐标
            y2: 右下角Y坐标
            file: 保存路径

        Returns:
            图片ID，失败返回0

        Example:
            # 截取屏幕区域
            pic_id = vu.Capture(0, 0, 100, 100, "screen.bmp")
            if pic_id > 0:
                print(f"截图成功，ID: {pic_id}")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def CaptureJpg(self, x1, y1, x2, y2, file):
        """CaptureJpg函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def CapturePng(self, x1, y1, x2, y2, file):
        """CapturePng函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def CaptureGif(self, x1, y1, x2, y2, file, delay, time):
        """CaptureGif函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindPic(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY):
        """在屏幕区域查找图片

        Args:
            x1: 查找区域左上角X
            y1: 查找区域左上角Y
            x2: 查找区域右下角X
            y2: 查找区域右下角Y
            pic_name: 图片文件路径
            delta_color: 颜色偏差值（0-255）
            sim: 相似度（0.0-1.0）
            dir: 查找方向（0从左到右，1从右到左等）
            intX: intX参数
            intY: intY参数

        Returns:
            1表示找到，0表示未找到

        Example:
            # 查找图片
            x, y = ctypes.c_long(0), ctypes.c_long(0)
            ret = vu.FindPic(0, 0, 1920, 1080, "target.bmp", 10, 0.9, 0, x, y)
            if ret:
                print(f"找到图片位置: ({x.value}, {y.value})")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicEx(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        """FindPicEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicExS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        """FindPicExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindMultiColor(self, x1, y1, x2, y2, first_color, offset_color, sim, dir, intX, intY):
        """FindMultiColor函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindColor(self, x1, y1, x2, y2, color_format, sim, dir, intX, intY):
        """FindColor函数
        """
        pass

    # ==================== 文件操作 ====================

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def IsFileExist(self, file):
        """IsFileExist函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def CopyFile(self, src_file, dst_file, over):
        """CopyFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def CreateFolder(self, folder):
        """CreateFolder函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def DeleteFile(self, file):
        """DeleteFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def DeleteFolder(self, folder):
        """DeleteFolder函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def GetFileLength(self, file):
        """GetFileLength函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def ReadFile(self, file):
        """读取文件内容

        Args:
            file: file参数

        Returns:
            文件内容字符串

        Example:
            # 读取文件
            content = vu.ReadFile("test.txt")
            print(f"文件内容: {content}")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def WriteFile(self, file, content):
        """写入文件

        Args:
            file: file参数
            content: 要写入的内容

        Returns:
            1表示成功，0表示失败

        Example:
            # 写入文件
            ret = vu.WriteFile("test.txt", "Hello VU Plugin")
            if ret:
                print("文件写入成功")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetDir(self, type):
        """GetDir函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def RunApp(self, app_path, mode):
        """RunApp函数
        """
        pass

    # ==================== 剪贴板操作 ====================

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetClipboard(self):
        """获取剪贴板内容

        Returns:
            剪贴板文本内容

        Example:
            # 读取剪贴板
            text = vu.GetClipboard()
            print(f"剪贴板内容: {text}")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def SetClipboard(self, value):
        """设置剪贴板内容

        Args:
            value: value参数

        Returns:
            1表示成功，0表示失败

        Example:
            # 写入剪贴板
            vu.SetClipboard("Hello World")
        """
        pass

    # ==================== 内存操作 ====================

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def ReadDouble(self, hwnd, addr):
        """ReadDouble函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_float, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def ReadFloat(self, hwnd, addr):
        """ReadFloat函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long])
    def ReadInt(self, hwnd, addr, type):
        """ReadInt函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def ReadString(self, hwnd, addr, type, len):
        """ReadString函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_double])
    def WriteDouble(self, hwnd, addr, data):
        """WriteDouble函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_float])
    def WriteFloat(self, hwnd, addr, data):
        """WriteFloat函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_longlong])
    def WriteInt(self, hwnd, addr, type, data):
        """WriteInt函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p])
    def WriteString(self, hwnd, addr, type, data):
        """WriteString函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_double, ctypes.c_double])
    def FindDouble(self, hwnd, addr_range, minV, maxV):
        """FindDouble函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_float, ctypes.c_float])
    def FindFloat(self, hwnd, addr_range, minV, maxV):
        """FindFloat函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long])
    def FindInt(self, hwnd, addr_range, minV, maxV, type):
        """FindInt函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def FindString(self, hwnd, addr_range, string_value, type):
        """FindString函数
        """
        pass

    # ==================== 后台操作 ====================

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def SendString(self, hwnd, str):
        """SendString函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def SendStringIme(self, hwnd, str):
        """SendStringIme函数
        """
        pass

    # ==================== 其他功能 ====================

    @cls_function(israw=False, restype=ctypes.c_void_p, arg_types=[ctypes.c_long])
    def TerminalStart(self, port):
        """TerminalStart函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_void_p])
    def TerminalStop(self, pTerminal):
        """TerminalStop函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def CreateRemote(self, ip, port):
        """CreateRemote函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetCursorShapeEx(self, type):
        """GetCursorShapeEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetMouseSpeed(self):
        """GetMouseSpeed函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetMouseSpeed(self, speed):
        """SetMouseSpeed函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetMouseDelay(self, delay):
        """SetMouseDelay函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def EnableRealKeypad(self, enable):
        """EnableRealKeypad函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetKeypadDelay(self, delay):
        """SetKeypadDelay函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindPicS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY):
        """FindPicS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicE(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        """FindPicE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def AppendPicAddr(self, pic_info, addr, size):
        """AppendPicAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindPicMem(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir, intX, intY):
        """FindPicMem函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicMemE(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        """FindPicMemE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicMemEx(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        """FindPicMemEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def MatchPicName(self, pic_name):
        """MatchPicName函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def GetPicSize(self, pic_name, w, h):
        """GetPicSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long])
    def GetScreenDataBmp(self, x1, y1, x2, y2, data, size):
        """GetScreenDataBmp函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_void_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetScreenData(self, x1, y1, x2, y2):
        """GetScreenData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long])
    def IsDisplayDead(self, x1, y1, x2, y2, times):
        """IsDisplayDead函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicByPic(self, source_pic, target_pic, delta_color, sim, dir):
        """FindPicByPic函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def BGR2RGB(self, bgr_color):
        """BGR2RGB函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def RGB2BGR(self, rgb_color):
        """RGB2BGR函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetColor(self, x, y):
        """GetColor函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetColorBGR(self, x, y):
        """GetColorBGR函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetAveRGB(self, x1, y1, x2, y2):
        """GetAveRGB函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def GetColorNum(self, x1, y1, x2, y2, color_format, sim):
        """GetColorNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def CmpColor(self, x, y, color_format, sim):
        """CmpColor函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindMultiColorE(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        """FindMultiColorE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindMultiColorEx(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        """FindMultiColorEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindColorE(self, x1, y1, x2, y2, color_format, sim, dir):
        """FindColorE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindColorEx(self, x1, y1, x2, y2, color_format, sim, dir):
        """FindColorEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def FindMulColor(self, x1, y1, x2, y2, color_format, sim):
        """FindMulColor函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long])
    def FindColorBlock(self, x1, y1, x2, y2, color_format, sim, count, width, height, intX, intY):
        """FindColorBlock函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def FindColorBlockE(self, x1, y1, x2, y2, color_format, sim, count, width, height):
        """FindColorBlockE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def FindColorBlockEx(self, x1, y1, x2, y2, color_format, sim, count, width, height):
        """FindColorBlockEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindShape(self, x1, y1, x2, y2, offset_info, color_format, sim, dir, intX, intY):
        """FindShape函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindShapeE(self, x1, y1, x2, y2, offset_info, color_format, sim, dir):
        """FindShapeE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindShapeEx(self, x1, y1, x2, y2, offset_info, color_format, sim, dir):
        """FindShapeEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def SetDict(self, index, file):
        """SetDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_void_p, ctypes.c_long])
    def SetDictMem(self, index, p数据, n长度):
        """SetDictMem函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def UseDict(self, index):
        """UseDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetNowDict(self):
        """GetNowDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def AddDict(self, index, dict_info):
        """AddDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def ClearDict(self, index):
        """ClearDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_long])
    def GetDict(self, index, font_index):
        """GetDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_long])
    def DelDict(self, index, font_index):
        """DelDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def GetDictCount(self, index):
        """GetDictCount函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def GetDictInfo(self, str, font_name, font_size, flag):
        """GetDictInfo函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetFontList(self):
        """GetFontList函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def SaveDict(self, index, file):
        """SaveDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p])
    def FetchWord(self, x1, y1, x2, y2, color_format, word):
        """FetchWord函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FetchDots(self, x1, y1, x2, y2, color_format, rowGap, colGap):
        """FetchDots函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def Ocr(self, x1, y1, x2, y2, color_format, sim):
        """Ocr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def OcrEx(self, x1, y1, x2, y2, color_format, sim):
        """OcrEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def OcrExOne(self, x1, y1, x2, y2, color_format, sim):
        """OcrExOne函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def OcrInFile(self, x1, y1, x2, y2, pic_name, color_format, sim):
        """OcrInFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def FindStr(self, x1, y1, x2, y2, str, color_format, sim, intX, intY):
        """FindStr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def FindStrS(self, x1, y1, x2, y2, str, color_format, sim, intX, intY):
        """FindStrS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrE(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrEx(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrExS(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def FindStrFast(self, x1, y1, x2, y2, str, color_format, sim, intX, intY):
        """FindStrFast函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def FindStrFastS(self, x1, y1, x2, y2, str, color_format, sim, intX, intY):
        """FindStrFastS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrFastE(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrFastE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrFastEx(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrFastEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrFastExS(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrFastExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindStrWithFont(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag, intX, intY):
        """FindStrWithFont函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindStrWithFontS(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag, intX, intY):
        """FindStrWithFontS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FindStrWithFontE(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag):
        """FindStrWithFontE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FindStrWithFontEx(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag):
        """FindStrWithFontEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FindStrWithFontExS(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag):
        """FindStrWithFontExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def GetResultCount(self, text, splitRows, splitCols):
        """GetResultCount函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def GetResultPos(self, text, index, intX, intY, splitRows, splitCols):
        """GetResultPos函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p])
    def ExcludePos(self, text, x1, y1, x2, y2, splitRows, splitCols):
        """ExcludePos函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p])
    def FindNearestPos(self, text, x, y, splitRows, splitCols):
        """FindNearestPos函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p])
    def SortPosDistance(self, text, x, y, splitRows, splitCols):
        """SortPosDistance函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def FindMinDistanceLine(self, text, beginX, beginY, endX, endY, splitRows, splitCols):
        """FindMinDistanceLine函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def GetLineAngle(self, beginX, beginY, endX, endY):
        """GetLineAngle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def StrSplitInit(self, str, split):
        """StrSplitInit函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def StrSplitGet(self, index):
        """StrSplitGet函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def StrToNum(self, str, radix):
        """StrToNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long])
    def StrNumConvert(self, num, radix):
        """StrNumConvert函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def IsFolderExist(self, folder):
        """IsFolderExist函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def MoveFile(self, src_file, dst_file):
        """MoveFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def ReadFileData(self, file, len):
        """ReadFileData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def WriteFileData(self, file, data, len, pos):
        """WriteFileData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def ReadIni(self, section, key, file):
        """ReadIni函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def WriteIni(self, section, key, value, file):
        """WriteIni函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetCurrentFile(self):
        """GetCurrentFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def SetFileAttribute(self, file, attributes):
        """SetFileAttribute函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def GetFileAttribute(self, file):
        """GetFileAttribute函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def SelectDirectory(self):
        """SelectDirectory函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def SelectFile(self):
        """SelectFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DisableCloseDisplayAndSleep(self):
        """DisableCloseDisplayAndSleep函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def Beep(self, GHz, Time):
        """Beep函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def Delay(self, ms):
        """延迟（毫秒）

        Args:
            ms: 延迟时间（毫秒）

        Returns:
            1表示成功

        Example:
            # 延迟1秒
            vu.Delay(1000)
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetTime(self):
        """GetTime函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def Is64Bit(self):
        """Is64Bit函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetScreenHeight(self):
        """GetScreenHeight函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetScreenWidth(self):
        """获取屏幕宽度

        Returns:
            屏幕宽度（像素）

        Example:
            # 获取屏幕尺寸
            width = vu.GetScreenWidth()
            height = vu.GetScreenHeight()
            print(f"屏幕分辨率: {width}x{height}")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def SetScreen(self, Width, Height):
        """SetScreen函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetUAC(self, enable):
        """SetUAC函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetOsType(self):
        """GetOsType函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SysExitOs(self, type):
        """SysExitOs函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def IsSurrpotVt(self):
        """IsSurrpotVt函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetCpuName(self):
        """GetCpuName函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetGpuName(self):
        """GetGpuName函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetCpuUsage(self):
        """GetCpuUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetMemUsage(self):
        """GetMemUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetGpuUsage(self):
        """GetGpuUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetGpuMemUsage(self):
        """GetGpuMemUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetGpuMemShareUsage(self):
        """GetGpuMemShareUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetDiskSerial(self):
        """GetDiskSerial函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def Play(self, media_file):
        """Play函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def Stop(self, id):
        """Stop函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def ExecuteCmd(self, cmd_str, current_dir, time_out):
        """ExecuteCmd函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def InitCri(self):
        """InitCri函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def EnterCriTry(self):
        """EnterCriTry函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def EnterCri(self):
        """EnterCri函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def LeaveCri(self):
        """LeaveCri函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetExitThread(self, mode):
        """SetExitThread函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetThreadStatus(self, status):
        """SetThreadStatus函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def ClientToScreen(self, hwnd, x, y):
        """ClientToScreen函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def ScreenToClient(self, hwnd, x, y):
        """ScreenToClient函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def EnumWindowByProcess(self, process_name, title, class_name, filter):
        """EnumWindowByProcess函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def EnumWindowByProcessId(self, pid, title, class_name, filter):
        """EnumWindowByProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def EnumWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2, sort):
        """EnumWindowSuper函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FindWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2):
        """FindWindowSuper函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetForegroundFocus(self):
        """GetForegroundFocus函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetForegroundWindow(self):
        """GetForegroundWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def GetWindow(self, hwnd, flag):
        """GetWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetWindowClass(self, hwnd):
        """GetWindowClass函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def GetWindowProcessId(self, hwnd):
        """GetWindowProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def GetWindowThreadId(self, hwnd):
        """GetWindowThreadId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetWindowProcessPath(self, hwnd):
        """GetWindowProcessPath函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def GetWindowRectSize(self, hwnd, x, y, w, h, type):
        """GetWindowRectSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetWindowBorder(self, hwnd, width, height):
        """GetWindowBorder函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def MoveWindow(self, hwnd, x, y):
        """MoveWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SendPaste(self, hwnd):
        """SendPaste函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def SendString2(self, hwnd, str):
        """SendString2函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def SetClientSize(self, hwnd, width, height):
        """SetClientSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long])
    def SetWindowRectSize(self, hwnd, x, y, width, height, type):
        """SetWindowRectSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def SetWindowTransparent(self, hwnd, trans):
        """SetWindowTransparent函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def WindowIsHunging(self, hwnd, time):
        """WindowIsHunging函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetCommandLine(self, pid):
        """GetCommandLine函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def ProcessGetPath(self, pid):
        """ProcessGetPath函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def ProcessGetName(self, pid):
        """ProcessGetName函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def EnumModules(self, pid):
        """EnumModules函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def ProcessCreate(self, file, cmdLine, showType, waitForEnd):
        """ProcessCreate函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def TerminateProcess(self, pid):
        """TerminateProcess函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def TerminateProcessTree(self, pid):
        """TerminateProcessTree函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def ProcessIsAliving(self, pid):
        """ProcessIsAliving函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def ProcessIsHunging(self, pid):
        """ProcessIsHunging函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def ProcessGetCurrentPid(self):
        """ProcessGetCurrentPid函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def ProcessIsX64(self, pid):
        """ProcessIsX64函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def ProcessSetIsSuspend(self, pid, isSuspend):
        """ProcessSetIsSuspend函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetMemoryHwndAsProcessId(self, en):
        """SetMemoryHwndAsProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def GetModuleBaseAddr(self, hwnd, module):
        """GetModuleBaseAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def GetModuleSize(self, hwnd, module):
        """GetModuleSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_char_p])
    def GetRemoteApiAddress(self, hwnd, base_addr, fun_name):
        """GetRemoteApiAddress函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def VirtualAllocEx(self, hwnd, addr, size, type):
        """VirtualAllocEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def VirtualFreeEx(self, hwnd, addr):
        """VirtualFreeEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def VirtualProtectEx(self, hwnd, addr, size, type, new_protect):
        """VirtualProtectEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def VirtualQueryEx(self, hwnd, addr):
        """VirtualQueryEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long])
    def ReadDataAddrToBin(self, hwnd, addr, len):
        """ReadDataAddrToBin函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long])
    def ReadDataAddr(self, hwnd, addr, len):
        """ReadDataAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long])
    def ReadData(self, hwnd, addr, len):
        """ReadData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long])
    def ReadDataToBin(self, hwnd, addr, len):
        """ReadDataToBin函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def ReadDoubleAddr(self, hwnd, addr):
        """ReadDoubleAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_float, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def ReadFloatAddr(self, hwnd, addr):
        """ReadFloatAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long])
    def ReadIntAddr(self, hwnd, addr, type):
        """ReadIntAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def ReadStringAddr(self, hwnd, addr, type, len):
        """ReadStringAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_long])
    def WriteDataAddrFromBin(self, hwnd, addr, data, len):
        """WriteDataAddrFromBin函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_long])
    def WriteDataFromBin(self, hwnd, addr, data, len):
        """WriteDataFromBin函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_char_p])
    def WriteDataAddr(self, hwnd, addr, data):
        """WriteDataAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def WriteData(self, hwnd, addr, data):
        """WriteData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_double])
    def WriteDoubleAddr(self, hwnd, addr, data):
        """WriteDoubleAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_float])
    def WriteFloatAddr(self, hwnd, addr, data):
        """WriteFloatAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_longlong])
    def WriteIntAddr(self, hwnd, addr, type, data):
        """WriteIntAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_char_p])
    def WriteStringAddr(self, hwnd, addr, type, data):
        """WriteStringAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def DataToBytes(self, data, len):
        """DataToBytes函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def BytesToData(self, pBuf, len):
        """BytesToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_double])
    def DoubleToData(self, value):
        """DoubleToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_float])
    def FloatToData(self, value):
        """FloatToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def IntToData(self, value, type):
        """IntToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def StringToData(self, value, type):
        """StringToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindDataEx(self, hwnd, addr_range, data, step, multi_thread, mode):
        """FindDataEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def FindData(self, hwnd, addr_range, data):
        """FindData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindDoubleEx(self, hwnd, addr_range, minV, maxV, step, multi_thread, mode):
        """FindDoubleEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_float, ctypes.c_float, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindFloatEx(self, hwnd, addr_range, minV, maxV, step, multi_thread, mode):
        """FindFloatEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindIntEx(self, hwnd, addr_range, minV, maxV, type, step, multi_thread, mode):
        """FindIntEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindStringEx(self, hwnd, addr_range, string_value, type, step, multi_thread, mode):
        """FindStringEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_long])
    def WriteDataAddrFromBinNoTrace(self, hwnd, addr, data, len):
        """WriteDataAddrFromBinNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_long])
    def WriteDataFromBinNoTrace(self, hwnd, addr, data, len):
        """WriteDataFromBinNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_char_p])
    def WriteDataAddrNoTrace(self, hwnd, addr, data):
        """WriteDataAddrNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def WriteDataNoTrace(self, hwnd, addr, data):
        """WriteDataNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def DataAddrCancelNoTrace(self, hwnd, addr):
        """DataAddrCancelNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def DataCancelNoTrace(self, hwnd, addr):
        """DataCancelNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_longlong])
    def InjectFileData(self, hwnd, file_data, len):
        """InjectFileData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def InjectFile(self, hwnd, path):
        """InjectFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_longlong])
    def HookCreateAddr(self, hwnd, addrFrom, addrTo):
        """HookCreateAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def HookCreate(self, hwnd, addrFrom, addrTo):
        """HookCreate函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long])
    def HookStartAddr(self, hwnd, addrFrom, isNoTrace):
        """HookStartAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long])
    def HookStart(self, hwnd, addrFrom, isNoTrace):
        """HookStart函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def HookStopAddr(self, hwnd, addrFrom):
        """HookStopAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def HookStop(self, hwnd, addrFrom):
        """HookStop函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def AsmAdd(self, asm_ins):
        """AsmAdd函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def AsmClear(self):
        """AsmClear函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def Assemble(self, base_addr, is_64bit):
        """Assemble函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_longlong, ctypes.c_long])
    def DisAssemble(self, asm_code, base_addr, is_64bit):
        """DisAssemble函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AsmMemAlloc(self, hwnd, retAddr, retSize):
        """AsmMemAlloc函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def AsmMemFree(self, hwnd, addr):
        """AsmMemFree函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_char_p])
    def AsmCallEx(self, hwnd, mode, base_addr):
        """AsmCallEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long])
    def AsmCall(self, hwnd, mode):
        """AsmCall函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetAsmHwndAsProcessId(self, enable):
        """SetAsmHwndAsProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetShowAsmErrorMsg(self, show):
        """SetShowAsmErrorMsg函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def GuardInstall(self, mode):
        """GuardInstall函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def GuardFolder(self, path, enable):
        """GuardFolder函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def GuardFile(self, path, enable):
        """GuardFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def GuardProcess(self, pid, enable, hide):
        """GuardProcess函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def GuardWindow(self, hwnd, enable, display):
        """GuardWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def GuardDisk(self, Serial_Number):
        """GuardDisk函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def GuardMAC(self, Serial_Number):
        """GuardMAC函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def GuardBOIS(self, Serial_Number):
        """GuardBOIS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def GuardGPU(self, Serial_Number):
        """GuardGPU函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def GuardEnvironment(self, exeName, title):
        """GuardEnvironment函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_longlong, ctypes.c_longlong])
    def GuardRegistry(self, pid, section, key, data, len):
        """GuardRegistry函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def GuardRegistryData(self, pid, section, key, data):
        """GuardRegistryData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def GuardKillHandle(self, pid, type, name):
        """GuardKillHandle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def AStartLoadMapData(self, pData, isInvert):
        """AStartLoadMapData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def AStartLoadMapFile(self, file, isInvert):
        """AStartLoadMapFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def AStartDestroy(self):
        """AStartDestroy函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AStartSet(self, dir, beeline, diagonal, isCenter):
        """AStartSet函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AStartFindWay(self, beginX, beginY, endX, endY, intX, intY):
        """AStartFindWay函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AStartNextWay(self, currentX, currentY, intX, intY, dir):
        """AStartNextWay函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPic(self, x1, y1, x2, y2, pic_name, sim, dir, intX, intY):
        """AiFindPic函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicS(self, x1, y1, x2, y2, pic_name, sim, dir, intX, intY):
        """AiFindPicS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicE(self, x1, y1, x2, y2, pic_name, sim, dir):
        """AiFindPicE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicEx(self, x1, y1, x2, y2, pic_name, sim, dir):
        """AiFindPicEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicExS(self, x1, y1, x2, y2, pic_name, sim, dir):
        """AiFindPicExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicMem(self, x1, y1, x2, y2, pic_info, sim, dir, intX, intY):
        """AiFindPicMem函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicMemE(self, x1, y1, x2, y2, pic_info, sim, dir):
        """AiFindPicMemE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicMemEx(self, x1, y1, x2, y2, pic_info, sim, dir):
        """AiFindPicMemEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuper(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin, intX, intY):
        """AiFindPicSuper函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperS(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin, intX, intY):
        """AiFindPicSuperS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperE(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin):
        """AiFindPicSuperE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperEx(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin):
        """AiFindPicSuperEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperExS(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin):
        """AiFindPicSuperExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperMem(self, x1, y1, x2, y2, pic_info, sim, detMode, isBin, intX, intY):
        """AiFindPicSuperMem函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperMemE(self, x1, y1, x2, y2, pic_info, sim, detMode, isBin):
        """AiFindPicSuperMemE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperMemEx(self, x1, y1, x2, y2, pic_info, sim, detMode, isBin):
        """AiFindPicSuperMemEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def AiYoloSetModel(self, index, file):
        """AiYoloSetModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_longlong, ctypes.c_long])
    def AiYoloSetModelMemory(self, index, data, size):
        """AiYoloSetModelMemory函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def AiYoloUseModel(self, index):
        """AiYoloUseModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_double, ctypes.c_double])
    def AiYoloDetectObjects(self, x1, y1, x2, y2, prob, iou):
        """AiYoloDetectObjects函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def AiOcrSetModel(self, index, det_model, rec_model, rec_dict):
        """AiOcrSetModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def AiOcrUseModel(self, index):
        """AiOcrUseModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def AiOcrDetectObjects(self, x1, y1, x2, y2):
        """AiOcrDetectObjects函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def AiTableSetModel(self, index, det_model, rec_model, rec_dict, table_model, table_dict, layout_model, layout_dict):
        """AiTableSetModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def AiTableUseModel(self, index):
        """AiTableUseModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def AiTableDetectObjects(self, x1, y1, x2, y2):
        """AiTableDetectObjects函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def JsonReadInPut(self, str):
        """JsonReadInPut函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong])
    def JsonReadGetObjType(self, obj):
        """JsonReadGetObjType函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong])
    def JsonReadGetObjSize(self, obj):
        """JsonReadGetObjSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong, ctypes.c_char_p])
    def JsonReadGetValObjByKey(self, obj, key):
        """JsonReadGetValObjByKey函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong, ctypes.POINTER(ctypes.c_long)])
    def JsonReadGetValObjByIndex(self, obj, index):
        """JsonReadGetValObjByIndex函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong, ctypes.POINTER(ctypes.c_long)])
    def JsonReadGetKeyObj(self, obj, index):
        """JsonReadGetKeyObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_longlong])
    def JsonReadGetNum(self, obj):
        """JsonReadGetNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong])
    def JsonReadGetStr(self, obj):
        """JsonReadGetStr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong])
    def JsonReadGetArraySize(self, obj):
        """JsonReadGetArraySize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong, ctypes.POINTER(ctypes.c_long)])
    def JsonReadGetArrayObj(self, obj, index):
        """JsonReadGetArrayObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def JsonWriteClear(self):
        """JsonWriteClear函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[])
    def JsonWriteCreateObj(self):
        """JsonWriteCreateObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def JsonWriteAddStr(self, pJson, key, val):
        """JsonWriteAddStr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def JsonWriteAddNum(self, pJson, key, val):
        """JsonWriteAddNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_longlong])
    def JsonWriteAddArray(self, pJson, key, arr):
        """JsonWriteAddArray函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_longlong])
    def JsonWriteAddObj(self, pJson, key, obj):
        """JsonWriteAddObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong])
    def JsonWriteCreateArray(self, pJson):
        """JsonWriteCreateArray函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def JsonWriteArrayAddStr(self, arr, val):
        """JsonWriteArrayAddStr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def JsonWriteArrayAddNum(self, arr, val):
        """JsonWriteArrayAddNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_longlong])
    def JsonWriteArrayAddArray(self, arr, val_arr):
        """JsonWriteArrayAddArray函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_longlong])
    def JsonWriteArrayAddObj(self, arr, obj):
        """JsonWriteArrayAddObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def JsonWriteDeleteKey(self, pJson, key):
        """JsonWriteDeleteKey函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong])
    def JsonWriteOutPut(self, pJson):
        """JsonWriteOutPut函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def Rgb2String(self, rgb):
        """Rgb2String函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def Rgb2Hsv(self, rgb, h, s, v):
        """Rgb2Hsv函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def Hsv2Rgb(self, h, s, v):
        """Hsv2Rgb函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgFindPic(self, pLarge, pSmall, isFast, dir, sim, matchMethod):
        """ImgFindPic函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgFindPicSuper(self, pLarge, pSmall, isFast, detMode, matchThresh, showDbg):
        """ImgFindPicSuper函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def ImgGetImgObj(self, id):
        """ImgGetImgObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgGetImgObjEx(self, id, alpha_rgb, offset_rgb):
        """ImgGetImgObjEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def ImgCopy(self, id, pImg):
        """ImgCopy函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def ImgGetCopy(self, id):
        """ImgGetCopy函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def ImgPolyGetPointsRange(self, id):
        """ImgPolyGetPointsRange函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long])
    def ImgContoursGetPoints(self, id, index):
        """ImgContoursGetPoints函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgContoursGetPointsSimplify(self, id, index, epsilon):
        """ImgContoursGetPointsSimplify函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def ImgMaskSelected(self, id):
        """ImgMaskSelected函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgMaskCircle(self, id, x, y, radius, isGradient):
        """ImgMaskCircle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgMaskRect(self, id, x1, y1, x2, y2, isGradient):
        """ImgMaskRect函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def ImgMaskPoly(self, id):
        """ImgMaskPoly函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def ImgMaskInvert(self, id, pMask):
        """ImgMaskInvert函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong])
    def ImgOperator(self, id, mode, pObj1, pObj2, pMask):
        """ImgOperator函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def LlmGetResponse(self, is_end):
        """LlmGetResponse函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def LlmGetToolCall(self, count):
        """LlmGetToolCall函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def AudioGetDeviceList(self):
        """AudioGetDeviceList函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def AudioGetDeviceDefault(self, mode):
        """AudioGetDeviceDefault函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long])
    def AudioRecordGetStreamInfo(self, channelse, sampleRate):
        """AudioRecordGetStreamInfo函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def AudioGetStreamSize(self, mode):
        """AudioGetStreamSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def SndAsr(self, index, buf, num_samples, sample_rate, isFinished):
        """SndAsr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def SndGetStream(self, index, samples, num_samples):
        """SndGetStream函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def SndGetError(self, index):
        """SndGetError函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def DrawGetError(self):
        """DrawGetError函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawCreate(self, x, y, w, h, isFast):
        """DrawCreate函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def DrawCreateByWindow(self, hTarget):
        """DrawCreateByWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def DrawSetStyle(self, isThrough, alpha):
        """DrawSetStyle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long])
    def DrawSetPosition(self, isShow, x, y, w, h):
        """DrawSetPosition函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawRun(self):
        """DrawRun函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawStop(self):
        """DrawStop函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawIsRunning(self):
        """DrawIsRunning函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawGetFps(self):
        """DrawGetFps函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawClear(self):
        """DrawClear函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawRender(self):
        """DrawRender函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawString(self, str, x, y, rgb, alpha, fontFamilyName, fontWeight, fontStyle, fontSize):
        """DrawString函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawLine(self, x1, y1, x2, y2, rgb, alpha, lineWidth):
        """DrawLine函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawPolygon(self, x, y, rgb, alpha, mode):
        """DrawPolygon函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawRectangle(self, x1, y1, x2, y2, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode):
        """DrawRectangle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawEllipse(self, x, y, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode):
        """DrawEllipse函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong])
    def DrawImgLoad(self, id, pImg, nImgSize):
        """DrawImgLoad函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong])
    def DrawImgRemove(self, id):
        """DrawImgRemove函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawImgClear(self):
        """DrawImgClear函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawImg(self, id, x, y, w, h, alpha, maintain):
        """DrawImg函数
        """
        pass

    # ==================== 其他功能 ====================

    @cls_function(israw=False, restype=ctypes.c_void_p, arg_types=[ctypes.c_long])
    def TerminalStart(self, port):
        """TerminalStart函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_void_p])
    def TerminalStop(self, pTerminal):
        """TerminalStop函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def CreateRemote(self, ip, port):
        """CreateRemote函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetCursorShapeEx(self, type):
        """GetCursorShapeEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetMouseSpeed(self):
        """GetMouseSpeed函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetMouseSpeed(self, speed):
        """SetMouseSpeed函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetMouseDelay(self, delay):
        """SetMouseDelay函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def EnableRealKeypad(self, enable):
        """EnableRealKeypad函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetKeypadDelay(self, delay):
        """SetKeypadDelay函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindPicS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY):
        """FindPicS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicE(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        """FindPicE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def AppendPicAddr(self, pic_info, addr, size):
        """AppendPicAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindPicMem(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir, intX, intY):
        """FindPicMem函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicMemE(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        """FindPicMemE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicMemEx(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        """FindPicMemEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def MatchPicName(self, pic_name):
        """MatchPicName函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def GetPicSize(self, pic_name, w, h):
        """GetPicSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long])
    def GetScreenDataBmp(self, x1, y1, x2, y2, data, size):
        """GetScreenDataBmp函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_void_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetScreenData(self, x1, y1, x2, y2):
        """GetScreenData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long])
    def IsDisplayDead(self, x1, y1, x2, y2, times):
        """IsDisplayDead函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindPicByPic(self, source_pic, target_pic, delta_color, sim, dir):
        """FindPicByPic函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def BGR2RGB(self, bgr_color):
        """BGR2RGB函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p])
    def RGB2BGR(self, rgb_color):
        """RGB2BGR函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetColor(self, x, y):
        """GetColor函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetColorBGR(self, x, y):
        """GetColorBGR函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetAveRGB(self, x1, y1, x2, y2):
        """GetAveRGB函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def GetColorNum(self, x1, y1, x2, y2, color_format, sim):
        """GetColorNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def CmpColor(self, x, y, color_format, sim):
        """CmpColor函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindMultiColorE(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        """FindMultiColorE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindMultiColorEx(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        """FindMultiColorEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindColorE(self, x1, y1, x2, y2, color_format, sim, dir):
        """FindColorE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindColorEx(self, x1, y1, x2, y2, color_format, sim, dir):
        """FindColorEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def FindMulColor(self, x1, y1, x2, y2, color_format, sim):
        """FindMulColor函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long])
    def FindColorBlock(self, x1, y1, x2, y2, color_format, sim, count, width, height, intX, intY):
        """FindColorBlock函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def FindColorBlockE(self, x1, y1, x2, y2, color_format, sim, count, width, height):
        """FindColorBlockE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def FindColorBlockEx(self, x1, y1, x2, y2, color_format, sim, count, width, height):
        """FindColorBlockEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindShape(self, x1, y1, x2, y2, offset_info, color_format, sim, dir, intX, intY):
        """FindShape函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindShapeE(self, x1, y1, x2, y2, offset_info, color_format, sim, dir):
        """FindShapeE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def FindShapeEx(self, x1, y1, x2, y2, offset_info, color_format, sim, dir):
        """FindShapeEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def SetDict(self, index, file):
        """SetDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_void_p, ctypes.c_long])
    def SetDictMem(self, index, p数据, n长度):
        """SetDictMem函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def UseDict(self, index):
        """UseDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetNowDict(self):
        """GetNowDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def AddDict(self, index, dict_info):
        """AddDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def ClearDict(self, index):
        """ClearDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_long])
    def GetDict(self, index, font_index):
        """GetDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_long])
    def DelDict(self, index, font_index):
        """DelDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def GetDictCount(self, index):
        """GetDictCount函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def GetDictInfo(self, str, font_name, font_size, flag):
        """GetDictInfo函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetFontList(self):
        """GetFontList函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def SaveDict(self, index, file):
        """SaveDict函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p])
    def FetchWord(self, x1, y1, x2, y2, color_format, word):
        """FetchWord函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FetchDots(self, x1, y1, x2, y2, color_format, rowGap, colGap):
        """FetchDots函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def Ocr(self, x1, y1, x2, y2, color_format, sim):
        """Ocr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def OcrEx(self, x1, y1, x2, y2, color_format, sim):
        """OcrEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double])
    def OcrExOne(self, x1, y1, x2, y2, color_format, sim):
        """OcrExOne函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def OcrInFile(self, x1, y1, x2, y2, pic_name, color_format, sim):
        """OcrInFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def FindStr(self, x1, y1, x2, y2, str, color_format, sim, intX, intY):
        """FindStr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def FindStrS(self, x1, y1, x2, y2, str, color_format, sim, intX, intY):
        """FindStrS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrE(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrEx(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrExS(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def FindStrFast(self, x1, y1, x2, y2, str, color_format, sim, intX, intY):
        """FindStrFast函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def FindStrFastS(self, x1, y1, x2, y2, str, color_format, sim, intX, intY):
        """FindStrFastS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrFastE(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrFastE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrFastEx(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrFastEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double])
    def FindStrFastExS(self, x1, y1, x2, y2, str, color_format, sim):
        """FindStrFastExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindStrWithFont(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag, intX, intY):
        """FindStrWithFont函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindStrWithFontS(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag, intX, intY):
        """FindStrWithFontS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FindStrWithFontE(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag):
        """FindStrWithFontE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FindStrWithFontEx(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag):
        """FindStrWithFontEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FindStrWithFontExS(self, x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag):
        """FindStrWithFontExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def GetResultCount(self, text, splitRows, splitCols):
        """GetResultCount函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def GetResultPos(self, text, index, intX, intY, splitRows, splitCols):
        """GetResultPos函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p])
    def ExcludePos(self, text, x1, y1, x2, y2, splitRows, splitCols):
        """ExcludePos函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p])
    def FindNearestPos(self, text, x, y, splitRows, splitCols):
        """FindNearestPos函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p])
    def SortPosDistance(self, text, x, y, splitRows, splitCols):
        """SortPosDistance函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def FindMinDistanceLine(self, text, beginX, beginY, endX, endY, splitRows, splitCols):
        """FindMinDistanceLine函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def GetLineAngle(self, beginX, beginY, endX, endY):
        """GetLineAngle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def StrSplitInit(self, str, split):
        """StrSplitInit函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def StrSplitGet(self, index):
        """StrSplitGet函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def StrToNum(self, str, radix):
        """StrToNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long])
    def StrNumConvert(self, num, radix):
        """StrNumConvert函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def IsFolderExist(self, folder):
        """IsFolderExist函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def MoveFile(self, src_file, dst_file):
        """MoveFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def ReadFileData(self, file, len):
        """ReadFileData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def WriteFileData(self, file, data, len, pos):
        """WriteFileData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def ReadIni(self, section, key, file):
        """ReadIni函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def WriteIni(self, section, key, value, file):
        """WriteIni函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetCurrentFile(self):
        """GetCurrentFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def SetFileAttribute(self, file, attributes):
        """SetFileAttribute函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def GetFileAttribute(self, file):
        """GetFileAttribute函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def SelectDirectory(self):
        """SelectDirectory函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def SelectFile(self):
        """SelectFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DisableCloseDisplayAndSleep(self):
        """DisableCloseDisplayAndSleep函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def Beep(self, GHz, Time):
        """Beep函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def Delay(self, ms):
        """延迟（毫秒）

        Args:
            ms: 延迟时间（毫秒）

        Returns:
            1表示成功

        Example:
            # 延迟1秒
            vu.Delay(1000)
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetTime(self):
        """GetTime函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def Is64Bit(self):
        """Is64Bit函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetScreenHeight(self):
        """GetScreenHeight函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetScreenWidth(self):
        """获取屏幕宽度

        Returns:
            屏幕宽度（像素）

        Example:
            # 获取屏幕尺寸
            width = vu.GetScreenWidth()
            height = vu.GetScreenHeight()
            print(f"屏幕分辨率: {width}x{height}")
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def SetScreen(self, Width, Height):
        """SetScreen函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetUAC(self, enable):
        """SetUAC函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetOsType(self):
        """GetOsType函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SysExitOs(self, type):
        """SysExitOs函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def IsSurrpotVt(self):
        """IsSurrpotVt函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetCpuName(self):
        """GetCpuName函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetGpuName(self):
        """GetGpuName函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetCpuUsage(self):
        """GetCpuUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetMemUsage(self):
        """GetMemUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetGpuUsage(self):
        """GetGpuUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetGpuMemUsage(self):
        """GetGpuMemUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetGpuMemShareUsage(self):
        """GetGpuMemShareUsage函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def GetDiskSerial(self):
        """GetDiskSerial函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def Play(self, media_file):
        """Play函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def Stop(self, id):
        """Stop函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def ExecuteCmd(self, cmd_str, current_dir, time_out):
        """ExecuteCmd函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def InitCri(self):
        """InitCri函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def EnterCriTry(self):
        """EnterCriTry函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def EnterCri(self):
        """EnterCri函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def LeaveCri(self):
        """LeaveCri函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetExitThread(self, mode):
        """SetExitThread函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetThreadStatus(self, status):
        """SetThreadStatus函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def ClientToScreen(self, hwnd, x, y):
        """ClientToScreen函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def ScreenToClient(self, hwnd, x, y):
        """ScreenToClient函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def EnumWindowByProcess(self, process_name, title, class_name, filter):
        """EnumWindowByProcess函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long])
    def EnumWindowByProcessId(self, pid, title, class_name, filter):
        """EnumWindowByProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def EnumWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2, sort):
        """EnumWindowSuper函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def FindWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2):
        """FindWindowSuper函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetForegroundFocus(self):
        """GetForegroundFocus函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def GetForegroundWindow(self):
        """GetForegroundWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def GetWindow(self, hwnd, flag):
        """GetWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetWindowClass(self, hwnd):
        """GetWindowClass函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def GetWindowProcessId(self, hwnd):
        """GetWindowProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def GetWindowThreadId(self, hwnd):
        """GetWindowThreadId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetWindowProcessPath(self, hwnd):
        """GetWindowProcessPath函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def GetWindowRectSize(self, hwnd, x, y, w, h, type):
        """GetWindowRectSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def GetWindowBorder(self, hwnd, width, height):
        """GetWindowBorder函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def MoveWindow(self, hwnd, x, y):
        """MoveWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SendPaste(self, hwnd):
        """SendPaste函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def SendString2(self, hwnd, str):
        """SendString2函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def SetClientSize(self, hwnd, width, height):
        """SetClientSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long])
    def SetWindowRectSize(self, hwnd, x, y, width, height, type):
        """SetWindowRectSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def SetWindowTransparent(self, hwnd, trans):
        """SetWindowTransparent函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def WindowIsHunging(self, hwnd, time):
        """WindowIsHunging函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def GetCommandLine(self, pid):
        """GetCommandLine函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def ProcessGetPath(self, pid):
        """ProcessGetPath函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def ProcessGetName(self, pid):
        """ProcessGetName函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def EnumModules(self, pid):
        """EnumModules函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_long])
    def ProcessCreate(self, file, cmdLine, showType, waitForEnd):
        """ProcessCreate函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def TerminateProcess(self, pid):
        """TerminateProcess函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def TerminateProcessTree(self, pid):
        """TerminateProcessTree函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def ProcessIsAliving(self, pid):
        """ProcessIsAliving函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def ProcessIsHunging(self, pid):
        """ProcessIsHunging函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def ProcessGetCurrentPid(self):
        """ProcessGetCurrentPid函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def ProcessIsX64(self, pid):
        """ProcessIsX64函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def ProcessSetIsSuspend(self, pid, isSuspend):
        """ProcessSetIsSuspend函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetMemoryHwndAsProcessId(self, en):
        """SetMemoryHwndAsProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def GetModuleBaseAddr(self, hwnd, module):
        """GetModuleBaseAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def GetModuleSize(self, hwnd, module):
        """GetModuleSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_char_p])
    def GetRemoteApiAddress(self, hwnd, base_addr, fun_name):
        """GetRemoteApiAddress函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def VirtualAllocEx(self, hwnd, addr, size, type):
        """VirtualAllocEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def VirtualFreeEx(self, hwnd, addr):
        """VirtualFreeEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def VirtualProtectEx(self, hwnd, addr, size, type, new_protect):
        """VirtualProtectEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def VirtualQueryEx(self, hwnd, addr):
        """VirtualQueryEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long])
    def ReadDataAddrToBin(self, hwnd, addr, len):
        """ReadDataAddrToBin函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long])
    def ReadDataAddr(self, hwnd, addr, len):
        """ReadDataAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long])
    def ReadData(self, hwnd, addr, len):
        """ReadData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long])
    def ReadDataToBin(self, hwnd, addr, len):
        """ReadDataToBin函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def ReadDoubleAddr(self, hwnd, addr):
        """ReadDoubleAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_float, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def ReadFloatAddr(self, hwnd, addr):
        """ReadFloatAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long])
    def ReadIntAddr(self, hwnd, addr, type):
        """ReadIntAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def ReadStringAddr(self, hwnd, addr, type, len):
        """ReadStringAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_long])
    def WriteDataAddrFromBin(self, hwnd, addr, data, len):
        """WriteDataAddrFromBin函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_long])
    def WriteDataFromBin(self, hwnd, addr, data, len):
        """WriteDataFromBin函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_char_p])
    def WriteDataAddr(self, hwnd, addr, data):
        """WriteDataAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def WriteData(self, hwnd, addr, data):
        """WriteData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_double])
    def WriteDoubleAddr(self, hwnd, addr, data):
        """WriteDoubleAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_float])
    def WriteFloatAddr(self, hwnd, addr, data):
        """WriteFloatAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_longlong])
    def WriteIntAddr(self, hwnd, addr, type, data):
        """WriteIntAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long, ctypes.c_char_p])
    def WriteStringAddr(self, hwnd, addr, type, data):
        """WriteStringAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def DataToBytes(self, data, len):
        """DataToBytes函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def BytesToData(self, pBuf, len):
        """BytesToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_double])
    def DoubleToData(self, value):
        """DoubleToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_float])
    def FloatToData(self, value):
        """FloatToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def IntToData(self, value, type):
        """IntToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def StringToData(self, value, type):
        """StringToData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindDataEx(self, hwnd, addr_range, data, step, multi_thread, mode):
        """FindDataEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def FindData(self, hwnd, addr_range, data):
        """FindData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindDoubleEx(self, hwnd, addr_range, minV, maxV, step, multi_thread, mode):
        """FindDoubleEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_float, ctypes.c_float, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindFloatEx(self, hwnd, addr_range, minV, maxV, step, multi_thread, mode):
        """FindFloatEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindIntEx(self, hwnd, addr_range, minV, maxV, type, step, multi_thread, mode):
        """FindIntEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def FindStringEx(self, hwnd, addr_range, string_value, type, step, multi_thread, mode):
        """FindStringEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_long])
    def WriteDataAddrFromBinNoTrace(self, hwnd, addr, data, len):
        """WriteDataAddrFromBinNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_long])
    def WriteDataFromBinNoTrace(self, hwnd, addr, data, len):
        """WriteDataFromBinNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_char_p])
    def WriteDataAddrNoTrace(self, hwnd, addr, data):
        """WriteDataAddrNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def WriteDataNoTrace(self, hwnd, addr, data):
        """WriteDataNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def DataAddrCancelNoTrace(self, hwnd, addr):
        """DataAddrCancelNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def DataCancelNoTrace(self, hwnd, addr):
        """DataCancelNoTrace函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_longlong])
    def InjectFileData(self, hwnd, file_data, len):
        """InjectFileData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def InjectFile(self, hwnd, path):
        """InjectFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_longlong])
    def HookCreateAddr(self, hwnd, addrFrom, addrTo):
        """HookCreateAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def HookCreate(self, hwnd, addrFrom, addrTo):
        """HookCreate函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_long])
    def HookStartAddr(self, hwnd, addrFrom, isNoTrace):
        """HookStartAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_long])
    def HookStart(self, hwnd, addrFrom, isNoTrace):
        """HookStart函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def HookStopAddr(self, hwnd, addrFrom):
        """HookStopAddr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p])
    def HookStop(self, hwnd, addrFrom):
        """HookStop函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p])
    def AsmAdd(self, asm_ins):
        """AsmAdd函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def AsmClear(self):
        """AsmClear函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def Assemble(self, base_addr, is_64bit):
        """Assemble函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_char_p, ctypes.c_longlong, ctypes.c_long])
    def DisAssemble(self, asm_code, base_addr, is_64bit):
        """DisAssemble函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AsmMemAlloc(self, hwnd, retAddr, retSize):
        """AsmMemAlloc函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def AsmMemFree(self, hwnd, addr):
        """AsmMemFree函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_char_p])
    def AsmCallEx(self, hwnd, mode, base_addr):
        """AsmCallEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long])
    def AsmCall(self, hwnd, mode):
        """AsmCall函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetAsmHwndAsProcessId(self, enable):
        """SetAsmHwndAsProcessId函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def SetShowAsmErrorMsg(self, show):
        """SetShowAsmErrorMsg函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def GuardInstall(self, mode):
        """GuardInstall函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def GuardFolder(self, path, enable):
        """GuardFolder函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def GuardFile(self, path, enable):
        """GuardFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def GuardProcess(self, pid, enable, hide):
        """GuardProcess函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def GuardWindow(self, hwnd, enable, display):
        """GuardWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def GuardDisk(self, Serial_Number):
        """GuardDisk函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def GuardMAC(self, Serial_Number):
        """GuardMAC函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def GuardBOIS(self, Serial_Number):
        """GuardBOIS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def GuardGPU(self, Serial_Number):
        """GuardGPU函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p, ctypes.c_char_p])
    def GuardEnvironment(self, exeName, title):
        """GuardEnvironment函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_longlong, ctypes.c_longlong])
    def GuardRegistry(self, pid, section, key, data, len):
        """GuardRegistry函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def GuardRegistryData(self, pid, section, key, data):
        """GuardRegistryData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p])
    def GuardKillHandle(self, pid, type, name):
        """GuardKillHandle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def AStartLoadMapData(self, pData, isInvert):
        """AStartLoadMapData函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long])
    def AStartLoadMapFile(self, file, isInvert):
        """AStartLoadMapFile函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def AStartDestroy(self):
        """AStartDestroy函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AStartSet(self, dir, beeline, diagonal, isCenter):
        """AStartSet函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AStartFindWay(self, beginX, beginY, endX, endY, intX, intY):
        """AStartFindWay函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AStartNextWay(self, currentX, currentY, intX, intY, dir):
        """AStartNextWay函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPic(self, x1, y1, x2, y2, pic_name, sim, dir, intX, intY):
        """AiFindPic函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicS(self, x1, y1, x2, y2, pic_name, sim, dir, intX, intY):
        """AiFindPicS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicE(self, x1, y1, x2, y2, pic_name, sim, dir):
        """AiFindPicE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicEx(self, x1, y1, x2, y2, pic_name, sim, dir):
        """AiFindPicEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicExS(self, x1, y1, x2, y2, pic_name, sim, dir):
        """AiFindPicExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicMem(self, x1, y1, x2, y2, pic_info, sim, dir, intX, intY):
        """AiFindPicMem函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicMemE(self, x1, y1, x2, y2, pic_info, sim, dir):
        """AiFindPicMemE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long])
    def AiFindPicMemEx(self, x1, y1, x2, y2, pic_info, sim, dir):
        """AiFindPicMemEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuper(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin, intX, intY):
        """AiFindPicSuper函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperS(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin, intX, intY):
        """AiFindPicSuperS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperE(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin):
        """AiFindPicSuperE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperEx(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin):
        """AiFindPicSuperEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperExS(self, x1, y1, x2, y2, pic_name, sim, detMode, isBin):
        """AiFindPicSuperExS函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperMem(self, x1, y1, x2, y2, pic_info, sim, detMode, isBin, intX, intY):
        """AiFindPicSuperMem函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperMemE(self, x1, y1, x2, y2, pic_info, sim, detMode, isBin):
        """AiFindPicSuperMemE函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_double, ctypes.c_long, ctypes.c_long])
    def AiFindPicSuperMemEx(self, x1, y1, x2, y2, pic_info, sim, detMode, isBin):
        """AiFindPicSuperMemEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p])
    def AiYoloSetModel(self, index, file):
        """AiYoloSetModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_longlong, ctypes.c_long])
    def AiYoloSetModelMemory(self, index, data, size):
        """AiYoloSetModelMemory函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def AiYoloUseModel(self, index):
        """AiYoloUseModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_double, ctypes.c_double])
    def AiYoloDetectObjects(self, x1, y1, x2, y2, prob, iou):
        """AiYoloDetectObjects函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def AiOcrSetModel(self, index, det_model, rec_model, rec_dict):
        """AiOcrSetModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def AiOcrUseModel(self, index):
        """AiOcrUseModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def AiOcrDetectObjects(self, x1, y1, x2, y2):
        """AiOcrDetectObjects函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])
    def AiTableSetModel(self, index, det_model, rec_model, rec_dict, table_model, table_dict, layout_model, layout_dict):
        """AiTableSetModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.POINTER(ctypes.c_long)])
    def AiTableUseModel(self, index):
        """AiTableUseModel函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)])
    def AiTableDetectObjects(self, x1, y1, x2, y2):
        """AiTableDetectObjects函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_char_p])
    def JsonReadInPut(self, str):
        """JsonReadInPut函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong])
    def JsonReadGetObjType(self, obj):
        """JsonReadGetObjType函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong])
    def JsonReadGetObjSize(self, obj):
        """JsonReadGetObjSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong, ctypes.c_char_p])
    def JsonReadGetValObjByKey(self, obj, key):
        """JsonReadGetValObjByKey函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong, ctypes.POINTER(ctypes.c_long)])
    def JsonReadGetValObjByIndex(self, obj, index):
        """JsonReadGetValObjByIndex函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong, ctypes.POINTER(ctypes.c_long)])
    def JsonReadGetKeyObj(self, obj, index):
        """JsonReadGetKeyObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_double, arg_types=[ctypes.c_longlong])
    def JsonReadGetNum(self, obj):
        """JsonReadGetNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong])
    def JsonReadGetStr(self, obj):
        """JsonReadGetStr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong])
    def JsonReadGetArraySize(self, obj):
        """JsonReadGetArraySize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong, ctypes.POINTER(ctypes.c_long)])
    def JsonReadGetArrayObj(self, obj, index):
        """JsonReadGetArrayObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def JsonWriteClear(self):
        """JsonWriteClear函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[])
    def JsonWriteCreateObj(self):
        """JsonWriteCreateObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def JsonWriteAddStr(self, pJson, key, val):
        """JsonWriteAddStr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def JsonWriteAddNum(self, pJson, key, val):
        """JsonWriteAddNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_longlong])
    def JsonWriteAddArray(self, pJson, key, arr):
        """JsonWriteAddArray函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_longlong])
    def JsonWriteAddObj(self, pJson, key, obj):
        """JsonWriteAddObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_longlong])
    def JsonWriteCreateArray(self, pJson):
        """JsonWriteCreateArray函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def JsonWriteArrayAddStr(self, arr, val):
        """JsonWriteArrayAddStr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def JsonWriteArrayAddNum(self, arr, val):
        """JsonWriteArrayAddNum函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_longlong])
    def JsonWriteArrayAddArray(self, arr, val_arr):
        """JsonWriteArrayAddArray函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_longlong])
    def JsonWriteArrayAddObj(self, arr, obj):
        """JsonWriteArrayAddObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long])
    def JsonWriteDeleteKey(self, pJson, key):
        """JsonWriteDeleteKey函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong])
    def JsonWriteOutPut(self, pJson):
        """JsonWriteOutPut函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def Rgb2String(self, rgb):
        """Rgb2String函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def Rgb2Hsv(self, rgb, h, s, v):
        """Rgb2Hsv函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def Hsv2Rgb(self, h, s, v):
        """Hsv2Rgb函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgFindPic(self, pLarge, pSmall, isFast, dir, sim, matchMethod):
        """ImgFindPic函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgFindPicSuper(self, pLarge, pSmall, isFast, detMode, matchThresh, showDbg):
        """ImgFindPicSuper函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def ImgGetImgObj(self, id):
        """ImgGetImgObj函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgGetImgObjEx(self, id, alpha_rgb, offset_rgb):
        """ImgGetImgObjEx函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def ImgCopy(self, id, pImg):
        """ImgCopy函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def ImgGetCopy(self, id):
        """ImgGetCopy函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def ImgPolyGetPointsRange(self, id):
        """ImgPolyGetPointsRange函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long])
    def ImgContoursGetPoints(self, id, index):
        """ImgContoursGetPoints函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgContoursGetPointsSimplify(self, id, index, epsilon):
        """ImgContoursGetPointsSimplify函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def ImgMaskSelected(self, id):
        """ImgMaskSelected函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgMaskCircle(self, id, x, y, radius, isGradient):
        """ImgMaskCircle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def ImgMaskRect(self, id, x1, y1, x2, y2, isGradient):
        """ImgMaskRect函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def ImgMaskPoly(self, id):
        """ImgMaskPoly函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_longlong])
    def ImgMaskInvert(self, id, pMask):
        """ImgMaskInvert函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong])
    def ImgOperator(self, id, mode, pObj1, pObj2, pMask):
        """ImgOperator函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def LlmGetResponse(self, is_end):
        """LlmGetResponse函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def LlmGetToolCall(self, count):
        """LlmGetToolCall函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def AudioGetDeviceList(self):
        """AudioGetDeviceList函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def AudioGetDeviceDefault(self, mode):
        """AudioGetDeviceDefault函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long, ctypes.c_long])
    def AudioRecordGetStreamInfo(self, channelse, sampleRate):
        """AudioRecordGetStreamInfo函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_longlong, arg_types=[ctypes.c_long])
    def AudioGetStreamSize(self, mode):
        """AudioGetStreamSize函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long, ctypes.c_long])
    def SndAsr(self, index, buf, num_samples, sample_rate, isFinished):
        """SndAsr函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def SndGetStream(self, index, samples, num_samples):
        """SndGetStream函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[ctypes.c_long])
    def SndGetError(self, index):
        """SndGetError函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_char_p, arg_types=[])
    def DrawGetError(self):
        """DrawGetError函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawCreate(self, x, y, w, h, isFast):
        """DrawCreate函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long])
    def DrawCreateByWindow(self, hTarget):
        """DrawCreateByWindow函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long])
    def DrawSetStyle(self, isThrough, alpha):
        """DrawSetStyle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long])
    def DrawSetPosition(self, isShow, x, y, w, h):
        """DrawSetPosition函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawRun(self):
        """DrawRun函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawStop(self):
        """DrawStop函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawIsRunning(self):
        """DrawIsRunning函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawGetFps(self):
        """DrawGetFps函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawClear(self):
        """DrawClear函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawRender(self):
        """DrawRender函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawString(self, str, x, y, rgb, alpha, fontFamilyName, fontWeight, fontStyle, fontSize):
        """DrawString函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawLine(self, x1, y1, x2, y2, rgb, alpha, lineWidth):
        """DrawLine函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawPolygon(self, x, y, rgb, alpha, mode):
        """DrawPolygon函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawRectangle(self, x1, y1, x2, y2, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode):
        """DrawRectangle函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawEllipse(self, x, y, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode):
        """DrawEllipse函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong])
    def DrawImgLoad(self, id, pImg, nImgSize):
        """DrawImgLoad函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong])
    def DrawImgRemove(self, id):
        """DrawImgRemove函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[])
    def DrawImgClear(self):
        """DrawImgClear函数
        """
        pass

    @cls_function(israw=False, restype=ctypes.c_long, arg_types=[ctypes.c_longlong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long])
    def DrawImg(self, id, x, y, w, h, alpha, maintain):
        """DrawImg函数
        """
        pass

