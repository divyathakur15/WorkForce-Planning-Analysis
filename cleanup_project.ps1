# ========================================
# PROJECT CLEANUP SCRIPT (PowerShell)
# Removes cache files, keeps all important files
# ========================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " PROJECT CLEANUP - Starting..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Count files before cleanup
$checkpointFolders = Get-ChildItem -Path . -Recurse -Directory -Filter ".ipynb_checkpoints" -ErrorAction SilentlyContinue
$pycacheFolders = Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue

$totalToRemove = $checkpointFolders.Count + $pycacheFolders.Count

if ($totalToRemove -eq 0) {
    Write-Host "✅ No cache files found - project is already clean!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Your project structure:" -ForegroundColor Yellow
    Write-Host "  ✅ EDA notebook: KEPT" -ForegroundColor Green
    Write-Host "  ✅ Static outputs: KEPT" -ForegroundColor Green
    Write-Host "  ✅ Dashboards: KEPT" -ForegroundColor Green
    Write-Host "  ✅ All data files: KEPT" -ForegroundColor Green
    Write-Host "  ✅ Documentation: KEPT" -ForegroundColor Green
} else {
    Write-Host "[1/2] Removing .ipynb_checkpoints folders..." -ForegroundColor Yellow
    $removed = 0
    foreach ($folder in $checkpointFolders) {
        Write-Host "  Removing: $($folder.FullName)" -ForegroundColor Gray
        Remove-Item $folder.FullName -Recurse -Force
        $removed++
    }
    Write-Host "  ✅ Removed $removed Jupyter checkpoint folder(s)" -ForegroundColor Green
    Write-Host ""

    Write-Host "[2/2] Removing __pycache__ folders..." -ForegroundColor Yellow
    $removed = 0
    foreach ($folder in $pycacheFolders) {
        Write-Host "  Removing: $($folder.FullName)" -ForegroundColor Gray
        Remove-Item $folder.FullName -Recurse -Force
        $removed++
    }
    Write-Host "  ✅ Removed $removed Python cache folder(s)" -ForegroundColor Green
    Write-Host ""

    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host " CLEANUP COMPLETE!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Removed:" -ForegroundColor Yellow
    Write-Host "  ✅ $($checkpointFolders.Count) Jupyter checkpoint folders" -ForegroundColor Green
    Write-Host "  ✅ $($pycacheFolders.Count) Python cache folders" -ForegroundColor Green
    Write-Host ""
    Write-Host "Kept (All Important Files):" -ForegroundColor Yellow
    Write-Host "  ✅ EDA Jupyter notebook" -ForegroundColor Green
    Write-Host "  ✅ Static output images (PNG files)" -ForegroundColor Green
    Write-Host "  ✅ Interactive HTML dashboard" -ForegroundColor Green
    Write-Host "  ✅ Streamlit dashboards" -ForegroundColor Green
    Write-Host "  ✅ All data files" -ForegroundColor Green
    Write-Host "  ✅ All documentation" -ForegroundColor Green
    Write-Host "  ✅ All scripts" -ForegroundColor Green
}

Write-Host ""
Write-Host "Your project is now clean and organized! 🎉" -ForegroundColor Cyan
Write-Host ""
