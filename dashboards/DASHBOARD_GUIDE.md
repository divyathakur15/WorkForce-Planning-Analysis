# 📊 Workforce Planning Dashboard

> **Interactive Streamlit dashboard for comprehensive HR analytics and workforce insights.**

---

## 🚀 Quick Launch

### **Method 1: Batch File (Easiest)**
Double-click: `run_dashboards.bat`

### **Method 2: Command Line**
```bash
streamlit run streamlit_app.py
```

### **Method 3: Python**
```bash
python -m streamlit run streamlit_app.py
```

**Access at:** `http://localhost:8501`

---

## 📱 Dashboard Tabs

### **1. 📊 Overview**
- Top 10 departments by headcount
- Job level distribution (Entry to Executive)
- Tenure distribution categories
- Attrition rate gauge with color zones

### **2. 👥 Demographics**
- Gender distribution
- Age group breakdown
- Marital status analysis
- Education level distribution
- Ethnicity insights
- Veteran status

### **3. 📉 Attrition Analysis**
- Attrition trends over time
- Department-wise attrition patterns
- Exit reasons analysis
- Risk factor identification
- Retention metrics

### **4. 💼 Performance & Engagement**
- Performance rating distributions
- Satisfaction scores
- Manager ratings
- Training completion rates
- Engagement metrics
- Performance trends

---

## 🎛️ Interactive Filters

All tabs support real-time filtering:

- **🏢 Departments**: Multi-select department filter
- **👔 Job Levels**: Entry, Mid, Senior, Lead, Executive
- **📅 Tenure Range**: Slider for years of service

---

## 🎨 Features

### **Visual Design**
✅ Light gradient background (blue → green)
✅ Compact spacing for maximum content
✅ Bold axis titles (13px, weight 700)
✅ Animated emojis with pulse effect
✅ Hover effects on cards
✅ Glassmorphism filter section
✅ Responsive layout

### **Interactivity**
✅ Real-time filtering across all charts
✅ Hover tooltips on all visualizations
✅ Color-coded metrics (KPIs)
✅ Dynamic data updates
✅ Export-ready charts

---

## 📊 Key Metrics (KPI Cards)

| Metric | Description |
|--------|-------------|
| **Total Employees** | Complete workforce count |
| **Active Employees** | Currently employed |
| **Attrition Rate** | % of employees who left |
| **Average Tenure** | Mean years of service |
| **Satisfaction Score** | Average employee satisfaction (1-5) |

---

## 📂 File Structure

```
dashboards/
├── streamlit_app.py        # Main application (919 lines)
├── chart_components.py     # Chart functions (389 lines)
├── dashboard_config.py     # Configuration (229 lines)
├── kpi_card.py             # KPI components
├── requirements.txt        # Dependencies
├── run_dashboards.bat      # Quick launcher
└── DASHBOARD_GUIDE.md      # This file
```

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Streamlit 1.x |
| **Visualization** | Plotly 5.x |
| **Data Processing** | Pandas |
| **Language** | Python 3.8+ |

---

## 🎨 Color Palette

### **Primary Colors**
- 🔵 Primary: `#2563EB` (Bright Blue)
- 🟣 Secondary: `#8B5CF6` (Vivid Purple)
- 🟠 Accent: `#F59E0B` (Amber Gold)
- 🔷 Tertiary: `#06B6D4` (Cyan)

### **Status Colors**
- 🟢 Success: `#10B981` (Emerald Green)
- 🟡 Warning: `#F59E0B` (Amber)
- 🔴 Danger: `#EF4444` (Red)
- 🔵 Info: `#3B82F6` (Blue)

---

## 📈 Chart Types

- **Bar Charts**: Department headcount, tenure distribution
- **Donut Charts**: Job levels, marital status, education
- **Pie Charts**: Gender, ethnicity distribution
- **Gauge Charts**: Attrition rate with color zones
- **Line Charts**: Trends over time
- **Heatmaps**: Correlation analysis
- **Grouped Bar**: Comparative analysis
- **Scatter Plots**: Relationship exploration

---

## 🔧 Configuration

### **Chart Settings** (`dashboard_config.py`)
- Plot backgrounds
- Font families and sizes
- Grid styles
- Color schemes
- Hover label formatting

### **Layout Settings**
- KPI card dimensions
- Border radius
- Shadow effects
- Spacing constants

---

## 📊 Data Requirements

The dashboard expects these CSV files in `../Raw dataset/`:

1. `employees_master.csv` - Employee details
2. `department_master.csv` - Department information
3. `attendance_records.csv` - Attendance data
4. `performance_reviews.csv` - Performance ratings
5. `training_and_skills.csv` - Training records
6. `compensation_history.csv` - Salary history
7. `engagement_surveys.csv` - Survey responses
8. `attrition_events.csv` - Exit information
9. `job_history.csv` - Job transitions

---

## 🚨 Troubleshooting

### **Dashboard won't start**
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### **Data not loading**
- Ensure CSV files are in `../Raw dataset/` folder
- Check file names match exactly
- Verify CSV encoding (UTF-8)

### **Charts not displaying**
- Clear Streamlit cache: Press `C` in the dashboard
- Restart the server
- Check browser console for errors

### **Port already in use**
```bash
streamlit run streamlit_app.py --server.port 8502
```

---

## 🎯 Usage Tips

1. **Filter First**: Use sidebar filters to narrow down data
2. **Hover for Details**: Hover over charts for tooltips
3. **Export Charts**: Click camera icon on charts to save
4. **Refresh Data**: Use browser refresh (F5) to reload
5. **Full Screen**: Click expand icon on charts

---

## 📝 Recent Updates

### **v2.0 - February 6, 2026**
✅ Light gradient background
✅ Compact spacing throughout
✅ Bolder axis titles (weight 700)
✅ Animated filter section
✅ Fixed gauge chart title
✅ Enhanced hover effects
✅ Glassmorphism design elements

---

## 👨‍💻 Development

### **Run in development mode**
```bash
streamlit run streamlit_app.py --server.runOnSave true
```

### **Debug mode**
```bash
streamlit run streamlit_app.py --logger.level debug
```

---

## 📄 License

MIT License - See LICENSE file for details

---

*Last Updated: February 6, 2026*
*Version: 2.0*
