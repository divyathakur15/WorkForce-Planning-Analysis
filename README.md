# 📊 Workforce Planning Analysis Dashboard

> **A comprehensive, interactive HR analytics dashboard for workforce planning, attrition analysis, and strategic insights.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.x-green)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 🚀 Quick Start

### **Launch the Dashboard**
```bash
cd dashboards
streamlit run streamlit_app.py
```
Or simply double-click: `dashboards/run_dashboards.bat`

**Access at:** `http://localhost:8501`

---

## 📁 Project Structure

```
WorkForce-Planning-Analysis/
│
├── � dashboards/              # ⭐ MAIN INTERACTIVE DASHBOARD
│   ├── streamlit_app.py        # Main dashboard application
│   ├── chart_components.py     # Reusable chart functions
│   ├── dashboard_config.py     # Configuration & styling
│   ├── kpi_card.py             # KPI card components
│   ├── requirements.txt        # Dashboard dependencies
│   └── README.md               # Dashboard documentation
│
├── 📁 Raw dataset/             # Original HR data files
│   ├── employees_master.csv    # Employee information
│   ├── department_master.csv   # Department details
│   ├── attendance_records.csv  # Attendance tracking
│   ├── performance_reviews.csv # Performance data
│   ├── training_and_skills.csv # Training records
│   ├── compensation_history.csv# Salary information
│   ├── engagement_surveys.csv  # Employee surveys
│   ├── attrition_events.csv    # Exit data
│   └── job_history.csv         # Job transitions
│
├── � notebooks/               # Jupyter notebooks (EDA)
├── 📁 scripts/                 # Utility scripts
├── 📁 reports/                 # Generated reports
├── � docs/                    # Documentation
│   ├── Domain.md               # Business domain
│   ├── Description.md          # Project details
│   ├── EndGoal.md              # Objectives
│   └── IDEA.md                 # Project ideation
│
├── 📄 README.md                # This file
├── 📄 STRUCTURE.md             # Detailed structure guide
├── 📄 requirements.txt         # Python dependencies
└── 📄 .gitignore               # Git ignore rules
```

