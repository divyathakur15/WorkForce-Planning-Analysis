# 📁 Project Structure

## Workforce Planning Analysis Dashboard

### **Root Directory**
```
WorkForce-Planning-Analysis/
│
├── 📊 dashboards/              # Streamlit Dashboard Application
│   ├── streamlit_app.py        # Main dashboard application
│   ├── chart_components.py     # Reusable chart functions
│   ├── dashboard_config.py     # Configuration & styling constants
│   ├── kpi_card.py             # KPI card components
│   ├── requirements.txt        # Dashboard dependencies
│   ├── run_dashboards.bat      # Quick launch script
│   └── README.md               # Dashboard documentation
│
├── 📁 Raw dataset/             # Original data files (CSV & Excel)
│   ├── employees_master.csv
│   ├── department_master.csv
│   ├── attendance_records.csv
│   ├── performance_reviews.csv
│   ├── training_and_skills.csv
│   ├── compensation_history.csv
│   ├── engagement_surveys.csv
│   ├── attrition_events.csv
│   ├── job_history.csv
│   └── Workforce Palnning Analysis DATASET.xlsx
│
├── 📁 data/                    # Processed data files
│
├── 📁 notebooks/               # Jupyter notebooks for analysis
│   └── (EDA, data cleaning notebooks)
│
├── 📁 scripts/                 # Utility scripts
│
├── 📁 reports/                 # Generated reports & exports
│
├── 📁 docs/                    # Project documentation
│   ├── Domain.md               # Business domain information
│   ├── Description.md          # Project description
│   ├── EndGoal.md              # Project objectives
│   └── IDEA.md                 # Project ideation
│
├── 📄 README.md                # Main project documentation
├── 📄 requirements.txt         # Python dependencies
├── 📄 .gitignore               # Git ignore rules
├── 📄 git_push.bat             # Quick git push script
└── 📄 git_commit_all.bat       # Quick commit script
```

---

## 📌 Quick Access

### **Start the Dashboard**
```bash
cd dashboards
streamlit run streamlit_app.py
```
Or double-click: `dashboards/run_dashboards.bat`

### **Access URLs**
- Local: `http://localhost:8501`
- Network: `http://YOUR_IP:8501`

---

## 🎯 Key Components

### **1. Dashboard Application** (`dashboards/`)
The main Streamlit dashboard with 4 interactive tabs:
- **📊 Overview**: Department headcount, job levels, tenure, attrition gauge
- **👥 Demographics**: Gender, age, education, marital status distributions
- **📉 Attrition Analysis**: Attrition trends, patterns, and predictions
- **💼 Performance & Engagement**: Performance ratings, satisfaction scores

### **2. Data Files** (`Raw dataset/`)
- **9 CSV files** containing HR data
- **1 Excel workbook** with consolidated data
- Covers: employees, departments, performance, compensation, training, engagement

### **3. Configuration** (`dashboards/dashboard_config.py`)
- Color schemes (vibrant professional palette)
- Chart configurations
- Font settings
- Layout constants

### **4. Reusable Components** (`dashboards/chart_components.py`)
- Bar charts
- Line charts
- Pie & donut charts
- Gauge charts
- Heatmaps
- Scatter plots
- Multi-line charts

---

## 🚀 Recent Enhancements

✅ **Compact spacing** - Reduced padding and margins
✅ **Light gradient background** - Professional blue-green gradient
✅ **Bolder axis titles** - Enhanced readability (13px, weight 700)
✅ **Animated graphics** - Pulse animations on emojis
✅ **Hover effects** - Interactive card transitions
✅ **Filter section redesign** - Gradient card with compact layout
✅ **Fixed undefined chart** - Proper gauge chart title display
✅ **Tab-based layout** - Clean separation of analytics sections

---

## 📝 Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Main project overview |
| `Domain.md` | HR analytics business domain |
| `Description.md` | Detailed project description |
| `EndGoal.md` | Project goals and objectives |
| `DASHBOARD_ACCESS_GUIDE.md` | How to access the dashboard |

---

## 🔧 Maintenance Scripts

- `git_push.bat` - Quick git push to remote
- `git_commit_all.bat` - Stage and commit all changes
- `dashboards/run_dashboards.bat` - Launch dashboard
- `cleanup_project.bat` - Clean temporary files

---

## 📊 Dashboard Features

### **Interactive Filters**
- 🏢 Department selection (multi-select)
- 👔 Job level filtering
- 📅 Tenure range slider

### **Key Metrics**
- Total Employees
- Active Employees
- Attrition Rate
- Average Tenure
- Satisfaction Score

### **Visualizations**
- 20+ interactive charts
- Real-time filtering
- Responsive design
- Export capabilities

---

## 🎨 Design System

### **Color Palette**
- Primary: `#2563EB` (Bright Blue)
- Secondary: `#8B5CF6` (Vivid Purple)
- Accent: `#F59E0B` (Amber Gold)
- Success: `#10B981` (Emerald Green)
- Warning: `#F59E0B` (Amber)
- Danger: `#EF4444` (Red)

### **Typography**
- Headers: Segoe UI, 700 weight
- Body: Segoe UI, 400 weight
- Metrics: 26px, 700 weight

---

## 📈 Technology Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas
- **Language**: Python 3.8+

---

*Last Updated: February 6, 2026*
