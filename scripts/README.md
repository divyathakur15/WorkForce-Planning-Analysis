# Scripts Folder

Python scripts for data processing, cleaning, and validation.

## 📜 Available Scripts

### 1. `data_cleaning_pipeline.py`
**Purpose**: Comprehensive data cleaning and transformation

**What it does**:
- Fixes department names (Department_1 → Human Resources, etc.)
- Standardizes all date formats
- Removes duplicate records
- Validates referential integrity
- Checks data ranges (ages, ratings, etc.)
- Standardizes boolean values
- Adds derived features (tenure_years, age_group, etc.)
- Generates cleaned CSV files

**Usage**:
```bash
cd scripts
python data_cleaning_pipeline.py
```

**Output**: Cleaned CSV files in `/data/processed/`

---

### 2. `verify_cleaned_data.py`
**Purpose**: Automated data quality validation and testing

**What it does**:
- Runs 18 automated quality tests
- Checks for duplicates
- Validates referential integrity
- Verifies data ranges
- Tests cross-table consistency
- Generates statistics and metrics
- Confirms production readiness

**Usage**:
```bash
cd scripts
python verify_cleaned_data.py
```

**Output**: Validation report with test results

---

## 🚀 Running the Scripts

### Requirements
```bash
pip install pandas numpy
```

### Full Pipeline
```bash
# 1. Clean the data
python scripts/data_cleaning_pipeline.py

# 2. Verify quality
python scripts/verify_cleaned_data.py
```

## 📊 What Gets Processed

**Input**: 9 CSV files from `/data/raw/` (385,986 records)

**Processing**:
- Duplicate removal
- Date standardization
- Value validation
- Integrity checks
- Feature engineering

**Output**: 9 cleaned CSV files in `/data/processed/`

## ✅ Quality Standards

All scripts ensure:
- ✅ No duplicate primary keys
- ✅ All foreign keys validated
- ✅ All dates in standard format
- ✅ All values within valid ranges
- ✅ Cross-table consistency
- ✅ Enterprise-grade quality

## 📚 Documentation

For detailed information:
- `/docs/DATA_CLEANING_SUMMARY.md` - What gets cleaned
- `/docs/DATA_DICTIONARY.md` - Column specifications
- `/docs/QUICK_START.md` - Analysis examples

---

**Maintainer**: Data Engineering Team  
**Last Updated**: January 31, 2026
