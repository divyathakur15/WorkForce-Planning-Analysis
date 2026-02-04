@echo off
echo ========================================
echo  GIT COMMIT AND PUSH
echo ========================================
echo.

cd "c:\Users\HP\Desktop\WORKFORCE PLANNING ANALYSIS\WorkForce-Planning-Analysis"

echo [1/3] Staging all changes...
git add .
echo      Done!
echo.

echo [2/3] Committing changes...
git commit -m "feat: Professional dashboard with meaningful labels and comprehensive docs

Features:
- Interactive Streamlit dashboard with 20 visualizations
- Meaningful labels: Entry Level, Poor-Excellent, Very Low-Very High
- Job levels, performance ratings, education all clearly labeled
- No more confusing numbers (1,2,3,4,5)

Dashboard Improvements:
- 11 charts updated with clear, business-friendly labels
- Filter section redesigned with proper spacing
- Vibrant colors and compact layout
- Fixed undefined values issue

Documentation:
- LABEL_IMPROVEMENTS.md - Complete guide to label changes
- CLEANUP_RECOMMENDATION.md - Project organization guide
- GIT_READINESS_REPORT.md - Verification report
- READY_TO_COMMIT.md - Quick commit guide

Project Organization:
- Cleanup scripts added (PowerShell and Batch)
- .gitignore properly configured
- Cache files excluded
- EDA notebook preserved for analysis documentation

All code tested and production-ready!"

if errorlevel 1 (
    echo      Error during commit!
    pause
    exit /b 1
)
echo      Done!
echo.

echo [3/3] Pushing to GitHub...
git push origin main
if errorlevel 1 (
    echo      Error during push!
    echo      Check your internet connection and GitHub credentials
    pause
    exit /b 1
)
echo      Done!
echo.

echo ========================================
echo  SUCCESS! Changes pushed to GitHub
echo ========================================
echo.
echo Your repository is now updated with:
echo   - Professional interactive dashboard
echo   - Meaningful labels (no more 1,2,3,4,5!)
echo   - Comprehensive documentation
echo   - Clean project structure
echo.
pause
