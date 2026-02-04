@echo off
echo ========================================
echo  PROJECT CLEANUP SCRIPT
echo  Removing unnecessary cache files only
echo ========================================
echo.

echo [1/4] Removing Jupyter checkpoint folders...
for /d /r . %%d in (.ipynb_checkpoints) do (
    if exist "%%d" (
        echo   Removing: %%d
        rmdir /s /q "%%d"
    )
)

echo.
echo [2/4] Removing Python cache folders...
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        echo   Removing: %%d
        rmdir /s /q "%%d"
    )
)

echo.
echo [3/4] Removing system files...
del /s /q .DS_Store 2>nul
del /s /q Thumbs.db 2>nul
del /s /q desktop.ini 2>nul

echo.
echo [4/4] Removing empty folders (if any)...
if exist "notebooks\" (
    echo   Checking notebooks folder...
    dir /b "notebooks\" | findstr /r /c:"." >nul
    if errorlevel 1 (
        echo   Removing empty notebooks folder...
        rmdir "notebooks\"
    ) else (
        echo   notebooks folder not empty, keeping it
    )
)

if exist "reports\" (
    echo   Checking reports folder...
    dir /b "reports\" | findstr /r /c:"[^README]" >nul
    if errorlevel 1 (
        echo   reports folder only has README, keeping for structure
    )
)

echo.
echo ========================================
echo  CLEANUP COMPLETE!
echo ========================================
echo.
echo ✅ Removed: Jupyter checkpoints
echo ✅ Removed: Python cache
echo ✅ Removed: System files
echo.
echo ✅ KEPT: EDA notebook
echo ✅ KEPT: Static outputs
echo ✅ KEPT: Dashboards
echo ✅ KEPT: All data files
echo ✅ KEPT: All documentation
echo.
echo Your project is now clean!
echo.
pause
