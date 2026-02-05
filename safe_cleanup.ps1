# ========================================
# SAFE CLEANUP SCRIPT
# Removes verified unnecessary files only
# ========================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " SAFE CLEANUP - Starting..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$filesRemoved = 0
$foldersRemoved = 0
$errors = @()

# 1. Remove old dashboard debug/fix scripts
Write-Host "[1/5] Removing old dashboard debug scripts..." -ForegroundColor Yellow
$debugScripts = @(
    "dashboards\create_dashboard.py",
    "dashboards\fix_dashboard.py",
    "dashboards\fix_indent.py",
    "dashboards\rebuild_dashboard.py",
    "streamlit_app_backup.py"
)

foreach ($file in $debugScripts) {
    if (Test-Path $file) {
        try {
            Remove-Item $file -Force
            Write-Host "  ✅ Removed: $file" -ForegroundColor Green
            $filesRemoved++
        } catch {
            Write-Host "  ❌ Failed to remove: $file" -ForegroundColor Red
            $errors += $file
        }
    } else {
        Write-Host "  ⚠️  Not found: $file" -ForegroundColor Gray
    }
}

Write-Host ""

# 2. Remove old documentation files
Write-Host "[2/5] Removing old documentation files..." -ForegroundColor Yellow
$oldDocs = @(
    "CLEANUP_RECOMMENDATION.md",
    "HOW_TO_CLEANUP.md",
    "DASHBOARD_ACCESS_GUIDE.md",
    "FINAL_COMPLETION_REPORT.md",
    "GITHUB_IMPROVEMENTS_SUMMARY.md"
)

foreach ($file in $oldDocs) {
    if (Test-Path $file) {
        try {
            Remove-Item $file -Force
            Write-Host "  ✅ Removed: $file" -ForegroundColor Green
            $filesRemoved++
        } catch {
            Write-Host "  ❌ Failed to remove: $file" -ForegroundColor Red
            $errors += $file
        }
    } else {
        Write-Host "  ⚠️  Not found: $file" -ForegroundColor Gray
    }
}

Write-Host ""

# 3. Remove duplicate documentation
Write-Host "[3/5] Removing duplicate documentation..." -ForegroundColor Yellow
$duplicates = @(
    "dashboards\INDEX.md"
)

foreach ($file in $duplicates) {
    if (Test-Path $file) {
        try {
            Remove-Item $file -Force
            Write-Host "  ✅ Removed: $file" -ForegroundColor Green
            $filesRemoved++
        } catch {
            Write-Host "  ❌ Failed to remove: $file" -ForegroundColor Red
            $errors += $file
        }
    } else {
        Write-Host "  ⚠️  Not found: $file" -ForegroundColor Gray
    }
}

Write-Host ""

# 4. Remove cleanup script in wrong location
Write-Host "[4/5] Removing redundant cleanup scripts..." -ForegroundColor Yellow
$redundantScripts = @(
    "dashboards\cleanup.bat"
)

foreach ($file in $redundantScripts) {
    if (Test-Path $file) {
        try {
            Remove-Item $file -Force
            Write-Host "  ✅ Removed: $file" -ForegroundColor Green
            $filesRemoved++
        } catch {
            Write-Host "  ❌ Failed to remove: $file" -ForegroundColor Red
            $errors += $file
        }
    } else {
        Write-Host "  ⚠️  Not found: $file" -ForegroundColor Gray
    }
}

Write-Host ""

# 5. Remove cache folders (safe - auto-regenerated)
Write-Host "[5/5] Removing cache folders..." -ForegroundColor Yellow

# Remove .ipynb_checkpoints
$checkpointFolders = Get-ChildItem -Path . -Recurse -Directory -Filter ".ipynb_checkpoints" -ErrorAction SilentlyContinue
foreach ($folder in $checkpointFolders) {
    try {
        Remove-Item $folder.FullName -Recurse -Force
        Write-Host "  ✅ Removed: $($folder.FullName)" -ForegroundColor Green
        $foldersRemoved++
    } catch {
        Write-Host "  ❌ Failed to remove: $($folder.FullName)" -ForegroundColor Red
    }
}

# Remove __pycache__
$pycacheFolders = Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue
foreach ($folder in $pycacheFolders) {
    try {
        Remove-Item $folder.FullName -Recurse -Force
        Write-Host "  ✅ Removed: $($folder.FullName)" -ForegroundColor Green
        $foldersRemoved++
    } catch {
        Write-Host "  ❌ Failed to remove: $($folder.FullName)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " CLEANUP COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 Summary:" -ForegroundColor Yellow
Write-Host "  ✅ Files removed: $filesRemoved" -ForegroundColor Green
Write-Host "  ✅ Folders removed: $foldersRemoved" -ForegroundColor Green

if ($errors.Count -gt 0) {
    Write-Host "  ⚠️  Errors encountered: $($errors.Count)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Files that couldn't be removed:" -ForegroundColor Red
    foreach ($err in $errors) {
        Write-Host "    - $err" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "✅ Your project is now clean and organized!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Files KEPT (Essential):" -ForegroundColor Yellow
Write-Host "  ✅ streamlit_app.py - Main dashboard" -ForegroundColor Green
Write-Host "  ✅ chart_components.py - Chart functions" -ForegroundColor Green
Write-Host "  ✅ dashboard_config.py - Configuration" -ForegroundColor Green
Write-Host "  ✅ STRUCTURE.md - Project structure" -ForegroundColor Green
Write-Host "  ✅ DASHBOARD_GUIDE.md - User guide" -ForegroundColor Green
Write-Host "  ✅ All data files" -ForegroundColor Green
Write-Host "  ✅ All documentation" -ForegroundColor Green
Write-Host ""
