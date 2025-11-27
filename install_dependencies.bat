@echo off
chcp 65001 >nul

echo ========================================
echo Python 版本检测与依赖安装
echo ========================================
echo.

set "PYTHON_EXE=C:\Users\x\AppData\Local\Programs\Python\Python314\python.exe"

if not exist "%PYTHON_EXE%" (
    echo [错误] 未找到 Python 3.14
    echo 路径: %PYTHON_EXE%
    echo.
    echo 请确认 Python 3.14 已正确安装
    pause
    exit /b 1
)

echo [成功] 将使用 Python 3.14
echo 路径: %PYTHON_EXE%
echo.
echo ========================================
echo 开始安装依赖包...
echo ========================================
echo.

echo [1/7] 升级 pip...
"%PYTHON_EXE%" -m pip install --upgrade pip

echo.
echo [2/11] 安装 PySide6...
"%PYTHON_EXE%" -m pip install PySide6

echo.
echo [3/11] 安装 numpy...
"%PYTHON_EXE%" -m pip install numpy

echo.
echo [4/11] 安装 psutil...
"%PYTHON_EXE%" -m pip install psutil

echo.
echo [5/11] 安装 keyboard...
"%PYTHON_EXE%" -m pip install keyboard

echo.
echo [6/11] 安装 wmi...
"%PYTHON_EXE%" -m pip install wmi

echo.
echo [7/11] 安装 pywin32...
"%PYTHON_EXE%" -m pip install pywin32

echo.
echo [8/11] 安装 opencv-python...
"%PYTHON_EXE%" -m pip install opencv-python

echo.
echo [9/11] 安装 pyautogui...
"%PYTHON_EXE%" -m pip install pyautogui

echo.
echo [10/11] 安装 Pillow...
"%PYTHON_EXE%" -m pip install Pillow

echo.
echo [11/11] 安装 mss...
"%PYTHON_EXE%" -m pip install mss

echo.
echo ========================================
echo 验证安装结果...
echo ========================================
echo.

"%PYTHON_EXE%" check_dependencies.py

echo.
echo 安装完成!
pause