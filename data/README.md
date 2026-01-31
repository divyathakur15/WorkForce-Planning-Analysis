# Data Folder

This folder contains all datasets for the Workforce Planning Analysis project.

## 📁 Subdirectories

### `/raw/`
Original, unprocessed data files.
- **Status**: ⚠️ Not cleaned
- **Purpose**: Reference and reproducibility
- **Usage**: Do NOT use for analysis

**Contains**:
- 9 CSV files with raw employee data
- 1 Excel workbook (all tables combined)

### `/processed/`
Production-ready, cleaned, and validated data files.
- **Status**: ✅ Production-ready
- **Purpose**: Analysis, visualization, modeling
- **Usage**: Use these files for ALL analysis work

**Contains**:
- 9 cleaned CSV files (385,986 total records)
- All quality checks passed (18/18 tests)
- Department names meaningful
- Dates standardized
- No duplicates
- Referential integrity validated

## 🎯 Quick Reference

| Need | Use |
|------|-----|
| Analysis | `/processed/` ✅ |
| Dashboard | `/processed/` ✅ |
| Machine Learning | `/processed/` ✅ |
| Original reference | `/raw/` |

## 📊 Data Statistics

- **Total Employees**: 5,000
- **Attrition Events**: 1,200 (24% rate)
- **Departments**: 20
- **Time Series Records**: 300,000+ attendance records
- **Quality Score**: 10/10 ⭐

## 📚 Documentation

For complete data specifications, see `/docs/`:
- `DATA_DICTIONARY.md` - Column definitions
- `QUICK_START.md` - Getting started guide
- `DATA_CLEANING_SUMMARY.md` - What was cleaned

---

**Last Updated**: January 31, 2026
