@echo off
echo ========================================
echo  Cleaning up unnecessary files...
echo ========================================
echo.

REM Remove __pycache__ folder
if exist "__pycache__\" (
    echo [1/2] Removing __pycache__ folder...
    rmdir /s /q "__pycache__"
    echo       ✓ Removed __pycache__
) else (
    echo       ✓ __pycache__ already removed
)

echo.
echo [2/2] Verifying clean structure...
dir /b

echo.
echo ========================================
echo  Cleanup Complete!
echo ========================================
echo.
echo All files are now properly organized.
echo Only essential files remain.
echo.
pause
