@echo off
setlocal enabledelayedexpansion

:: --- Configuration ---
set "max_files=50"
:: ---------------------

set "root_path=%cd%"
echo Starting to process folder: "%root_path%"
echo Each subfolder will contain a maximum of %max_files% files.
echo.

set "temp_dir_list=%TEMP%\dirlist_%RANDOM%.tmp"

(
    echo %root_path%
    dir /b /s /ad "%root_path%"
) > "%temp_dir_list%" 2>nul

for /f "delims=" %%d in ('sort /r "%temp_dir_list%"') do (
    call :process_folder "%%d"
)

del "%temp_dir_list%"

echo.
echo ====================
echo      All tasks have been completed!
echo ====================
echo.
pause
goto :eof


:process_folder
    set "current_folder=%~1"
    
    set /a total_files=0
    for %%f in ("%current_folder%\*") do (
        if not exist "%%f\" (
            set /a total_files+=1
        )
    )

    if !total_files! LEQ %max_files% (
        goto :eof
    )

    echo Processing: "!current_folder!"
    echo   Found !total_files! files, starting to create batches...

    set /a file_count=0
    set /a dir_count=1
    
    for /f "delims=" %%f in ('dir /b /a-d "%current_folder%\*"') do (
        
        if /i not "%%f"=="%~nx0" (
            
            set "dest_dir=%current_folder%\batch_!dir_count!"
            
            if not exist "!dest_dir!" (
                md "!dest_dir!"
            )

            move "%current_folder%\%%f" "!dest_dir!" > nul

            set /a file_count+=1

            if !file_count! equ %max_files% (
                set /a file_count=0
                set /a dir_count+=1
            )
        )
    )
goto :eof
