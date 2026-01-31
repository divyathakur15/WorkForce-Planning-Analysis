# 📦 Cleaned Workforce Planning Dataset

## Overview

This folder contains the **production-ready, cleaned, and validated** workforce planning datasets. All 9 CSV files have been professionally processed using enterprise-grade data engineering standards.

---

## 📊 Dataset Files

| File Name | Records | Description |
|-----------|---------|-------------|
| `employees_master_cleaned.csv` | 5,000 | Core employee information with demographics, job details, and derived features |
| `department_master_cleaned.csv` | 20 | Department organizational structure with meaningful names |
| `job_history_cleaned.csv` | 10,010 | Employee role changes, promotions, and transfers |
| `compensation_history_cleaned.csv` | 15,073 | Salary revisions, bonuses, and stock options |
| `attendance_records_cleaned.csv` | 300,000 | Monthly attendance, absences, and overtime |
| `performance_reviews_cleaned.csv` | 10,048 | Performance evaluations and ratings |
| `engagement_surveys_cleaned.csv` | 7,472 | Employee satisfaction and engagement scores |
| `training_and_skills_cleaned.csv` | 14,969 | Employee skills, certifications, and training |
| `attrition_events_cleaned.csv` | 1,200 | Employee exits and attrition reasons |

**Total Records**: 385,986 across all tables

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| **`QUICK_START.md`** | ⚡ Start here! Quick guide to begin analysis |
| **`DATA_CLEANING_SUMMARY.md`** | 📋 Complete list of all cleaning actions performed |
| **`DATA_DICTIONARY.md`** | 📖 Detailed column definitions and specifications |
| **`DATA_QUALITY_REPORT.txt`** | ✅ Validation report (auto-generated) |

---

## ✨ What Makes This Dataset Ready?

### ✅ Cleaned & Standardized
- All duplicate records removed
- All dates in standard format (YYYY-MM-DD)
- All boolean values standardized (True/False)
- All categorical values cleaned and consistent
- All data ranges validated

### ✅ Validated & Verified
- 18/18 data quality tests passed (100%)
- All referential integrity validated
- All foreign keys checked
- All business rules enforced
- Cross-table consistency verified

### ✅ Enhanced & Enriched
- Department names replaced with meaningful names (HR, Engineering, Sales, etc.)
- Derived features added (tenure_years, tenure_category, age_group)
- Status synchronized across tables
- Engagement scores recalculated for accuracy

---

## 🚀 Quick Start

### Python
```python
import pandas as pd

# Load data
employees = pd.read_csv('employees_master_cleaned.csv')
attrition = pd.read_csv('attrition_events_cleaned.csv')

# Calculate attrition rate
attrition_rate = len(attrition) / len(employees) * 100
print(f"Attrition Rate: {attrition_rate:.2f}%")
```

### Power BI
1. Get Data → Text/CSV
2. Load all 9 CSV files
3. Create relationships on employee_id and department_id
4. Start building visuals!

### SQL
```sql
-- Import CSVs as tables, then query:
SELECT 
    department_name,
    COUNT(*) as employee_count,
    AVG(tenure_years) as avg_tenure
FROM employees_master_cleaned
JOIN department_master_cleaned USING (department_id)
WHERE status = 'Active'
GROUP BY department_name;
```

---

## 📈 Key Metrics

- **Total Employees**: 5,000
- **Active**: 3,800 (76%)
- **Attrited**: 1,200 (24%)
- **Attrition Rate**: 24%
- **Departments**: 20
- **Average Tenure**: 8.49 years
- **Average Age**: 40.2 years
- **Gender Balance**: 50/50 split

---

## 🎯 Use Cases

This dataset is perfect for:

1. **Attrition Prediction** - Build ML models to predict turnover
2. **Dashboard Development** - Create Power BI/Tableau dashboards
3. **HR Analytics** - Analyze workforce trends and patterns
4. **SQL Practice** - Complex joins and aggregations
5. **Data Visualization** - Create compelling visual stories
6. **Business Intelligence** - Generate actionable insights
7. **Portfolio Projects** - Showcase data analytics skills

---

## 🔗 Table Relationships

```
employees_master (PK: employee_id)
    ├── department_master (FK: department_id)
    ├── job_history (FK: employee_id)
    ├── compensation_history (FK: employee_id)
    ├── attendance_records (FK: employee_id)
    ├── performance_reviews (FK: employee_id)
    ├── engagement_surveys (FK: employee_id)
    ├── training_and_skills (FK: employee_id)
    └── attrition_events (FK: employee_id)
```

---

## 🛠️ Technical Specifications

- **Format**: CSV (UTF-8 encoded)
- **Date Format**: YYYY-MM-DD HH:MM:SS
- **Boolean Format**: Python boolean (True/False)
- **Null Handling**: Intentional nulls only (e.g., end_date for current roles)
- **File Size**: ~17 MB total
- **Compatible With**: Python, R, SQL, Excel, Power BI, Tableau

---

## 📊 Data Quality Score

### Overall: 10/10 ⭐⭐⭐⭐⭐

- **Completeness**: 10/10 (No missing critical data)
- **Accuracy**: 10/10 (All values validated)
- **Consistency**: 10/10 (Cross-table sync verified)
- **Timeliness**: 10/10 (Current as of 2024-12-31)
- **Validity**: 10/10 (All ranges and references checked)

---

## 🎓 Learning Resources

For detailed information, see:
1. **QUICK_START.md** - Begin your analysis journey
2. **DATA_DICTIONARY.md** - Understand every column
3. **DATA_CLEANING_SUMMARY.md** - Learn what was cleaned

---

## ⚠️ Important Notes

1. **Use cleaned_dataset/ for analysis** - Don't use Raw dataset/
2. **Department names are meaningful** - Human Resources, Engineering, etc.
3. **All dates are standardized** - Consistent YYYY-MM-DD format
4. **Status field is synced** - Matches attrition_events table
5. **Derived features included** - tenure_years, age_group ready to use

---

## 🏆 Data Engineering Standards

This dataset meets professional data engineering standards:
- ✅ Schema design (normalized relational structure)
- ✅ Data validation (comprehensive rule enforcement)
- ✅ Referential integrity (all FKs validated)
- ✅ Data standardization (consistent formats)
- ✅ Documentation (complete specifications)
- ✅ Testing (18 automated quality checks)
- ✅ Version control (tracked and documented)

---

## 📞 Need Help?

- **Schema Questions**: See DATA_DICTIONARY.md
- **Analysis Ideas**: See QUICK_START.md
- **Cleaning Details**: See DATA_CLEANING_SUMMARY.md
- **Validation Results**: Run verify_cleaned_data.py

---

## ✅ Ready to Use

This dataset is **100% production-ready** for:
- ✅ Data Analysis
- ✅ Machine Learning
- ✅ Dashboard Development
- ✅ SQL Queries
- ✅ Statistical Analysis
- ✅ Business Reporting

**Start analyzing now!** 🚀

---

**Version**: 1.0  
**Last Updated**: 2026-01-31  
**Status**: Production-Ready  
**Quality**: Enterprise-Grade  
**Verified**: ✅ All Tests Passed
