@echo off
title Workforce Planning Dashboards
color 0A

echo ========================================
echo   WORKFORCE PLANNING DASHBOARDS
echo ========================================
echo.
echo Select an option:
echo.
echo 1. Generate Static HTML Dashboard
echo 2. Launch Interactive Streamlit Dashboard
echo 3. Install Dependencies
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto static
if "%choice%"=="2" goto streamlit
if "%choice%"=="3" goto install
if "%choice%"=="4" goto end

:static
echo.
echo Generating static dashboard...
python create_dashboard.py
echo.
pause
goto end

:streamlit
echo.
echo Launching interactive dashboard...
echo.
echo Dashboard will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.
streamlit run streamlit_app.py
pause
goto end

:install
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Installation complete!
pause
goto end

:end
exit
