@echo off
chcp 65001 >nul
title 安装项目依赖

echo ========================================
echo 自动化工作流 - 依赖安装脚本
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python环境
    echo 请先从 https://www.python.org/ 下载并安装Python 3.8或更高版本
    echo.
    pause
    exit /b 1
)

echo [信息] 检测到Python环境:
python --version
echo.

REM 升级pip到最新版本
echo [步骤1/3] 正在升级pip到最新版本...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo [警告] pip升级失败，继续使用当前版本
) else (
    echo [完成] pip升级成功
)
echo.

REM 安装核心依赖
echo [步骤2/3] 正在安装核心依赖库...
echo.
echo 安装GUI框架 (PySide6)...
python -m pip install PySide6
echo.
echo 安装图像处理库 (OpenCV, Pillow, numpy)...
python -m pip install opencv-python pillow numpy
echo.
echo 安装屏幕操作库 (pyautogui, mss)...
python -m pip install pyautogui mss
echo.
echo 安装Windows操作库 (pywin32)...
python -m pip install pywin32
echo.

REM 安装可选依赖
echo [步骤3/3] 正在安装可选依赖库...
echo.
echo 安装快捷键支持 (keyboard)...
python -m pip install keyboard
echo.
echo 安装OCR支持 (paddleocr, paddlepaddle)...
python -m pip install paddleocr paddlepaddle
echo.

REM 检查安装结果
echo.
echo ========================================
echo 正在验证安装结果...
echo ========================================
echo.

python -c "import PySide6; print('[✓] PySide6 已安装')" 2>nul || echo [✗] PySide6 安装失败
python -c "import cv2; print('[✓] OpenCV 已安装')" 2>nul || echo [✗] OpenCV 安装失败
python -c "import PIL; print('[✓] Pillow 已安装')" 2>nul || echo [✗] Pillow 安装失败
python -c "import numpy; print('[✓] NumPy 已安装')" 2>nul || echo [✗] NumPy 安装失败
python -c "import pyautogui; print('[✓] PyAutoGUI 已安装')" 2>nul || echo [✗] PyAutoGUI 安装失败
python -c "import mss; print('[✓] MSS 已安装')" 2>nul || echo [✗] MSS 安装失败
python -c "import win32api; print('[✓] pywin32 已安装')" 2>nul || echo [✗] pywin32 安装失败
python -c "import keyboard; print('[✓] keyboard 已安装')" 2>nul || echo [✗] keyboard 安装失败
python -c "import paddleocr; print('[✓] PaddleOCR 已安装')" 2>nul || echo [✗] PaddleOCR 安装失败

echo.
echo ========================================
echo 依赖安装完成！
echo ========================================
echo.
echo 如果所有依赖都显示 [✓]，则可以运行程序
echo 如果有依赖显示 [✗]，请手动安装对应的库
echo.
echo 常见问题解决：
echo 1. 如果安装过程中出现权限错误，请以管理员身份运行此脚本
echo 2. 如果安装速度很慢，可以使用国内镜像源：
echo    python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple [包名]
echo 3. 如果PaddleOCR安装失败，这是可选组件，不影响基本功能
echo.
pause