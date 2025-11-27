@echo off
chcp 65001 >nul
echo ========================================
echo 正在检测系统中已安装的Python版本...
echo ========================================
echo.

set found=0

echo [1] 检查PATH环境变量中的Python:
echo ----------------------------------------
where python >nul 2>&1
if %errorlevel% equ 0 (
    for /f "delims=" %%i in ('where python') do (
        echo 找到: %%i
        "%%i" --version 2>&1
        echo.
        set found=1
    )
) else (
    echo 未在PATH中找到python命令
    echo.
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    for /f "delims=" %%i in ('where python3') do (
        echo 找到: %%i
        "%%i" --version 2>&1
        echo.
        set found=1
    )
)

echo [2] 检查常见安装目录:
echo ----------------------------------------
for %%d in (
    "C:\Python*"
    "C:\Program Files\Python*"
    "C:\Program Files (x86)\Python*"
    "%LOCALAPPDATA%\Programs\Python\Python*"
    "%APPDATA%\Local\Programs\Python\Python*"
) do (
    if exist %%d\python.exe (
        echo 找到: %%d\python.exe
        "%%d\python.exe" --version 2>&1
        echo.
        set found=1
    )
)

echo [3] 检查注册表中的Python安装:
echo ----------------------------------------
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Python\PythonCore" /s /v InstallPath 2>nul | findstr "InstallPath" >nul
if %errorlevel% equ 0 (
    for /f "tokens=2*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Python\PythonCore" /s /v InstallPath 2^>nul ^| findstr "REG_SZ"') do (
        if exist "%%b\python.exe" (
            echo 找到: %%b\python.exe
            "%%b\python.exe" --version 2>&1
            echo.
            set found=1
        )
    )
) else (
    echo 注册表中未找到Python安装信息
    echo.
)

reg query "HKEY_CURRENT_USER\SOFTWARE\Python\PythonCore" /s /v InstallPath 2>nul | findstr "InstallPath" >nul
if %errorlevel% equ 0 (
    for /f "tokens=2*" %%a in ('reg query "HKEY_CURRENT_USER\SOFTWARE\Python\PythonCore" /s /v InstallPath 2^>nul ^| findstr "REG_SZ"') do (
        if exist "%%b\python.exe" (
            echo 找到: %%b\python.exe
            "%%b\python.exe" --version 2>&1
            echo.
            set found=1
        )
    )
)

echo [4] 检查py启动器:
echo ----------------------------------------
py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo 找到py启动器,列出所有可用版本:
    py -0 2>&1
    echo.
    set found=1
) else (
    echo 未找到py启动器
    echo.
)

echo ========================================
if %found% equ 0 (
    echo 未找到任何Python安装
) else (
    echo 检测完成!
)
echo ========================================
echo.
pause