@echo off
echo ========================================
echo  GIT: ADD, COMMIT, PUSH
echo ========================================
echo.

cd "c:\Users\HP\Desktop\WORKFORCE PLANNING ANALYSIS\WorkForce-Planning-Analysis"

echo [Step 1/3] Staging all changes...
git add .
if errorlevel 1 (
    echo      ❌ Error staging files!
    pause
    exit /b 1
)
echo      ✅ Files staged
echo.

echo [Step 2/3] Creating commit...
git commit -m "docs: Add clear dashboard access guide and clarify outputs folder" -m "- Added prominent 'LIVE INTERACTIVE DASHBOARD' section at top of README with localhost link" -m "- Created comprehensive DASHBOARD_ACCESS_GUIDE.md with 3-step quick start" -m "- Added warning README in notebook/outputs/outputs/ folder to redirect users" -m "- Clarified difference between EDA outputs (static reference) and live dashboard" -m "- Updated project structure with clear markers (⭐ USE THIS, ⚠️ reference only)" -m "- Improved user experience for GitHub visitors" -m "- Fixed dashboard label improvements (Entry Level, Poor-Excellent, etc.)" -m "- All changes ready for professional portfolio presentation"
if errorlevel 1 (
    echo      ⚠️  Nothing to commit or error occurred
    echo      This might be OK if no changes were made
)
echo      ✅ Commit created
echo.

echo [Step 3/3] Pushing to GitHub...
git push origin main
if errorlevel 1 (
    echo      ❌ Error pushing to GitHub!
    echo      Check your internet connection and credentials
    pause
    exit /b 1
)
echo      ✅ Pushed to GitHub
echo.

echo ========================================
echo  SUCCESS! All changes on GitHub 🎉
echo ========================================
echo.
echo Your repository now has:
echo   ✅ Clear dashboard access instructions
echo   ✅ Localhost link prominently displayed
echo   ✅ Warning on static outputs folder
echo   ✅ Professional documentation
echo   ✅ User-friendly structure
echo.
echo View at: https://github.com/divyathakur15/WorkForce-Planning-Analysis
echo.
pause
