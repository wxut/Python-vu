@echo off
chcp 65001 >nul
title 自动化工作流程序

echo ========================================
echo 正在启动自动化工作流程序...
echo ========================================
echo.

REM 查找 Python 3.14
set "PYTHON_EXE="

REM 尝试 py launcher
where py >nul 2>&1
if %errorlevel% equ 0 (
    py -3.14 --version >nul 2>&1
    if !errorlevel! equ 0 (
        for /f "tokens=*" %%p in ('py -3.14 -c "import sys; print(sys.executable)" 2^>nul') do set "PYTHON_EXE=%%p"
    )
)

REM 检查常见路径
if not defined PYTHON_EXE (
    for %%p in (
        "C:\Python314\python.exe"
        "C:\Program Files\Python314\python.exe"
        "%LOCALAPPDATA%\Programs\Python\Python314\python.exe"
    ) do (
        if exist %%p set "PYTHON_EXE=%%p"
    )
)

REM 如果未找到 3.14,使用默认 python
if not defined PYTHON_EXE (
    where python >nul 2>&1
    if !errorlevel! equ 0 (
        set "PYTHON_EXE=python"
    ) else (
        echo [错误] 未检测到Python环境
        echo 请先安装Python 3.14或更高版本
        echo.
        pause
        exit /b 1
    )
)

echo [信息] 使用 Python: %PYTHON_EXE%
"%PYTHON_EXE%" --version
echo.

REM 检查main.py是否存在
if not exist "main.py" (
    echo [错误] 找不到main.py文件
    echo 请确保在项目根目录下运行此脚本
    echo.
    pause
    exit /b 1
)

REM 启动程序
echo [启动] 正在运行程序...
echo.
"%PYTHON_EXE%" main.py

REM 程序退出后的处理
echo.
echo ========================================
echo 程序已退出
echo ========================================
pause