# 🧹 HOW TO RUN CLEANUP

## Option 1: PowerShell Script (Recommended)

1. **Open a NEW PowerShell window** (separate from Streamlit)
   
2. **Navigate to project:**
   ```powershell
   cd "c:\Users\HP\Desktop\WORKFORCE PLANNING ANALYSIS\WorkForce-Planning-Analysis"
   ```

3. **Run the cleanup script:**
   ```powershell
   .\cleanup_project.ps1
   ```

   If you get an error about execution policy, run this first:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\cleanup_project.ps1
   ```

---

## Option 2: Manual Commands

Copy and paste these commands one at a time in a NEW PowerShell window:

```powershell
# Navigate to project
cd "c:\Users\HP\Desktop\WORKFORCE PLANNING ANALYSIS\WorkForce-Planning-Analysis"

# Remove Jupyter checkpoints
Get-ChildItem -Path . -Recurse -Directory -Filter ".ipynb_checkpoints" | Remove-Item -Recurse -Force

# Remove Python cache
Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force

# Confirm
Write-Host "Cleanup complete! ✅"
```

---

## What Gets Removed:
- ❌ `.ipynb_checkpoints/` folders (Jupyter cache)
- ❌ `__pycache__/` folders (Python cache)

## What Gets KEPT:
- ✅ `notebook/outputs/EDA IN WorkForce.ipynb` - Your EDA analysis
- ✅ `notebook/outputs/outputs/*.png` - Static output images
- ✅ `notebook/outputs/outputs/interactive_dashboard.html` - HTML dashboard
- ✅ `dashboards/` - All Streamlit dashboard files
- ✅ `data/` - All data files
- ✅ `docs/` - All documentation
- ✅ Everything else important!

---

## Note:
Make sure to open a **NEW** PowerShell window, not the one running Streamlit!
