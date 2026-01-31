# Notebooks Folder

Jupyter notebooks for exploratory data analysis, visualization, and modeling.

## 📓 Purpose

This folder is designated for interactive analysis notebooks including:
- Exploratory Data Analysis (EDA)
- Data Visualization
- Statistical Analysis
- Machine Learning Models
- Hypothesis Testing
- Feature Engineering Experiments

## 🚀 Getting Started

### Create a New Notebook

1. **Launch Jupyter**:
```bash
jupyter notebook
```

2. **Load Processed Data**:
```python
import pandas as pd

# Load cleaned data
employees = pd.read_csv('../data/processed/employees_master_cleaned.csv')
departments = pd.read_csv('../data/processed/department_master_cleaned.csv')
attrition = pd.read_csv('../data/processed/attrition_events_cleaned.csv')

# Quick check
print(f"Total Employees: {len(employees):,}")
print(f"Attrition Rate: {len(attrition) / len(employees) * 100:.2f}%")
```

## 📊 Suggested Notebooks

### 1. **EDA_Workforce_Analysis.ipynb**
- Dataset overview and statistics
- Distribution analysis
- Missing value checks
- Correlation analysis

### 2. **Attrition_Analysis.ipynb**
- Attrition trends over time
- Department-wise attrition
- Reason analysis
- Risk segmentation

### 3. **Employee_Satisfaction.ipynb**
- Engagement score analysis
- Satisfaction vs retention
- Work-life balance impact
- Manager relationship effects

### 4. **Performance_Analysis.ipynb**
- Performance distribution
- Rating trends
- Promotion patterns
- Goal completion analysis

### 5. **ML_Attrition_Prediction.ipynb**
- Feature engineering
- Model training (RF, XGBoost, etc.)
- Model evaluation
- Feature importance

## 💡 Best Practices

### ✅ DO:
- Use data from `/data/processed/` folder
- Document your analysis clearly
- Use meaningful variable names
- Save important visualizations
- Version control your notebooks

### ❌ DON'T:
- Don't use `/data/raw/` for analysis
- Don't modify source CSV files
- Don't commit large output files
- Don't skip data validation

## 📚 Resources

- **Data Dictionary**: `/docs/DATA_DICTIONARY.md`
- **Quick Start Guide**: `/docs/QUICK_START.md`
- **Cleaning Summary**: `/docs/DATA_CLEANING_SUMMARY.md`

## 🎯 Example Analysis

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
employees = pd.read_csv('../data/processed/employees_master_cleaned.csv')
attrition = pd.read_csv('../data/processed/attrition_events_cleaned.csv')
departments = pd.read_csv('../data/processed/department_master_cleaned.csv')

# Merge for analysis
df = employees.merge(departments, on='department_id')
df = df.merge(attrition, on='employee_id', how='left')
df['attrition_flag'] = df['attrition_flag'].fillna(False)

# Attrition by department
dept_attrition = df.groupby('department_name').agg({
    'employee_id': 'count',
    'attrition_flag': 'sum'
}).rename(columns={'employee_id': 'total', 'attrition_flag': 'attrited'})
dept_attrition['rate'] = (dept_attrition['attrited'] / dept_attrition['total'] * 100).round(2)

print(dept_attrition.sort_values('rate', ascending=False).head())
```

---

**Recommended**: Start with EDA before building models  
**Last Updated**: January 31, 2026
