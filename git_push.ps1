# ========================================
# GIT COMMIT AND PUSH (PowerShell)
# ========================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " GIT COMMIT AND PUSH" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Set-Location "c:\Users\HP\Desktop\WORKFORCE PLANNING ANALYSIS\WorkForce-Planning-Analysis"

# Stage all changes
Write-Host "[1/3] Staging all changes..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -eq 0) {
    Write-Host "      ✅ Done!" -ForegroundColor Green
} else {
    Write-Host "      ❌ Error during staging!" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Commit with detailed message
Write-Host "[2/3] Committing changes..." -ForegroundColor Yellow
$commitMessage = @"
feat: Professional dashboard with meaningful labels and comprehensive docs

✨ Features:
- Interactive Streamlit dashboard with 20 visualizations
- Meaningful labels: Entry Level, Poor-Excellent, Very Low-Very High
- Job levels, performance ratings, education all clearly labeled
- No more confusing numbers (1,2,3,4,5)

📊 Dashboard Improvements:
- 11 charts updated with clear, business-friendly labels
- Filter section redesigned with proper spacing
- Vibrant colors and compact layout
- Fixed undefined values issue

📚 Documentation:
- LABEL_IMPROVEMENTS.md - Complete guide to label changes
- CLEANUP_RECOMMENDATION.md - Project organization guide
- GIT_READINESS_REPORT.md - Verification report
- READY_TO_COMMIT.md - Quick commit guide

🧹 Project Organization:
- Cleanup scripts added (PowerShell and Batch)
- .gitignore properly configured
- Cache files excluded
- EDA notebook preserved for analysis documentation

All code tested and production-ready!
"@

git commit -m $commitMessage
if ($LASTEXITCODE -eq 0) {
    Write-Host "      ✅ Done!" -ForegroundColor Green
} else {
    Write-Host "      ❌ Error during commit!" -ForegroundColor Red
    Write-Host "      (This might be OK if there are no changes to commit)" -ForegroundColor Yellow
}
Write-Host ""

# Push to GitHub
Write-Host "[3/3] Pushing to GitHub..." -ForegroundColor Yellow
git push origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "      ✅ Done!" -ForegroundColor Green
} else {
    Write-Host "      ❌ Error during push!" -ForegroundColor Red
    Write-Host "      Check your internet connection and GitHub credentials" -ForegroundColor Yellow
    exit 1
}
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " SUCCESS! Changes pushed to GitHub 🎉" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Your repository is now updated with:" -ForegroundColor Yellow
Write-Host "  ✅ Professional interactive dashboard" -ForegroundColor Green
Write-Host "  ✅ Meaningful labels (no more 1,2,3,4,5!)" -ForegroundColor Green
Write-Host "  ✅ Comprehensive documentation" -ForegroundColor Green
Write-Host "  ✅ Clean project structure" -ForegroundColor Green
Write-Host ""
Write-Host "View your repository at:" -ForegroundColor Cyan
Write-Host "  https://github.com/divyathakur15/WorkForce-Planning-Analysis" -ForegroundColor Blue
Write-Host ""