---

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Data Quality](https://img.shields.io/badge/Data%20Quality-10%2F10-brightgreen.svg)](docs/DATA_CLEANING_SUMMARY.md)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](data/processed/)
[![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-red.svg)](dashboards/)

---

## 🎨 **LIVE INTERACTIVE DASHBOARD** ⭐

**Want to see the insights in action?** Run the professional interactive dashboard:

```bash
# Navigate to dashboards folder
cd dashboards

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run streamlit_app.py
```

**🌐 Then open your browser to:** `http://localhost:8501`

**Features:**
- 📊 20 interactive visualizations across 4 tabs
- 🎯 6 real-time KPI cards
- 🔍 Dynamic filters (Department, Job Level, Tenure)
- 🎨 Professional UI with meaningful labels (no confusing numbers!)
- 📈 Overview, Demographics, Attrition, Performance analytics

**📚 For detailed dashboard documentation, see:** [`dashboards/README.md`](dashboards/README.md)

---

## 🎯 Project Overview

Employee attrition is one of the most expensive challenges for organizations. This project analyzes workforce data to:
- Identify patterns behind employee turnover
- Predict which employees are at risk of leaving
- Understand key factors influencing retention
- Provide actionable insights for HR teams

**Focus**: Data analytics and visualization with emphasis on business insights and workforce planning strategies.

---

## � **Two Analysis Components**

This project contains **two complementary analysis tools** for different audiences:

### 1. 🎨 **Interactive Streamlit Dashboard** (RECOMMENDED)
- **Location:** `dashboards/streamlit_app.py`
- **Purpose:** Real-time workforce analytics for business users
- **Audience:** HR managers, executives, stakeholders
- **Features:** Live filters, interactive charts, real-time KPIs
- **Run:** `cd dashboards && streamlit run streamlit_app.py`
- **Access:** `http://localhost:8501`

### 2. 📓 **EDA Jupyter Notebook** (Analysis Documentation)
- **Location:** `notebook/outputs/EDA IN WorkForce.ipynb`
- **Purpose:** Exploratory data analysis and methodology documentation
- **Audience:** Data scientists, analysts, technical reviewers
- **Features:** Statistical analysis, correlation studies, static visualizations
- **Output:** Static images in `notebook/outputs/outputs/` (PNG files, HTML)
- **Note:** ⚠️ These are **static snapshots** from initial analysis, not the live dashboard

**💡 TIP:** Use the **Streamlit Dashboard** for live analysis. The notebook outputs are for reference only.

---

## �📁 Project Structure

```
WorkForce-Planning-Analysis/
│
├── 📂 data/                          # All datasets
│   ├── raw/                          # Original data (9 CSVs + Excel)
│   └── processed/                    # ⭐ Cleaned, production-ready data
│
├── 📂 notebooks/                     # Jupyter notebooks for analysis
│   └── README.md                     # Notebook usage guide
│
├── 📂 scripts/                       # Python automation scripts
│   ├── data_cleaning_pipeline.py    # Comprehensive data cleaning
│   ├── verify_cleaned_data.py       # Quality validation
│   └── README.md                     # Script documentation
│
├── 📂 docs/                          # Project documentation
│   ├── QUICK_START.md               # Getting started guide
│   ├── DATA_DICTIONARY.md           # Complete column specs
│   ├── DATA_CLEANING_SUMMARY.md     # Cleaning report
│   ├── Description.md               # Dataset schema
│   ├── Domain.md                    # Project domain
│   ├── EndGoal.md                   # Objectives
│   └── IDEA.md                      # Project concept
│
├── 📂 reports/                       # Analysis outputs
│   └── README.md                     # Report guidelines
│
├── 📄 README.md                      # This file
├── 📄 .gitignore                     # Git ignore rules
└── 📄 requirements.txt               # Python dependencies
```

---

## 📊 Dataset Overview

### Size & Scope
- **Total Employees**: 5,000
- **Attrition Events**: 1,200 (24% attrition rate)
- **Departments**: 20 (with meaningful names)
- **Total Records**: 385,986 across 9 relational tables
- **Time Period**: Multi-year historical data

### Data Tables
1. **employees_master** - Core employee information
2. **department_master** - Department organizational structure
3. **job_history** - Role changes and promotions
4. **compensation_history** - Salary and bonus records
5. **attendance_records** - Monthly attendance tracking
6. **performance_reviews** - Performance evaluations
7. **engagement_surveys** - Satisfaction and engagement
8. **training_and_skills** - Skills and certifications
9. **attrition_events** - Employee exits and reasons

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/divyathakur15/WorkForce-Planning-Analysis.git
cd WorkForce-Planning-Analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Load Cleaned Data
```python
import pandas as pd

# Load production-ready data
employees = pd.read_csv('data/processed/employees_master_cleaned.csv')
attrition = pd.read_csv('data/processed/attrition_events_cleaned.csv')

# Quick analysis
print(f"Attrition Rate: {len(attrition) / len(employees) * 100:.2f}%")
```

### 4. Explore Documentation
- **New to project?** → Read `docs/QUICK_START.md`
- **Need column details?** → See `docs/DATA_DICTIONARY.md`
- **Want to understand cleaning?** → Check `docs/DATA_CLEANING_SUMMARY.md`

---

## 🎯 Key Features

### ✅ Data Quality
- **100% validated** - 18/18 quality tests passed
- **No duplicates** - All primary keys unique
- **Referential integrity** - All foreign keys validated
- **Standardized formats** - Dates, booleans, categoricals
- **Meaningful names** - Department names business-friendly
- **Derived features** - Tenure, age groups added

### ✅ Enterprise-Grade
- Professional data engineering standards
- Comprehensive documentation
- Reproducible pipeline
- Automated validation
- Production-ready outputs

---

## 📈 Analysis Areas

### 1. **Attrition Analysis**
- Overall attrition trends
- Department-wise breakdown
- Reason analysis
- Tenure-based patterns
- High-risk segments

### 2. **Employee Satisfaction**
- Engagement score trends
- Job satisfaction impact
- Work-life balance analysis
- Manager relationship effects

### 3. **Performance Analytics**
- Performance distribution
- Rating vs retention
- Promotion patterns
- Goal completion trends

### 4. **Compensation Analysis**
- Salary impact on retention
- Bonus effectiveness
- Salary bands comparison
- Hike patterns

### 5. **Predictive Modeling**
- Attrition prediction (ML)
- Risk scoring
- Feature importance
- Employee segmentation

---

## 🛠️ Tools & Technologies

- **Python** - Data cleaning, transformation, analysis
  - Pandas, NumPy (data manipulation)
  - Matplotlib, Seaborn (visualization)
  - Scikit-learn (machine learning)
- **SQL** - Querying and aggregations
- **Excel** - Initial exploration
- **Power BI / Tableau** - Interactive dashboards
- **Jupyter** - Exploratory analysis
- **Git** - Version control

---

## 📊 Key Metrics & KPIs

| Metric | Value |
|--------|-------|
| Total Employees | 5,000 |
| Active Employees | 3,800 (76%) |
| Attrited Employees | 1,200 (24%) |
| Departments | 20 |
| Average Age | 40.2 years |
| Average Tenure | 8.49 years |
| Engagement Score | 3.0/5.0 |
| Performance Rating | 3.0/5.0 |

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [Quick Start](docs/QUICK_START.md) | Begin analysis immediately |
| [Data Dictionary](docs/DATA_DICTIONARY.md) | Column definitions & specs |
| [Cleaning Summary](docs/DATA_CLEANING_SUMMARY.md) | What was cleaned & why |
| [Description](docs/Description.md) | Dataset schema & structure |
| [Domain](docs/Domain.md) | HR analytics context |
| [End Goal](docs/EndGoal.md) | Project objectives |

---

## 🎨 Dashboard Examples

### Power BI Dashboard
- **Executive Overview**: KPIs, trends, department breakdown
- **Attrition Analysis**: Deep dive into turnover patterns
- **Employee Satisfaction**: Engagement and satisfaction metrics
- **Performance & Retention**: Correlation analysis

### Sample Insights
- "Which departments have the highest attrition?"
- "How does job satisfaction affect retention?"
- "What's the ROI of training on employee retention?"
- "Which employee segments are at highest risk?"

---

## 🔄 Data Pipeline

```
Raw Data → Cleaning Scripts → Processed Data → Analysis → Insights
   ↓            ↓                  ↓              ↓          ↓
9 CSVs    data_cleaning_     9 cleaned     Notebooks/   Dashboards
          pipeline.py         CSVs        Power BI      Reports
```

---

## ✅ Quality Assurance

- **Automated Testing**: 18 validation tests
- **Data Validation**: All ranges and references checked
- **Documentation**: Comprehensive specs
- **Reproducibility**: Automated pipeline
- **Version Control**: Git tracked

**Quality Score**: 10/10 ⭐

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📝 License

This project is open source and available for educational and portfolio purposes.

---

## 👤 Author

**Divya Thakur**
- GitHub: [@divyathakur15](https://github.com/divyathakur15)
- Project: Workforce Planning Analysis

---

## 🎯 Use Cases

This project demonstrates:
- ✅ Data cleaning & transformation
- ✅ Exploratory data analysis
- ✅ Data visualization
- ✅ SQL querying & joins
- ✅ Dashboard development
- ✅ Machine learning (predictive analytics)
- ✅ Business insights generation
- ✅ Technical documentation

**Perfect for**: Data Analyst, Data Scientist, BI Developer portfolios

---

## 📞 Support

For questions or issues:
- Check documentation in `/docs/`
- Review README files in each folder
- Open an issue on GitHub

---

## 🎉 Project Status

**✅ PRODUCTION READY**

- Data: Clean & validated
- Documentation: Complete
- Scripts: Tested & working
- Quality: Enterprise-grade

**Start analyzing now!** 🚀

---

**Last Updated**: January 31, 2026  
**Version**: 1.0  
**Status**: Active

