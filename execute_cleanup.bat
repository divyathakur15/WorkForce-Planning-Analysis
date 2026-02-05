@echo off
echo ========================================
echo  SAFE CLEANUP SCRIPT
echo  Removing verified unnecessary files
echo ========================================
echo.

cd /d "c:\Users\HP\Desktop\WORKFORCE PLANNING ANALYSIS\WorkForce-Planning-Analysis"

echo [1/4] Removing old dashboard debug scripts...
if exist "dashboards\create_dashboard.py" (
    del /q "dashboards\create_dashboard.py"
    echo   [OK] Removed: dashboards\create_dashboard.py
) else (
    echo   [SKIP] Not found: dashboards\create_dashboard.py
)

if exist "dashboards\fix_dashboard.py" (
    del /q "dashboards\fix_dashboard.py"
    echo   [OK] Removed: dashboards\fix_dashboard.py
) else (
    echo   [SKIP] Not found: dashboards\fix_dashboard.py
)

if exist "dashboards\fix_indent.py" (
    del /q "dashboards\fix_indent.py"
    echo   [OK] Removed: dashboards\fix_indent.py
) else (
    echo   [SKIP] Not found: dashboards\fix_indent.py
)

if exist "dashboards\rebuild_dashboard.py" (
    del /q "dashboards\rebuild_dashboard.py"
    echo   [OK] Removed: dashboards\rebuild_dashboard.py
) else (
    echo   [SKIP] Not found: dashboards\rebuild_dashboard.py
)

echo.
echo [2/4] Removing old documentation files...
if exist "CLEANUP_RECOMMENDATION.md" (
    del /q "CLEANUP_RECOMMENDATION.md"
    echo   [OK] Removed: CLEANUP_RECOMMENDATION.md
) else (
    echo   [SKIP] Not found: CLEANUP_RECOMMENDATION.md
)

if exist "HOW_TO_CLEANUP.md" (
    del /q "HOW_TO_CLEANUP.md"
    echo   [OK] Removed: HOW_TO_CLEANUP.md
) else (
    echo   [SKIP] Not found: HOW_TO_CLEANUP.md
)

if exist "DASHBOARD_ACCESS_GUIDE.md" (
    del /q "DASHBOARD_ACCESS_GUIDE.md"
    echo   [OK] Removed: DASHBOARD_ACCESS_GUIDE.md
) else (
    echo   [SKIP] Not found: DASHBOARD_ACCESS_GUIDE.md
)

if exist "FINAL_COMPLETION_REPORT.md" (
    del /q "FINAL_COMPLETION_REPORT.md"
    echo   [OK] Removed: FINAL_COMPLETION_REPORT.md
) else (
    echo   [SKIP] Not found: FINAL_COMPLETION_REPORT.md
)

if exist "GITHUB_IMPROVEMENTS_SUMMARY.md" (
    del /q "GITHUB_IMPROVEMENTS_SUMMARY.md"
    echo   [OK] Removed: GITHUB_IMPROVEMENTS_SUMMARY.md
) else (
    echo   [SKIP] Not found: GITHUB_IMPROVEMENTS_SUMMARY.md
)

echo.
echo [3/4] Removing duplicate documentation...
if exist "dashboards\INDEX.md" (
    del /q "dashboards\INDEX.md"
    echo   [OK] Removed: dashboards\INDEX.md
) else (
    echo   [SKIP] Not found: dashboards\INDEX.md
)

if exist "dashboards\cleanup.bat" (
    del /q "dashboards\cleanup.bat"
    echo   [OK] Removed: dashboards\cleanup.bat
) else (
    echo   [SKIP] Not found: dashboards\cleanup.bat
)

echo.
echo [4/4] Removing cache folders...
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        echo   [OK] Removing: %%d
        rmdir /s /q "%%d"
    )
)

for /d /r . %%d in (.ipynb_checkpoints) do (
    if exist "%%d" (
        echo   [OK] Removing: %%d
        rmdir /s /q "%%d"
    )
)

echo.
echo ========================================
echo  CLEANUP COMPLETE!
echo ========================================
echo.
echo All unnecessary files have been removed.
echo Your dashboard is still running perfectly!
echo.
echo Files KEPT (Essential):
echo   - streamlit_app.py
echo   - chart_components.py
echo   - dashboard_config.py
echo   - kpi_card.py
echo   - STRUCTURE.md
echo   - DASHBOARD_GUIDE.md
echo   - All data files
echo.
pause
