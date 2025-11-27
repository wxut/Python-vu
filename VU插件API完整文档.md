# VU插件 Python API 完整文档

> 本文档由 vusoft.py 自动生成

## 目录

- [简介](#简介)
- [快速开始](#快速开始)
- [插件功能函数](#插件功能函数)
- [基础功能](#基础功能)
- [窗口绑定](#窗口绑定)
- [鼠标操作](#鼠标操作)
- [键盘操作](#键盘操作)
- [窗口操作](#窗口操作)
- [图像识别](#图像识别)
- [文件操作](#文件操作)
- [剪贴板操作](#剪贴板操作)
- [内存操作](#内存操作)
- [后台操作](#后台操作)
- [其他功能](#其他功能)

---

## 简介

VU插件是一个功能强大的Windows自动化工具库，提供了丰富的API用于：
- 窗口操作和管理
- 鼠标键盘模拟
- 图像识别和OCR
- 文件操作
- 内存读写
- 剪贴板操作
- 以及更多...

### 特性

- ✓ 支持前台和后台操作
- ✓ 强大的图像识别功能
- ✓ AI OCR文字识别
- ✓ 内存读写功能
- ✓ 完整的键鼠模拟
- ✓ 易用的Python API

---

## 快速开始

```python
from vusoft import vusoft
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

---

## 基础功能

> 共 9 个函数

### Ver

获取插件版本号

        Returns:
            版本号字符串，如 "10.251025"

        Example:
            # 获取版本号
            version = vu.Ver()
            print(f"VU插件版本: {version}")

---

### Reg

注册插件

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

**参数:** `reg_code, ver_info`

---

### RegUrl

RegUrl函数

**参数:** `server_url`

---

### GetID

GetID函数

---

### SetPath

SetPath函数

**参数:** `path`

---

### GetPath

GetPath函数

---

### GetLastError

GetLastError函数

---

### Crypt

Crypt函数

**参数:** `mode, key, data, in_out_Len`

---

### SetDisplayInput

SetDisplayInput函数

**参数:** `mode`

---

## 窗口绑定

> 共 6 个函数

### BindWindowEx

BindWindowEx函数

**参数:** `hwnd, display, mouse, keypad, _public, mode`

---

### UnBindWindow

UnBindWindow函数

---

### GetBindWindow

GetBindWindow函数

---

### IsBind

IsBind函数

**参数:** `hwnd`

---

### SwitchBindWindow

SwitchBindWindow函数

**参数:** `hwnd`

---

### LockInput

LockInput函数

**参数:** `lock`

---

## 鼠标操作

> 共 19 个函数

### EnableRealMouse

EnableRealMouse函数

**参数:** `enable, mousedelay, mousestep`

---

### GetCursorPos

获取鼠标当前坐标

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

**参数:** `x, y`

---

### GetCursorSpot

GetCursorSpot函数

**参数:** `x, y`

---

### GetCursorShape

GetCursorShape函数

---

### LeftClick

鼠标左键单击

        Returns:
            1表示成功，0表示失败

        Example:
            # 左键单击
            vu.LeftClick()

---

### LeftDoubleClick

LeftDoubleClick函数

---

### LeftDown

LeftDown函数

---

### LeftUp

LeftUp函数

---

### MiddleClick

MiddleClick函数

---

### MiddleDown

MiddleDown函数

---

### MiddleUp

MiddleUp函数

---

### RightClick

RightClick函数

---

### RightDown

RightDown函数

---

### RightUp

RightUp函数

---

### WheelDown

WheelDown函数

---

### WheelUp

WheelUp函数

---

### MoveR

MoveR函数

**参数:** `rx, ry`

---

### MoveTo

移动鼠标到指定坐标

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

**参数:** `x, y`

---

### MoveToEx

MoveToEx函数

**参数:** `x, y, w, h`

---

## 键盘操作

> 共 9 个函数

### GetKeyState

GetKeyState函数

**参数:** `vk_code`

---

### WaitKey

WaitKey函数

**参数:** `vk_code, time_out`

---

### KeyDown

KeyDown函数

**参数:** `vk_code`

---

### KeyUp

KeyUp函数

**参数:** `vk_code`

---

### KeyDownChar

KeyDownChar函数

**参数:** `key_str`

---

### KeyUpChar

KeyUpChar函数

**参数:** `key_str`

---

### KeyPress

按下并释放指定按键

        Args:
            vk_code: vk_code参数

        Returns:
            1表示成功，0表示失败

        Example:
            # 按下回车键 (VK_RETURN = 13)
            vu.KeyPress(13)

**参数:** `vk_code`

---

### KeyPressChar

KeyPressChar函数

**参数:** `key_str`

---

### KeyPressStr

输入字符串

        Args:
            key_str: key_str参数
            delay: delay参数

        Returns:
            1表示成功，0表示失败

        Example:
            # 输入文本
            vu.KeyPressStr("Hello World")

**参数:** `key_str, delay`

---

## 窗口操作

> 共 18 个函数

### EnumWindow

EnumWindow函数

**参数:** `hParent, title, class_name, filter`

---

### FindWindow

查找窗口

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

**参数:** `class_name, title`

---

### FindWindowByProcess

FindWindowByProcess函数

**参数:** `process_name, class_name, title`

---

### FindWindowByProcessId

FindWindowByProcessId函数

**参数:** `pid, class_name, title`

---

### FindWindowEx

FindWindowEx函数

**参数:** `hParent, class_name, title`

---

### GetClientRect

GetClientRect函数

**参数:** `hwnd, x1, y1, x2, y2`

---

### GetClientSize

GetClientSize函数

**参数:** `hwnd, width, height`

---

### GetMousePointWindow

GetMousePointWindow函数

---

### GetPointWindow

GetPointWindow函数

**参数:** `x, y`

---

### GetSpecialWindow

GetSpecialWindow函数

**参数:** `flag`

---

### GetWindowTitle

GetWindowTitle函数

**参数:** `hwnd`

---

### GetWindowRect

获取窗口矩形区域

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

**参数:** `hwnd, x1, y1, x2, y2`

---

### GetWindowState

GetWindowState函数

**参数:** `hwnd, flag`

---

### SetWindowSize

SetWindowSize函数

**参数:** `hwnd, width, height`

---

### SetWindowState

SetWindowState函数

**参数:** `hwnd, flag`

---

### SetWindowText

SetWindowText函数

**参数:** `hwnd, title`

---

### GetProcessInfo

GetProcessInfo函数

**参数:** `pid`

---

### EnumProcess

EnumProcess函数

**参数:** `name`

---

## 图像识别

> 共 9 个函数

### Capture

截图到内存

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

**参数:** `x1, y1, x2, y2, file`

---

### CaptureJpg

CaptureJpg函数

**参数:** `x1, y1, x2, y2, file`

---

### CapturePng

CapturePng函数

**参数:** `x1, y1, x2, y2, file`

---

### CaptureGif

CaptureGif函数

**参数:** `x1, y1, x2, y2, file, delay, time`

---

### FindPic

在屏幕区域查找图片

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

**参数:** `x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY`

---

### FindPicEx

FindPicEx函数

**参数:** `x1, y1, x2, y2, pic_name, delta_color, sim, dir`

---

### FindPicExS

FindPicExS函数

**参数:** `x1, y1, x2, y2, pic_name, delta_color, sim, dir`

---

### FindMultiColor

FindMultiColor函数

**参数:** `x1, y1, x2, y2, first_color, offset_color, sim, dir, intX, intY`

---

### FindColor

FindColor函数

**参数:** `x1, y1, x2, y2, color_format, sim, dir, intX, intY`

---

## 文件操作

> 共 10 个函数

### IsFileExist

IsFileExist函数

**参数:** `file`

---

### CopyFile

CopyFile函数

**参数:** `src_file, dst_file, over`

---

### CreateFolder

CreateFolder函数

**参数:** `folder`

---

### DeleteFile

DeleteFile函数

**参数:** `file`

---

### DeleteFolder

DeleteFolder函数

**参数:** `folder`

---

### GetFileLength

GetFileLength函数

**参数:** `file`

---

### ReadFile

读取文件内容

        Args:
            file: file参数

        Returns:
            文件内容字符串

        Example:
            # 读取文件
            content = vu.ReadFile("test.txt")
            print(f"文件内容: {content}")

**参数:** `file`

---

### WriteFile

写入文件

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

**参数:** `file, content`

---

### GetDir

GetDir函数

**参数:** `type`

---

### RunApp

RunApp函数

**参数:** `app_path, mode`

---

## 剪贴板操作

> 共 2 个函数

### GetClipboard

获取剪贴板内容

        Returns:
            剪贴板文本内容

        Example:
            # 读取剪贴板
            text = vu.GetClipboard()
            print(f"剪贴板内容: {text}")

---

### SetClipboard

设置剪贴板内容

        Args:
            value: value参数

        Returns:
            1表示成功，0表示失败

        Example:
            # 写入剪贴板
            vu.SetClipboard("Hello World")

**参数:** `value`

---

## 内存操作

> 共 12 个函数

### ReadDouble

ReadDouble函数

**参数:** `hwnd, addr`

---

### ReadFloat

ReadFloat函数

**参数:** `hwnd, addr`

---

### ReadInt

ReadInt函数

**参数:** `hwnd, addr, type`

---

### ReadString

ReadString函数

**参数:** `hwnd, addr, type, len`

---

### WriteDouble

WriteDouble函数

**参数:** `hwnd, addr, data`

---

### WriteFloat

WriteFloat函数

**参数:** `hwnd, addr, data`

---

### WriteInt

WriteInt函数

**参数:** `hwnd, addr, type, data`

---

### WriteString

WriteString函数

**参数:** `hwnd, addr, type, data`

---

### FindDouble

FindDouble函数

**参数:** `hwnd, addr_range, minV, maxV`

---

### FindFloat

FindFloat函数

**参数:** `hwnd, addr_range, minV, maxV`

---

### FindInt

FindInt函数

**参数:** `hwnd, addr_range, minV, maxV, type`

---

### FindString

FindString函数

**参数:** `hwnd, addr_range, string_value, type`

---

## 后台操作

> 共 2 个函数

### SendString

SendString函数

**参数:** `hwnd, str`

---

### SendStringIme

SendStringIme函数

**参数:** `hwnd, str`

---

## 其他功能

> 共 664 个函数

### TerminalStart

TerminalStart函数

**参数:** `port`

---

### TerminalStop

TerminalStop函数

**参数:** `pTerminal`

---

### CreateRemote

CreateRemote函数

**参数:** `ip, port`

---

### GetCursorShapeEx

GetCursorShapeEx函数

**参数:** `type`

---

### GetMouseSpeed

GetMouseSpeed函数

---

### SetMouseSpeed

SetMouseSpeed函数

**参数:** `speed`

---

### SetMouseDelay

SetMouseDelay函数

**参数:** `delay`

---

### EnableRealKeypad

EnableRealKeypad函数

**参数:** `enable`

---

### SetKeypadDelay

SetKeypadDelay函数

**参数:** `delay`

---

### FindPicS

FindPicS函数

**参数:** `x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY`

---

### FindPicE

FindPicE函数

**参数:** `x1, y1, x2, y2, pic_name, delta_color, sim, dir`

---

### AppendPicAddr

AppendPicAddr函数

**参数:** `pic_info, addr, size`

---

### FindPicMem

FindPicMem函数

**参数:** `x1, y1, x2, y2, pic_info, delta_color, sim, dir, intX, intY`

---

### FindPicMemE

FindPicMemE函数

**参数:** `x1, y1, x2, y2, pic_info, delta_color, sim, dir`

---

### FindPicMemEx

FindPicMemEx函数

**参数:** `x1, y1, x2, y2, pic_info, delta_color, sim, dir`

---

### MatchPicName

MatchPicName函数

**参数:** `pic_name`

---

### GetPicSize

GetPicSize函数

**参数:** `pic_name, w, h`

---

### GetScreenDataBmp

GetScreenDataBmp函数

**参数:** `x1, y1, x2, y2, data, size`

---

### GetScreenData

GetScreenData函数

**参数:** `x1, y1, x2, y2`

---

### IsDisplayDead

IsDisplayDead函数

**参数:** `x1, y1, x2, y2, times`

---

### FindPicByPic

FindPicByPic函数

**参数:** `source_pic, target_pic, delta_color, sim, dir`

---

### BGR2RGB

BGR2RGB函数

**参数:** `bgr_color`

---

### RGB2BGR

RGB2BGR函数

**参数:** `rgb_color`

---

### GetColor

GetColor函数

**参数:** `x, y`

---

### GetColorBGR

GetColorBGR函数

**参数:** `x, y`

---

### GetAveRGB

GetAveRGB函数

**参数:** `x1, y1, x2, y2`

---

### GetColorNum

GetColorNum函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### CmpColor

CmpColor函数

**参数:** `x, y, color_format, sim`

---

### FindMultiColorE

FindMultiColorE函数

**参数:** `x1, y1, x2, y2, first_color, offset_color, sim, dir`

---

### FindMultiColorEx

FindMultiColorEx函数

**参数:** `x1, y1, x2, y2, first_color, offset_color, sim, dir`

---

### FindColorE

FindColorE函数

**参数:** `x1, y1, x2, y2, color_format, sim, dir`

---

### FindColorEx

FindColorEx函数

**参数:** `x1, y1, x2, y2, color_format, sim, dir`

---

### FindMulColor

FindMulColor函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### FindColorBlock

FindColorBlock函数

**参数:** `x1, y1, x2, y2, color_format, sim, count, width, height, intX, intY`

---

### FindColorBlockE

FindColorBlockE函数

**参数:** `x1, y1, x2, y2, color_format, sim, count, width, height`

---

### FindColorBlockEx

FindColorBlockEx函数

**参数:** `x1, y1, x2, y2, color_format, sim, count, width, height`

---

### FindShape

FindShape函数

**参数:** `x1, y1, x2, y2, offset_info, color_format, sim, dir, intX, intY`

---

### FindShapeE

FindShapeE函数

**参数:** `x1, y1, x2, y2, offset_info, color_format, sim, dir`

---

### FindShapeEx

FindShapeEx函数

**参数:** `x1, y1, x2, y2, offset_info, color_format, sim, dir`

---

### SetDict

SetDict函数

**参数:** `index, file`

---

### SetDictMem

SetDictMem函数

**参数:** `index, p数据, n长度`

---

### UseDict

UseDict函数

**参数:** `index`

---

### GetNowDict

GetNowDict函数

---

### AddDict

AddDict函数

**参数:** `index, dict_info`

---

### ClearDict

ClearDict函数

**参数:** `index`

---

### GetDict

GetDict函数

**参数:** `index, font_index`

---

### DelDict

DelDict函数

**参数:** `index, font_index`

---

### GetDictCount

GetDictCount函数

**参数:** `index`

---

### GetDictInfo

GetDictInfo函数

**参数:** `str, font_name, font_size, flag`

---

### GetFontList

GetFontList函数

---

### SaveDict

SaveDict函数

**参数:** `index, file`

---

### FetchWord

FetchWord函数

**参数:** `x1, y1, x2, y2, color_format, word`

---

### FetchDots

FetchDots函数

**参数:** `x1, y1, x2, y2, color_format, rowGap, colGap`

---

### Ocr

Ocr函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### OcrEx

OcrEx函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### OcrExOne

OcrExOne函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### OcrInFile

OcrInFile函数

**参数:** `x1, y1, x2, y2, pic_name, color_format, sim`

---

### FindStr

FindStr函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, intX, intY`

---

### FindStrS

FindStrS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, intX, intY`

---

### FindStrE

FindStrE函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrEx

FindStrEx函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrExS

FindStrExS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrFast

FindStrFast函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, intX, intY`

---

### FindStrFastS

FindStrFastS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, intX, intY`

---

### FindStrFastE

FindStrFastE函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrFastEx

FindStrFastEx函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrFastExS

FindStrFastExS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrWithFont

FindStrWithFont函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag, intX, intY`

---

### FindStrWithFontS

FindStrWithFontS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag, intX, intY`

---

### FindStrWithFontE

FindStrWithFontE函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag`

---

### FindStrWithFontEx

FindStrWithFontEx函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag`

---

### FindStrWithFontExS

FindStrWithFontExS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag`

---

### GetResultCount

GetResultCount函数

**参数:** `text, splitRows, splitCols`

---

### GetResultPos

GetResultPos函数

**参数:** `text, index, intX, intY, splitRows, splitCols`

---

### ExcludePos

ExcludePos函数

**参数:** `text, x1, y1, x2, y2, splitRows, splitCols`

---

### FindNearestPos

FindNearestPos函数

**参数:** `text, x, y, splitRows, splitCols`

---

### SortPosDistance

SortPosDistance函数

**参数:** `text, x, y, splitRows, splitCols`

---

### FindMinDistanceLine

FindMinDistanceLine函数

**参数:** `text, beginX, beginY, endX, endY, splitRows, splitCols`

---

### GetLineAngle

GetLineAngle函数

**参数:** `beginX, beginY, endX, endY`

---

### StrSplitInit

StrSplitInit函数

**参数:** `str, split`

---

### StrSplitGet

StrSplitGet函数

**参数:** `index`

---

### StrToNum

StrToNum函数

**参数:** `str, radix`

---

### StrNumConvert

StrNumConvert函数

**参数:** `num, radix`

---

### IsFolderExist

IsFolderExist函数

**参数:** `folder`

---

### MoveFile

MoveFile函数

**参数:** `src_file, dst_file`

---

### ReadFileData

ReadFileData函数

**参数:** `file, len`

---

### WriteFileData

WriteFileData函数

**参数:** `file, data, len, pos`

---

### ReadIni

ReadIni函数

**参数:** `section, key, file`

---

### WriteIni

WriteIni函数

**参数:** `section, key, value, file`

---

### GetCurrentFile

GetCurrentFile函数

---

### SetFileAttribute

SetFileAttribute函数

**参数:** `file, attributes`

---

### GetFileAttribute

GetFileAttribute函数

**参数:** `file`

---

### SelectDirectory

SelectDirectory函数

---

### SelectFile

SelectFile函数

---

### DisableCloseDisplayAndSleep

DisableCloseDisplayAndSleep函数

---

### Beep

Beep函数

**参数:** `GHz, Time`

---

### Delay

延迟（毫秒）

        Args:
            ms: 延迟时间（毫秒）

        Returns:
            1表示成功

        Example:
            # 延迟1秒
            vu.Delay(1000)

**参数:** `ms`

---

### GetTime

GetTime函数

---

### Is64Bit

Is64Bit函数

---

### GetScreenHeight

GetScreenHeight函数

---

### GetScreenWidth

获取屏幕宽度

        Returns:
            屏幕宽度（像素）

        Example:
            # 获取屏幕尺寸
            width = vu.GetScreenWidth()
            height = vu.GetScreenHeight()
            print(f"屏幕分辨率: {width}x{height}")

---

### SetScreen

SetScreen函数

**参数:** `Width, Height`

---

### SetUAC

SetUAC函数

**参数:** `enable`

---

### GetOsType

GetOsType函数

---

### SysExitOs

SysExitOs函数

**参数:** `type`

---

### IsSurrpotVt

IsSurrpotVt函数

---

### GetCpuName

GetCpuName函数

---

### GetGpuName

GetGpuName函数

---

### GetCpuUsage

GetCpuUsage函数

---

### GetMemUsage

GetMemUsage函数

---

### GetGpuUsage

GetGpuUsage函数

---

### GetGpuMemUsage

GetGpuMemUsage函数

---

### GetGpuMemShareUsage

GetGpuMemShareUsage函数

---

### GetDiskSerial

GetDiskSerial函数

---

### Play

Play函数

**参数:** `media_file`

---

### Stop

Stop函数

**参数:** `id`

---

### ExecuteCmd

ExecuteCmd函数

**参数:** `cmd_str, current_dir, time_out`

---

### InitCri

InitCri函数

---

### EnterCriTry

EnterCriTry函数

---

### EnterCri

EnterCri函数

---

### LeaveCri

LeaveCri函数

---

### SetExitThread

SetExitThread函数

**参数:** `mode`

---

### SetThreadStatus

SetThreadStatus函数

**参数:** `status`

---

### ClientToScreen

ClientToScreen函数

**参数:** `hwnd, x, y`

---

### ScreenToClient

ScreenToClient函数

**参数:** `hwnd, x, y`

---

### EnumWindowByProcess

EnumWindowByProcess函数

**参数:** `process_name, title, class_name, filter`

---

### EnumWindowByProcessId

EnumWindowByProcessId函数

**参数:** `pid, title, class_name, filter`

---

### EnumWindowSuper

EnumWindowSuper函数

**参数:** `spec1, flag1, type1, spec2, flag2, type2, sort`

---

### FindWindowSuper

FindWindowSuper函数

**参数:** `spec1, flag1, type1, spec2, flag2, type2`

---

### GetForegroundFocus

GetForegroundFocus函数

---

### GetForegroundWindow

GetForegroundWindow函数

---

### GetWindow

GetWindow函数

**参数:** `hwnd, flag`

---

### GetWindowClass

GetWindowClass函数

**参数:** `hwnd`

---

### GetWindowProcessId

GetWindowProcessId函数

**参数:** `hwnd`

---

### GetWindowThreadId

GetWindowThreadId函数

**参数:** `hwnd`

---

### GetWindowProcessPath

GetWindowProcessPath函数

**参数:** `hwnd`

---

### GetWindowRectSize

GetWindowRectSize函数

**参数:** `hwnd, x, y, w, h, type`

---

### GetWindowBorder

GetWindowBorder函数

**参数:** `hwnd, width, height`

---

### MoveWindow

MoveWindow函数

**参数:** `hwnd, x, y`

---

### SendPaste

SendPaste函数

**参数:** `hwnd`

---

### SendString2

SendString2函数

**参数:** `hwnd, str`

---

### SetClientSize

SetClientSize函数

**参数:** `hwnd, width, height`

---

### SetWindowRectSize

SetWindowRectSize函数

**参数:** `hwnd, x, y, width, height, type`

---

### SetWindowTransparent

SetWindowTransparent函数

**参数:** `hwnd, trans`

---

### WindowIsHunging

WindowIsHunging函数

**参数:** `hwnd, time`

---

### GetCommandLine

GetCommandLine函数

**参数:** `pid`

---

### ProcessGetPath

ProcessGetPath函数

**参数:** `pid`

---

### ProcessGetName

ProcessGetName函数

**参数:** `pid`

---

### EnumModules

EnumModules函数

**参数:** `pid`

---

### ProcessCreate

ProcessCreate函数

**参数:** `file, cmdLine, showType, waitForEnd`

---

### TerminateProcess

TerminateProcess函数

**参数:** `pid`

---

### TerminateProcessTree

TerminateProcessTree函数

**参数:** `pid`

---

### ProcessIsAliving

ProcessIsAliving函数

**参数:** `pid`

---

### ProcessIsHunging

ProcessIsHunging函数

**参数:** `pid`

---

### ProcessGetCurrentPid

ProcessGetCurrentPid函数

---

### ProcessIsX64

ProcessIsX64函数

**参数:** `pid`

---

### ProcessSetIsSuspend

ProcessSetIsSuspend函数

**参数:** `pid, isSuspend`

---

### SetMemoryHwndAsProcessId

SetMemoryHwndAsProcessId函数

**参数:** `en`

---

### GetModuleBaseAddr

GetModuleBaseAddr函数

**参数:** `hwnd, module`

---

### GetModuleSize

GetModuleSize函数

**参数:** `hwnd, module`

---

### GetRemoteApiAddress

GetRemoteApiAddress函数

**参数:** `hwnd, base_addr, fun_name`

---

### VirtualAllocEx

VirtualAllocEx函数

**参数:** `hwnd, addr, size, type`

---

### VirtualFreeEx

VirtualFreeEx函数

**参数:** `hwnd, addr`

---

### VirtualProtectEx

VirtualProtectEx函数

**参数:** `hwnd, addr, size, type, new_protect`

---

### VirtualQueryEx

VirtualQueryEx函数

**参数:** `hwnd, addr`

---

### ReadDataAddrToBin

ReadDataAddrToBin函数

**参数:** `hwnd, addr, len`

---

### ReadDataAddr

ReadDataAddr函数

**参数:** `hwnd, addr, len`

---

### ReadData

ReadData函数

**参数:** `hwnd, addr, len`

---

### ReadDataToBin

ReadDataToBin函数

**参数:** `hwnd, addr, len`

---

### ReadDoubleAddr

ReadDoubleAddr函数

**参数:** `hwnd, addr`

---

### ReadFloatAddr

ReadFloatAddr函数

**参数:** `hwnd, addr`

---

### ReadIntAddr

ReadIntAddr函数

**参数:** `hwnd, addr, type`

---

### ReadStringAddr

ReadStringAddr函数

**参数:** `hwnd, addr, type, len`

---

### WriteDataAddrFromBin

WriteDataAddrFromBin函数

**参数:** `hwnd, addr, data, len`

---

### WriteDataFromBin

WriteDataFromBin函数

**参数:** `hwnd, addr, data, len`

---

### WriteDataAddr

WriteDataAddr函数

**参数:** `hwnd, addr, data`

---

### WriteData

WriteData函数

**参数:** `hwnd, addr, data`

---

### WriteDoubleAddr

WriteDoubleAddr函数

**参数:** `hwnd, addr, data`

---

### WriteFloatAddr

WriteFloatAddr函数

**参数:** `hwnd, addr, data`

---

### WriteIntAddr

WriteIntAddr函数

**参数:** `hwnd, addr, type, data`

---

### WriteStringAddr

WriteStringAddr函数

**参数:** `hwnd, addr, type, data`

---

### DataToBytes

DataToBytes函数

**参数:** `data, len`

---

### BytesToData

BytesToData函数

**参数:** `pBuf, len`

---

### DoubleToData

DoubleToData函数

**参数:** `value`

---

### FloatToData

FloatToData函数

**参数:** `value`

---

### IntToData

IntToData函数

**参数:** `value, type`

---

### StringToData

StringToData函数

**参数:** `value, type`

---

### FindDataEx

FindDataEx函数

**参数:** `hwnd, addr_range, data, step, multi_thread, mode`

---

### FindData

FindData函数

**参数:** `hwnd, addr_range, data`

---

### FindDoubleEx

FindDoubleEx函数

**参数:** `hwnd, addr_range, minV, maxV, step, multi_thread, mode`

---

### FindFloatEx

FindFloatEx函数

**参数:** `hwnd, addr_range, minV, maxV, step, multi_thread, mode`

---

### FindIntEx

FindIntEx函数

**参数:** `hwnd, addr_range, minV, maxV, type, step, multi_thread, mode`

---

### FindStringEx

FindStringEx函数

**参数:** `hwnd, addr_range, string_value, type, step, multi_thread, mode`

---

### WriteDataAddrFromBinNoTrace

WriteDataAddrFromBinNoTrace函数

**参数:** `hwnd, addr, data, len`

---

### WriteDataFromBinNoTrace

WriteDataFromBinNoTrace函数

**参数:** `hwnd, addr, data, len`

---

### WriteDataAddrNoTrace

WriteDataAddrNoTrace函数

**参数:** `hwnd, addr, data`

---

### WriteDataNoTrace

WriteDataNoTrace函数

**参数:** `hwnd, addr, data`

---

### DataAddrCancelNoTrace

DataAddrCancelNoTrace函数

**参数:** `hwnd, addr`

---

### DataCancelNoTrace

DataCancelNoTrace函数

**参数:** `hwnd, addr`

---

### InjectFileData

InjectFileData函数

**参数:** `hwnd, file_data, len`

---

### InjectFile

InjectFile函数

**参数:** `hwnd, path`

---

### HookCreateAddr

HookCreateAddr函数

**参数:** `hwnd, addrFrom, addrTo`

---

### HookCreate

HookCreate函数

**参数:** `hwnd, addrFrom, addrTo`

---

### HookStartAddr

HookStartAddr函数

**参数:** `hwnd, addrFrom, isNoTrace`

---

### HookStart

HookStart函数

**参数:** `hwnd, addrFrom, isNoTrace`

---

### HookStopAddr

HookStopAddr函数

**参数:** `hwnd, addrFrom`

---

### HookStop

HookStop函数

**参数:** `hwnd, addrFrom`

---

### AsmAdd

AsmAdd函数

**参数:** `asm_ins`

---

### AsmClear

AsmClear函数

---

### Assemble

Assemble函数

**参数:** `base_addr, is_64bit`

---

### DisAssemble

DisAssemble函数

**参数:** `asm_code, base_addr, is_64bit`

---

### AsmMemAlloc

AsmMemAlloc函数

**参数:** `hwnd, retAddr, retSize`

---

### AsmMemFree

AsmMemFree函数

**参数:** `hwnd, addr`

---

### AsmCallEx

AsmCallEx函数

**参数:** `hwnd, mode, base_addr`

---

### AsmCall

AsmCall函数

**参数:** `hwnd, mode`

---

### SetAsmHwndAsProcessId

SetAsmHwndAsProcessId函数

**参数:** `enable`

---

### SetShowAsmErrorMsg

SetShowAsmErrorMsg函数

**参数:** `show`

---

### GuardInstall

GuardInstall函数

**参数:** `mode`

---

### GuardFolder

GuardFolder函数

**参数:** `path, enable`

---

### GuardFile

GuardFile函数

**参数:** `path, enable`

---

### GuardProcess

GuardProcess函数

**参数:** `pid, enable, hide`

---

### GuardWindow

GuardWindow函数

**参数:** `hwnd, enable, display`

---

### GuardDisk

GuardDisk函数

**参数:** `Serial_Number`

---

### GuardMAC

GuardMAC函数

**参数:** `Serial_Number`

---

### GuardBOIS

GuardBOIS函数

**参数:** `Serial_Number`

---

### GuardGPU

GuardGPU函数

**参数:** `Serial_Number`

---

### GuardEnvironment

GuardEnvironment函数

**参数:** `exeName, title`

---

### GuardRegistry

GuardRegistry函数

**参数:** `pid, section, key, data, len`

---

### GuardRegistryData

GuardRegistryData函数

**参数:** `pid, section, key, data`

---

### GuardKillHandle

GuardKillHandle函数

**参数:** `pid, type, name`

---

### AStartLoadMapData

AStartLoadMapData函数

**参数:** `pData, isInvert`

---

### AStartLoadMapFile

AStartLoadMapFile函数

**参数:** `file, isInvert`

---

### AStartDestroy

AStartDestroy函数

---

### AStartSet

AStartSet函数

**参数:** `dir, beeline, diagonal, isCenter`

---

### AStartFindWay

AStartFindWay函数

**参数:** `beginX, beginY, endX, endY, intX, intY`

---

### AStartNextWay

AStartNextWay函数

**参数:** `currentX, currentY, intX, intY, dir`

---

### AiFindPic

AiFindPic函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir, intX, intY`

---

### AiFindPicS

AiFindPicS函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir, intX, intY`

---

### AiFindPicE

AiFindPicE函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir`

---

### AiFindPicEx

AiFindPicEx函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir`

---

### AiFindPicExS

AiFindPicExS函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir`

---

### AiFindPicMem

AiFindPicMem函数

**参数:** `x1, y1, x2, y2, pic_info, sim, dir, intX, intY`

---

### AiFindPicMemE

AiFindPicMemE函数

**参数:** `x1, y1, x2, y2, pic_info, sim, dir`

---

### AiFindPicMemEx

AiFindPicMemEx函数

**参数:** `x1, y1, x2, y2, pic_info, sim, dir`

---

### AiFindPicSuper

AiFindPicSuper函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin, intX, intY`

---

### AiFindPicSuperS

AiFindPicSuperS函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin, intX, intY`

---

### AiFindPicSuperE

AiFindPicSuperE函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin`

---

### AiFindPicSuperEx

AiFindPicSuperEx函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin`

---

### AiFindPicSuperExS

AiFindPicSuperExS函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin`

---

### AiFindPicSuperMem

AiFindPicSuperMem函数

**参数:** `x1, y1, x2, y2, pic_info, sim, detMode, isBin, intX, intY`

---

### AiFindPicSuperMemE

AiFindPicSuperMemE函数

**参数:** `x1, y1, x2, y2, pic_info, sim, detMode, isBin`

---

### AiFindPicSuperMemEx

AiFindPicSuperMemEx函数

**参数:** `x1, y1, x2, y2, pic_info, sim, detMode, isBin`

---

### AiYoloSetModel

AiYoloSetModel函数

**参数:** `index, file`

---

### AiYoloSetModelMemory

AiYoloSetModelMemory函数

**参数:** `index, data, size`

---

### AiYoloUseModel

AiYoloUseModel函数

**参数:** `index`

---

### AiYoloDetectObjects

AiYoloDetectObjects函数

**参数:** `x1, y1, x2, y2, prob, iou`

---

### AiOcrSetModel

AiOcrSetModel函数

**参数:** `index, det_model, rec_model, rec_dict`

---

### AiOcrUseModel

AiOcrUseModel函数

**参数:** `index`

---

### AiOcrDetectObjects

AiOcrDetectObjects函数

**参数:** `x1, y1, x2, y2`

---

### AiTableSetModel

AiTableSetModel函数

**参数:** `index, det_model, rec_model, rec_dict, table_model, table_dict, layout_model, layout_dict`

---

### AiTableUseModel

AiTableUseModel函数

**参数:** `index`

---

### AiTableDetectObjects

AiTableDetectObjects函数

**参数:** `x1, y1, x2, y2`

---

### JsonReadInPut

JsonReadInPut函数

**参数:** `str`

---

### JsonReadGetObjType

JsonReadGetObjType函数

**参数:** `obj`

---

### JsonReadGetObjSize

JsonReadGetObjSize函数

**参数:** `obj`

---

### JsonReadGetValObjByKey

JsonReadGetValObjByKey函数

**参数:** `obj, key`

---

### JsonReadGetValObjByIndex

JsonReadGetValObjByIndex函数

**参数:** `obj, index`

---

### JsonReadGetKeyObj

JsonReadGetKeyObj函数

**参数:** `obj, index`

---

### JsonReadGetNum

JsonReadGetNum函数

**参数:** `obj`

---

### JsonReadGetStr

JsonReadGetStr函数

**参数:** `obj`

---

### JsonReadGetArraySize

JsonReadGetArraySize函数

**参数:** `obj`

---

### JsonReadGetArrayObj

JsonReadGetArrayObj函数

**参数:** `obj, index`

---

### JsonWriteClear

JsonWriteClear函数

---

### JsonWriteCreateObj

JsonWriteCreateObj函数

---

### JsonWriteAddStr

JsonWriteAddStr函数

**参数:** `pJson, key, val`

---

### JsonWriteAddNum

JsonWriteAddNum函数

**参数:** `pJson, key, val`

---

### JsonWriteAddArray

JsonWriteAddArray函数

**参数:** `pJson, key, arr`

---

### JsonWriteAddObj

JsonWriteAddObj函数

**参数:** `pJson, key, obj`

---

### JsonWriteCreateArray

JsonWriteCreateArray函数

**参数:** `pJson`

---

### JsonWriteArrayAddStr

JsonWriteArrayAddStr函数

**参数:** `arr, val`

---

### JsonWriteArrayAddNum

JsonWriteArrayAddNum函数

**参数:** `arr, val`

---

### JsonWriteArrayAddArray

JsonWriteArrayAddArray函数

**参数:** `arr, val_arr`

---

### JsonWriteArrayAddObj

JsonWriteArrayAddObj函数

**参数:** `arr, obj`

---

### JsonWriteDeleteKey

JsonWriteDeleteKey函数

**参数:** `pJson, key`

---

### JsonWriteOutPut

JsonWriteOutPut函数

**参数:** `pJson`

---

### Rgb2String

Rgb2String函数

**参数:** `rgb`

---

### Rgb2Hsv

Rgb2Hsv函数

**参数:** `rgb, h, s, v`

---

### Hsv2Rgb

Hsv2Rgb函数

**参数:** `h, s, v`

---

### ImgFindPic

ImgFindPic函数

**参数:** `pLarge, pSmall, isFast, dir, sim, matchMethod`

---

### ImgFindPicSuper

ImgFindPicSuper函数

**参数:** `pLarge, pSmall, isFast, detMode, matchThresh, showDbg`

---

### ImgGetImgObj

ImgGetImgObj函数

**参数:** `id`

---

### ImgGetImgObjEx

ImgGetImgObjEx函数

**参数:** `id, alpha_rgb, offset_rgb`

---

### ImgCopy

ImgCopy函数

**参数:** `id, pImg`

---

### ImgGetCopy

ImgGetCopy函数

**参数:** `id`

---

### ImgPolyGetPointsRange

ImgPolyGetPointsRange函数

**参数:** `id`

---

### ImgContoursGetPoints

ImgContoursGetPoints函数

**参数:** `id, index`

---

### ImgContoursGetPointsSimplify

ImgContoursGetPointsSimplify函数

**参数:** `id, index, epsilon`

---

### ImgMaskSelected

ImgMaskSelected函数

**参数:** `id`

---

### ImgMaskCircle

ImgMaskCircle函数

**参数:** `id, x, y, radius, isGradient`

---

### ImgMaskRect

ImgMaskRect函数

**参数:** `id, x1, y1, x2, y2, isGradient`

---

### ImgMaskPoly

ImgMaskPoly函数

**参数:** `id`

---

### ImgMaskInvert

ImgMaskInvert函数

**参数:** `id, pMask`

---

### ImgOperator

ImgOperator函数

**参数:** `id, mode, pObj1, pObj2, pMask`

---

### LlmGetResponse

LlmGetResponse函数

**参数:** `is_end`

---

### LlmGetToolCall

LlmGetToolCall函数

**参数:** `count`

---

### AudioGetDeviceList

AudioGetDeviceList函数

---

### AudioGetDeviceDefault

AudioGetDeviceDefault函数

**参数:** `mode`

---

### AudioRecordGetStreamInfo

AudioRecordGetStreamInfo函数

**参数:** `channelse, sampleRate`

---

### AudioGetStreamSize

AudioGetStreamSize函数

**参数:** `mode`

---

### SndAsr

SndAsr函数

**参数:** `index, buf, num_samples, sample_rate, isFinished`

---

### SndGetStream

SndGetStream函数

**参数:** `index, samples, num_samples`

---

### SndGetError

SndGetError函数

**参数:** `index`

---

### DrawGetError

DrawGetError函数

---

### DrawCreate

DrawCreate函数

**参数:** `x, y, w, h, isFast`

---

### DrawCreateByWindow

DrawCreateByWindow函数

**参数:** `hTarget`

---

### DrawSetStyle

DrawSetStyle函数

**参数:** `isThrough, alpha`

---

### DrawSetPosition

DrawSetPosition函数

**参数:** `isShow, x, y, w, h`

---

### DrawRun

DrawRun函数

---

### DrawStop

DrawStop函数

---

### DrawIsRunning

DrawIsRunning函数

---

### DrawGetFps

DrawGetFps函数

---

### DrawClear

DrawClear函数

---

### DrawRender

DrawRender函数

---

### DrawString

DrawString函数

**参数:** `str, x, y, rgb, alpha, fontFamilyName, fontWeight, fontStyle, fontSize`

---

### DrawLine

DrawLine函数

**参数:** `x1, y1, x2, y2, rgb, alpha, lineWidth`

---

### DrawPolygon

DrawPolygon函数

**参数:** `x, y, rgb, alpha, mode`

---

### DrawRectangle

DrawRectangle函数

**参数:** `x1, y1, x2, y2, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode`

---

### DrawEllipse

DrawEllipse函数

**参数:** `x, y, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode`

---

### DrawImgLoad

DrawImgLoad函数

**参数:** `id, pImg, nImgSize`

---

### DrawImgRemove

DrawImgRemove函数

**参数:** `id`

---

### DrawImgClear

DrawImgClear函数

---

### DrawImg

DrawImg函数

**参数:** `id, x, y, w, h, alpha, maintain`

---

### TerminalStart

TerminalStart函数

**参数:** `port`

---

### TerminalStop

TerminalStop函数

**参数:** `pTerminal`

---

### CreateRemote

CreateRemote函数

**参数:** `ip, port`

---

### GetCursorShapeEx

GetCursorShapeEx函数

**参数:** `type`

---

### GetMouseSpeed

GetMouseSpeed函数

---

### SetMouseSpeed

SetMouseSpeed函数

**参数:** `speed`

---

### SetMouseDelay

SetMouseDelay函数

**参数:** `delay`

---

### EnableRealKeypad

EnableRealKeypad函数

**参数:** `enable`

---

### SetKeypadDelay

SetKeypadDelay函数

**参数:** `delay`

---

### FindPicS

FindPicS函数

**参数:** `x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY`

---

### FindPicE

FindPicE函数

**参数:** `x1, y1, x2, y2, pic_name, delta_color, sim, dir`

---

### AppendPicAddr

AppendPicAddr函数

**参数:** `pic_info, addr, size`

---

### FindPicMem

FindPicMem函数

**参数:** `x1, y1, x2, y2, pic_info, delta_color, sim, dir, intX, intY`

---

### FindPicMemE

FindPicMemE函数

**参数:** `x1, y1, x2, y2, pic_info, delta_color, sim, dir`

---

### FindPicMemEx

FindPicMemEx函数

**参数:** `x1, y1, x2, y2, pic_info, delta_color, sim, dir`

---

### MatchPicName

MatchPicName函数

**参数:** `pic_name`

---

### GetPicSize

GetPicSize函数

**参数:** `pic_name, w, h`

---

### GetScreenDataBmp

GetScreenDataBmp函数

**参数:** `x1, y1, x2, y2, data, size`

---

### GetScreenData

GetScreenData函数

**参数:** `x1, y1, x2, y2`

---

### IsDisplayDead

IsDisplayDead函数

**参数:** `x1, y1, x2, y2, times`

---

### FindPicByPic

FindPicByPic函数

**参数:** `source_pic, target_pic, delta_color, sim, dir`

---

### BGR2RGB

BGR2RGB函数

**参数:** `bgr_color`

---

### RGB2BGR

RGB2BGR函数

**参数:** `rgb_color`

---

### GetColor

GetColor函数

**参数:** `x, y`

---

### GetColorBGR

GetColorBGR函数

**参数:** `x, y`

---

### GetAveRGB

GetAveRGB函数

**参数:** `x1, y1, x2, y2`

---

### GetColorNum

GetColorNum函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### CmpColor

CmpColor函数

**参数:** `x, y, color_format, sim`

---

### FindMultiColorE

FindMultiColorE函数

**参数:** `x1, y1, x2, y2, first_color, offset_color, sim, dir`

---

### FindMultiColorEx

FindMultiColorEx函数

**参数:** `x1, y1, x2, y2, first_color, offset_color, sim, dir`

---

### FindColorE

FindColorE函数

**参数:** `x1, y1, x2, y2, color_format, sim, dir`

---

### FindColorEx

FindColorEx函数

**参数:** `x1, y1, x2, y2, color_format, sim, dir`

---

### FindMulColor

FindMulColor函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### FindColorBlock

FindColorBlock函数

**参数:** `x1, y1, x2, y2, color_format, sim, count, width, height, intX, intY`

---

### FindColorBlockE

FindColorBlockE函数

**参数:** `x1, y1, x2, y2, color_format, sim, count, width, height`

---

### FindColorBlockEx

FindColorBlockEx函数

**参数:** `x1, y1, x2, y2, color_format, sim, count, width, height`

---

### FindShape

FindShape函数

**参数:** `x1, y1, x2, y2, offset_info, color_format, sim, dir, intX, intY`

---

### FindShapeE

FindShapeE函数

**参数:** `x1, y1, x2, y2, offset_info, color_format, sim, dir`

---

### FindShapeEx

FindShapeEx函数

**参数:** `x1, y1, x2, y2, offset_info, color_format, sim, dir`

---

### SetDict

SetDict函数

**参数:** `index, file`

---

### SetDictMem

SetDictMem函数

**参数:** `index, p数据, n长度`

---

### UseDict

UseDict函数

**参数:** `index`

---

### GetNowDict

GetNowDict函数

---

### AddDict

AddDict函数

**参数:** `index, dict_info`

---

### ClearDict

ClearDict函数

**参数:** `index`

---

### GetDict

GetDict函数

**参数:** `index, font_index`

---

### DelDict

DelDict函数

**参数:** `index, font_index`

---

### GetDictCount

GetDictCount函数

**参数:** `index`

---

### GetDictInfo

GetDictInfo函数

**参数:** `str, font_name, font_size, flag`

---

### GetFontList

GetFontList函数

---

### SaveDict

SaveDict函数

**参数:** `index, file`

---

### FetchWord

FetchWord函数

**参数:** `x1, y1, x2, y2, color_format, word`

---

### FetchDots

FetchDots函数

**参数:** `x1, y1, x2, y2, color_format, rowGap, colGap`

---

### Ocr

Ocr函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### OcrEx

OcrEx函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### OcrExOne

OcrExOne函数

**参数:** `x1, y1, x2, y2, color_format, sim`

---

### OcrInFile

OcrInFile函数

**参数:** `x1, y1, x2, y2, pic_name, color_format, sim`

---

### FindStr

FindStr函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, intX, intY`

---

### FindStrS

FindStrS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, intX, intY`

---

### FindStrE

FindStrE函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrEx

FindStrEx函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrExS

FindStrExS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrFast

FindStrFast函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, intX, intY`

---

### FindStrFastS

FindStrFastS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, intX, intY`

---

### FindStrFastE

FindStrFastE函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrFastEx

FindStrFastEx函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrFastExS

FindStrFastExS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim`

---

### FindStrWithFont

FindStrWithFont函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag, intX, intY`

---

### FindStrWithFontS

FindStrWithFontS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag, intX, intY`

---

### FindStrWithFontE

FindStrWithFontE函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag`

---

### FindStrWithFontEx

FindStrWithFontEx函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag`

---

### FindStrWithFontExS

FindStrWithFontExS函数

**参数:** `x1, y1, x2, y2, str, color_format, sim, font_name, font_size, flag`

---

### GetResultCount

GetResultCount函数

**参数:** `text, splitRows, splitCols`

---

### GetResultPos

GetResultPos函数

**参数:** `text, index, intX, intY, splitRows, splitCols`

---

### ExcludePos

ExcludePos函数

**参数:** `text, x1, y1, x2, y2, splitRows, splitCols`

---

### FindNearestPos

FindNearestPos函数

**参数:** `text, x, y, splitRows, splitCols`

---

### SortPosDistance

SortPosDistance函数

**参数:** `text, x, y, splitRows, splitCols`

---

### FindMinDistanceLine

FindMinDistanceLine函数

**参数:** `text, beginX, beginY, endX, endY, splitRows, splitCols`

---

### GetLineAngle

GetLineAngle函数

**参数:** `beginX, beginY, endX, endY`

---

### StrSplitInit

StrSplitInit函数

**参数:** `str, split`

---

### StrSplitGet

StrSplitGet函数

**参数:** `index`

---

### StrToNum

StrToNum函数

**参数:** `str, radix`

---

### StrNumConvert

StrNumConvert函数

**参数:** `num, radix`

---

### IsFolderExist

IsFolderExist函数

**参数:** `folder`

---

### MoveFile

MoveFile函数

**参数:** `src_file, dst_file`

---

### ReadFileData

ReadFileData函数

**参数:** `file, len`

---

### WriteFileData

WriteFileData函数

**参数:** `file, data, len, pos`

---

### ReadIni

ReadIni函数

**参数:** `section, key, file`

---

### WriteIni

WriteIni函数

**参数:** `section, key, value, file`

---

### GetCurrentFile

GetCurrentFile函数

---

### SetFileAttribute

SetFileAttribute函数

**参数:** `file, attributes`

---

### GetFileAttribute

GetFileAttribute函数

**参数:** `file`

---

### SelectDirectory

SelectDirectory函数

---

### SelectFile

SelectFile函数

---

### DisableCloseDisplayAndSleep

DisableCloseDisplayAndSleep函数

---

### Beep

Beep函数

**参数:** `GHz, Time`

---

### Delay

延迟（毫秒）

        Args:
            ms: 延迟时间（毫秒）

        Returns:
            1表示成功

        Example:
            # 延迟1秒
            vu.Delay(1000)

**参数:** `ms`

---

### GetTime

GetTime函数

---

### Is64Bit

Is64Bit函数

---

### GetScreenHeight

GetScreenHeight函数

---

### GetScreenWidth

获取屏幕宽度

        Returns:
            屏幕宽度（像素）

        Example:
            # 获取屏幕尺寸
            width = vu.GetScreenWidth()
            height = vu.GetScreenHeight()
            print(f"屏幕分辨率: {width}x{height}")

---

### SetScreen

SetScreen函数

**参数:** `Width, Height`

---

### SetUAC

SetUAC函数

**参数:** `enable`

---

### GetOsType

GetOsType函数

---

### SysExitOs

SysExitOs函数

**参数:** `type`

---

### IsSurrpotVt

IsSurrpotVt函数

---

### GetCpuName

GetCpuName函数

---

### GetGpuName

GetGpuName函数

---

### GetCpuUsage

GetCpuUsage函数

---

### GetMemUsage

GetMemUsage函数

---

### GetGpuUsage

GetGpuUsage函数

---

### GetGpuMemUsage

GetGpuMemUsage函数

---

### GetGpuMemShareUsage

GetGpuMemShareUsage函数

---

### GetDiskSerial

GetDiskSerial函数

---

### Play

Play函数

**参数:** `media_file`

---

### Stop

Stop函数

**参数:** `id`

---

### ExecuteCmd

ExecuteCmd函数

**参数:** `cmd_str, current_dir, time_out`

---

### InitCri

InitCri函数

---

### EnterCriTry

EnterCriTry函数

---

### EnterCri

EnterCri函数

---

### LeaveCri

LeaveCri函数

---

### SetExitThread

SetExitThread函数

**参数:** `mode`

---

### SetThreadStatus

SetThreadStatus函数

**参数:** `status`

---

### ClientToScreen

ClientToScreen函数

**参数:** `hwnd, x, y`

---

### ScreenToClient

ScreenToClient函数

**参数:** `hwnd, x, y`

---

### EnumWindowByProcess

EnumWindowByProcess函数

**参数:** `process_name, title, class_name, filter`

---

### EnumWindowByProcessId

EnumWindowByProcessId函数

**参数:** `pid, title, class_name, filter`

---

### EnumWindowSuper

EnumWindowSuper函数

**参数:** `spec1, flag1, type1, spec2, flag2, type2, sort`

---

### FindWindowSuper

FindWindowSuper函数

**参数:** `spec1, flag1, type1, spec2, flag2, type2`

---

### GetForegroundFocus

GetForegroundFocus函数

---

### GetForegroundWindow

GetForegroundWindow函数

---

### GetWindow

GetWindow函数

**参数:** `hwnd, flag`

---

### GetWindowClass

GetWindowClass函数

**参数:** `hwnd`

---

### GetWindowProcessId

GetWindowProcessId函数

**参数:** `hwnd`

---

### GetWindowThreadId

GetWindowThreadId函数

**参数:** `hwnd`

---

### GetWindowProcessPath

GetWindowProcessPath函数

**参数:** `hwnd`

---

### GetWindowRectSize

GetWindowRectSize函数

**参数:** `hwnd, x, y, w, h, type`

---

### GetWindowBorder

GetWindowBorder函数

**参数:** `hwnd, width, height`

---

### MoveWindow

MoveWindow函数

**参数:** `hwnd, x, y`

---

### SendPaste

SendPaste函数

**参数:** `hwnd`

---

### SendString2

SendString2函数

**参数:** `hwnd, str`

---

### SetClientSize

SetClientSize函数

**参数:** `hwnd, width, height`

---

### SetWindowRectSize

SetWindowRectSize函数

**参数:** `hwnd, x, y, width, height, type`

---

### SetWindowTransparent

SetWindowTransparent函数

**参数:** `hwnd, trans`

---

### WindowIsHunging

WindowIsHunging函数

**参数:** `hwnd, time`

---

### GetCommandLine

GetCommandLine函数

**参数:** `pid`

---

### ProcessGetPath

ProcessGetPath函数

**参数:** `pid`

---

### ProcessGetName

ProcessGetName函数

**参数:** `pid`

---

### EnumModules

EnumModules函数

**参数:** `pid`

---

### ProcessCreate

ProcessCreate函数

**参数:** `file, cmdLine, showType, waitForEnd`

---

### TerminateProcess

TerminateProcess函数

**参数:** `pid`

---

### TerminateProcessTree

TerminateProcessTree函数

**参数:** `pid`

---

### ProcessIsAliving

ProcessIsAliving函数

**参数:** `pid`

---

### ProcessIsHunging

ProcessIsHunging函数

**参数:** `pid`

---

### ProcessGetCurrentPid

ProcessGetCurrentPid函数

---

### ProcessIsX64

ProcessIsX64函数

**参数:** `pid`

---

### ProcessSetIsSuspend

ProcessSetIsSuspend函数

**参数:** `pid, isSuspend`

---

### SetMemoryHwndAsProcessId

SetMemoryHwndAsProcessId函数

**参数:** `en`

---

### GetModuleBaseAddr

GetModuleBaseAddr函数

**参数:** `hwnd, module`

---

### GetModuleSize

GetModuleSize函数

**参数:** `hwnd, module`

---

### GetRemoteApiAddress

GetRemoteApiAddress函数

**参数:** `hwnd, base_addr, fun_name`

---

### VirtualAllocEx

VirtualAllocEx函数

**参数:** `hwnd, addr, size, type`

---

### VirtualFreeEx

VirtualFreeEx函数

**参数:** `hwnd, addr`

---

### VirtualProtectEx

VirtualProtectEx函数

**参数:** `hwnd, addr, size, type, new_protect`

---

### VirtualQueryEx

VirtualQueryEx函数

**参数:** `hwnd, addr`

---

### ReadDataAddrToBin

ReadDataAddrToBin函数

**参数:** `hwnd, addr, len`

---

### ReadDataAddr

ReadDataAddr函数

**参数:** `hwnd, addr, len`

---

### ReadData

ReadData函数

**参数:** `hwnd, addr, len`

---

### ReadDataToBin

ReadDataToBin函数

**参数:** `hwnd, addr, len`

---

### ReadDoubleAddr

ReadDoubleAddr函数

**参数:** `hwnd, addr`

---

### ReadFloatAddr

ReadFloatAddr函数

**参数:** `hwnd, addr`

---

### ReadIntAddr

ReadIntAddr函数

**参数:** `hwnd, addr, type`

---

### ReadStringAddr

ReadStringAddr函数

**参数:** `hwnd, addr, type, len`

---

### WriteDataAddrFromBin

WriteDataAddrFromBin函数

**参数:** `hwnd, addr, data, len`

---

### WriteDataFromBin

WriteDataFromBin函数

**参数:** `hwnd, addr, data, len`

---

### WriteDataAddr

WriteDataAddr函数

**参数:** `hwnd, addr, data`

---

### WriteData

WriteData函数

**参数:** `hwnd, addr, data`

---

### WriteDoubleAddr

WriteDoubleAddr函数

**参数:** `hwnd, addr, data`

---

### WriteFloatAddr

WriteFloatAddr函数

**参数:** `hwnd, addr, data`

---

### WriteIntAddr

WriteIntAddr函数

**参数:** `hwnd, addr, type, data`

---

### WriteStringAddr

WriteStringAddr函数

**参数:** `hwnd, addr, type, data`

---

### DataToBytes

DataToBytes函数

**参数:** `data, len`

---

### BytesToData

BytesToData函数

**参数:** `pBuf, len`

---

### DoubleToData

DoubleToData函数

**参数:** `value`

---

### FloatToData

FloatToData函数

**参数:** `value`

---

### IntToData

IntToData函数

**参数:** `value, type`

---

### StringToData

StringToData函数

**参数:** `value, type`

---

### FindDataEx

FindDataEx函数

**参数:** `hwnd, addr_range, data, step, multi_thread, mode`

---

### FindData

FindData函数

**参数:** `hwnd, addr_range, data`

---

### FindDoubleEx

FindDoubleEx函数

**参数:** `hwnd, addr_range, minV, maxV, step, multi_thread, mode`

---

### FindFloatEx

FindFloatEx函数

**参数:** `hwnd, addr_range, minV, maxV, step, multi_thread, mode`

---

### FindIntEx

FindIntEx函数

**参数:** `hwnd, addr_range, minV, maxV, type, step, multi_thread, mode`

---

### FindStringEx

FindStringEx函数

**参数:** `hwnd, addr_range, string_value, type, step, multi_thread, mode`

---

### WriteDataAddrFromBinNoTrace

WriteDataAddrFromBinNoTrace函数

**参数:** `hwnd, addr, data, len`

---

### WriteDataFromBinNoTrace

WriteDataFromBinNoTrace函数

**参数:** `hwnd, addr, data, len`

---

### WriteDataAddrNoTrace

WriteDataAddrNoTrace函数

**参数:** `hwnd, addr, data`

---

### WriteDataNoTrace

WriteDataNoTrace函数

**参数:** `hwnd, addr, data`

---

### DataAddrCancelNoTrace

DataAddrCancelNoTrace函数

**参数:** `hwnd, addr`

---

### DataCancelNoTrace

DataCancelNoTrace函数

**参数:** `hwnd, addr`

---

### InjectFileData

InjectFileData函数

**参数:** `hwnd, file_data, len`

---

### InjectFile

InjectFile函数

**参数:** `hwnd, path`

---

### HookCreateAddr

HookCreateAddr函数

**参数:** `hwnd, addrFrom, addrTo`

---

### HookCreate

HookCreate函数

**参数:** `hwnd, addrFrom, addrTo`

---

### HookStartAddr

HookStartAddr函数

**参数:** `hwnd, addrFrom, isNoTrace`

---

### HookStart

HookStart函数

**参数:** `hwnd, addrFrom, isNoTrace`

---

### HookStopAddr

HookStopAddr函数

**参数:** `hwnd, addrFrom`

---

### HookStop

HookStop函数

**参数:** `hwnd, addrFrom`

---

### AsmAdd

AsmAdd函数

**参数:** `asm_ins`

---

### AsmClear

AsmClear函数

---

### Assemble

Assemble函数

**参数:** `base_addr, is_64bit`

---

### DisAssemble

DisAssemble函数

**参数:** `asm_code, base_addr, is_64bit`

---

### AsmMemAlloc

AsmMemAlloc函数

**参数:** `hwnd, retAddr, retSize`

---

### AsmMemFree

AsmMemFree函数

**参数:** `hwnd, addr`

---

### AsmCallEx

AsmCallEx函数

**参数:** `hwnd, mode, base_addr`

---

### AsmCall

AsmCall函数

**参数:** `hwnd, mode`

---

### SetAsmHwndAsProcessId

SetAsmHwndAsProcessId函数

**参数:** `enable`

---

### SetShowAsmErrorMsg

SetShowAsmErrorMsg函数

**参数:** `show`

---

### GuardInstall

GuardInstall函数

**参数:** `mode`

---

### GuardFolder

GuardFolder函数

**参数:** `path, enable`

---

### GuardFile

GuardFile函数

**参数:** `path, enable`

---

### GuardProcess

GuardProcess函数

**参数:** `pid, enable, hide`

---

### GuardWindow

GuardWindow函数

**参数:** `hwnd, enable, display`

---

### GuardDisk

GuardDisk函数

**参数:** `Serial_Number`

---

### GuardMAC

GuardMAC函数

**参数:** `Serial_Number`

---

### GuardBOIS

GuardBOIS函数

**参数:** `Serial_Number`

---

### GuardGPU

GuardGPU函数

**参数:** `Serial_Number`

---

### GuardEnvironment

GuardEnvironment函数

**参数:** `exeName, title`

---

### GuardRegistry

GuardRegistry函数

**参数:** `pid, section, key, data, len`

---

### GuardRegistryData

GuardRegistryData函数

**参数:** `pid, section, key, data`

---

### GuardKillHandle

GuardKillHandle函数

**参数:** `pid, type, name`

---

### AStartLoadMapData

AStartLoadMapData函数

**参数:** `pData, isInvert`

---

### AStartLoadMapFile

AStartLoadMapFile函数

**参数:** `file, isInvert`

---

### AStartDestroy

AStartDestroy函数

---

### AStartSet

AStartSet函数

**参数:** `dir, beeline, diagonal, isCenter`

---

### AStartFindWay

AStartFindWay函数

**参数:** `beginX, beginY, endX, endY, intX, intY`

---

### AStartNextWay

AStartNextWay函数

**参数:** `currentX, currentY, intX, intY, dir`

---

### AiFindPic

AiFindPic函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir, intX, intY`

---

### AiFindPicS

AiFindPicS函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir, intX, intY`

---

### AiFindPicE

AiFindPicE函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir`

---

### AiFindPicEx

AiFindPicEx函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir`

---

### AiFindPicExS

AiFindPicExS函数

**参数:** `x1, y1, x2, y2, pic_name, sim, dir`

---

### AiFindPicMem

AiFindPicMem函数

**参数:** `x1, y1, x2, y2, pic_info, sim, dir, intX, intY`

---

### AiFindPicMemE

AiFindPicMemE函数

**参数:** `x1, y1, x2, y2, pic_info, sim, dir`

---

### AiFindPicMemEx

AiFindPicMemEx函数

**参数:** `x1, y1, x2, y2, pic_info, sim, dir`

---

### AiFindPicSuper

AiFindPicSuper函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin, intX, intY`

---

### AiFindPicSuperS

AiFindPicSuperS函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin, intX, intY`

---

### AiFindPicSuperE

AiFindPicSuperE函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin`

---

### AiFindPicSuperEx

AiFindPicSuperEx函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin`

---

### AiFindPicSuperExS

AiFindPicSuperExS函数

**参数:** `x1, y1, x2, y2, pic_name, sim, detMode, isBin`

---

### AiFindPicSuperMem

AiFindPicSuperMem函数

**参数:** `x1, y1, x2, y2, pic_info, sim, detMode, isBin, intX, intY`

---

### AiFindPicSuperMemE

AiFindPicSuperMemE函数

**参数:** `x1, y1, x2, y2, pic_info, sim, detMode, isBin`

---

### AiFindPicSuperMemEx

AiFindPicSuperMemEx函数

**参数:** `x1, y1, x2, y2, pic_info, sim, detMode, isBin`

---

### AiYoloSetModel

AiYoloSetModel函数

**参数:** `index, file`

---

### AiYoloSetModelMemory

AiYoloSetModelMemory函数

**参数:** `index, data, size`

---

### AiYoloUseModel

AiYoloUseModel函数

**参数:** `index`

---

### AiYoloDetectObjects

AiYoloDetectObjects函数

**参数:** `x1, y1, x2, y2, prob, iou`

---

### AiOcrSetModel

AiOcrSetModel函数

**参数:** `index, det_model, rec_model, rec_dict`

---

### AiOcrUseModel

AiOcrUseModel函数

**参数:** `index`

---

### AiOcrDetectObjects

AiOcrDetectObjects函数

**参数:** `x1, y1, x2, y2`

---

### AiTableSetModel

AiTableSetModel函数

**参数:** `index, det_model, rec_model, rec_dict, table_model, table_dict, layout_model, layout_dict`

---

### AiTableUseModel

AiTableUseModel函数

**参数:** `index`

---

### AiTableDetectObjects

AiTableDetectObjects函数

**参数:** `x1, y1, x2, y2`

---

### JsonReadInPut

JsonReadInPut函数

**参数:** `str`

---

### JsonReadGetObjType

JsonReadGetObjType函数

**参数:** `obj`

---

### JsonReadGetObjSize

JsonReadGetObjSize函数

**参数:** `obj`

---

### JsonReadGetValObjByKey

JsonReadGetValObjByKey函数

**参数:** `obj, key`

---

### JsonReadGetValObjByIndex

JsonReadGetValObjByIndex函数

**参数:** `obj, index`

---

### JsonReadGetKeyObj

JsonReadGetKeyObj函数

**参数:** `obj, index`

---

### JsonReadGetNum

JsonReadGetNum函数

**参数:** `obj`

---

### JsonReadGetStr

JsonReadGetStr函数

**参数:** `obj`

---

### JsonReadGetArraySize

JsonReadGetArraySize函数

**参数:** `obj`

---

### JsonReadGetArrayObj

JsonReadGetArrayObj函数

**参数:** `obj, index`

---

### JsonWriteClear

JsonWriteClear函数

---

### JsonWriteCreateObj

JsonWriteCreateObj函数

---

### JsonWriteAddStr

JsonWriteAddStr函数

**参数:** `pJson, key, val`

---

### JsonWriteAddNum

JsonWriteAddNum函数

**参数:** `pJson, key, val`

---

### JsonWriteAddArray

JsonWriteAddArray函数

**参数:** `pJson, key, arr`

---

### JsonWriteAddObj

JsonWriteAddObj函数

**参数:** `pJson, key, obj`

---

### JsonWriteCreateArray

JsonWriteCreateArray函数

**参数:** `pJson`

---

### JsonWriteArrayAddStr

JsonWriteArrayAddStr函数

**参数:** `arr, val`

---

### JsonWriteArrayAddNum

JsonWriteArrayAddNum函数

**参数:** `arr, val`

---

### JsonWriteArrayAddArray

JsonWriteArrayAddArray函数

**参数:** `arr, val_arr`

---

### JsonWriteArrayAddObj

JsonWriteArrayAddObj函数

**参数:** `arr, obj`

---

### JsonWriteDeleteKey

JsonWriteDeleteKey函数

**参数:** `pJson, key`

---

### JsonWriteOutPut

JsonWriteOutPut函数

**参数:** `pJson`

---

### Rgb2String

Rgb2String函数

**参数:** `rgb`

---

### Rgb2Hsv

Rgb2Hsv函数

**参数:** `rgb, h, s, v`

---

### Hsv2Rgb

Hsv2Rgb函数

**参数:** `h, s, v`

---

### ImgFindPic

ImgFindPic函数

**参数:** `pLarge, pSmall, isFast, dir, sim, matchMethod`

---

### ImgFindPicSuper

ImgFindPicSuper函数

**参数:** `pLarge, pSmall, isFast, detMode, matchThresh, showDbg`

---

### ImgGetImgObj

ImgGetImgObj函数

**参数:** `id`

---

### ImgGetImgObjEx

ImgGetImgObjEx函数

**参数:** `id, alpha_rgb, offset_rgb`

---

### ImgCopy

ImgCopy函数

**参数:** `id, pImg`

---

### ImgGetCopy

ImgGetCopy函数

**参数:** `id`

---

### ImgPolyGetPointsRange

ImgPolyGetPointsRange函数

**参数:** `id`

---

### ImgContoursGetPoints

ImgContoursGetPoints函数

**参数:** `id, index`

---

### ImgContoursGetPointsSimplify

ImgContoursGetPointsSimplify函数

**参数:** `id, index, epsilon`

---

### ImgMaskSelected

ImgMaskSelected函数

**参数:** `id`

---

### ImgMaskCircle

ImgMaskCircle函数

**参数:** `id, x, y, radius, isGradient`

---

### ImgMaskRect

ImgMaskRect函数

**参数:** `id, x1, y1, x2, y2, isGradient`

---

### ImgMaskPoly

ImgMaskPoly函数

**参数:** `id`

---

### ImgMaskInvert

ImgMaskInvert函数

**参数:** `id, pMask`

---

### ImgOperator

ImgOperator函数

**参数:** `id, mode, pObj1, pObj2, pMask`

---

### LlmGetResponse

LlmGetResponse函数

**参数:** `is_end`

---

### LlmGetToolCall

LlmGetToolCall函数

**参数:** `count`

---

### AudioGetDeviceList

AudioGetDeviceList函数

---

### AudioGetDeviceDefault

AudioGetDeviceDefault函数

**参数:** `mode`

---

### AudioRecordGetStreamInfo

AudioRecordGetStreamInfo函数

**参数:** `channelse, sampleRate`

---

### AudioGetStreamSize

AudioGetStreamSize函数

**参数:** `mode`

---

### SndAsr

SndAsr函数

**参数:** `index, buf, num_samples, sample_rate, isFinished`

---

### SndGetStream

SndGetStream函数

**参数:** `index, samples, num_samples`

---

### SndGetError

SndGetError函数

**参数:** `index`

---

### DrawGetError

DrawGetError函数

---

### DrawCreate

DrawCreate函数

**参数:** `x, y, w, h, isFast`

---

### DrawCreateByWindow

DrawCreateByWindow函数

**参数:** `hTarget`

---

### DrawSetStyle

DrawSetStyle函数

**参数:** `isThrough, alpha`

---

### DrawSetPosition

DrawSetPosition函数

**参数:** `isShow, x, y, w, h`

---

### DrawRun

DrawRun函数

---

### DrawStop

DrawStop函数

---

### DrawIsRunning

DrawIsRunning函数

---

### DrawGetFps

DrawGetFps函数

---

### DrawClear

DrawClear函数

---

### DrawRender

DrawRender函数

---

### DrawString

DrawString函数

**参数:** `str, x, y, rgb, alpha, fontFamilyName, fontWeight, fontStyle, fontSize`

---

### DrawLine

DrawLine函数

**参数:** `x1, y1, x2, y2, rgb, alpha, lineWidth`

---

### DrawPolygon

DrawPolygon函数

**参数:** `x, y, rgb, alpha, mode`

---

### DrawRectangle

DrawRectangle函数

**参数:** `x1, y1, x2, y2, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode`

---

### DrawEllipse

DrawEllipse函数

**参数:** `x, y, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode`

---

### DrawImgLoad

DrawImgLoad函数

**参数:** `id, pImg, nImgSize`

---

### DrawImgRemove

DrawImgRemove函数

**参数:** `id`

---

### DrawImgClear

DrawImgClear函数

---

### DrawImg

DrawImg函数

**参数:** `id, x, y, w, h, alpha, maintain`

---


## 统计信息

- 总分类数: 12
- 总函数数: 760
- 文档行数: 约 7600 行

---

*文档生成时间: 2025-11-12*
