# Professional Workforce Planning Dashboards

This directory contains professional, corporate-grade dashboards for comprehensive workforce planning analysis.

## 📊 Dashboard Components

### 1. **Static HTML Dashboard** (`create_dashboard.py`)
- **Purpose**: Generate static HTML dashboards for reports and presentations
- **Features**:
  - Executive summary dashboard
  - KPI cards with professional styling
  - Multiple visualization types
  - Export to HTML for sharing

### 2. **Interactive Streamlit Dashboard** (`streamlit_app.py`)
- **Purpose**: Interactive web-based dashboard for real-time analysis
- **Features**:
  - Dynamic filters (department, job level, tenure)
  - Real-time KPI calculations
  - Multiple analytical views (Overview, Demographics, Attrition, Performance)
  - Professional color scheme and styling
  - Responsive layout

## 🚀 Quick Start

### Option 1: Run Static Dashboard
```bash
python create_dashboard.py
```
This will generate an HTML file in the `output/` folder that you can open in any browser.

### Option 2: Run Interactive Dashboard
```bash
streamlit run streamlit_app.py
```
This will launch a web server and open the interactive dashboard in your browser.

### Option 3: Use the Batch File (Windows)
```bash
run_dashboards.bat
```
This provides a menu to run either dashboard.

## 📦 Installation

Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🎨 Design Features

### Professional Color Scheme
- **Primary Blue**: #1E3A8A (Deep Blue)
- **Secondary Purple**: #7C3AED
- **Accent Amber**: #F59E0B
- **Success Green**: #10B981
- **Danger Red**: #EF4444

### Typography
- **Font Family**: Segoe UI, Arial, sans-serif
- **Title**: 24px, Bold
- **Subtitle**: 18px, Semi-bold
- **Body**: 14px, Regular

### KPI Cards
Each KPI card includes:
- Icon representation
- Large, bold value display
- Descriptive label
- Optional trend indicator with color coding
- Professional shadow and border styling

### Chart Types Available
1. **Bar Charts**: Horizontal and vertical
2. **Pie Charts**: Traditional and donut
3. **Line Charts**: Single and multi-line
4. **Gauge Charts**: For metrics with thresholds
5. **Heatmaps**: For correlation analysis
6. **Stacked/Grouped Bar Charts**: For comparative analysis
7. **Histograms**: For distribution analysis
8. **Box Plots**: For statistical analysis

## 📋 Dashboard Sections

### Executive Dashboard
- **KPIs**: Total Employees, Active Employees, Attrition Rate, Retention Rate, Avg Tenure, Avg Satisfaction, High Risk Employees
- **Visualizations**:
  - Attrition rate gauge
  - Headcount by department
  - Employees by job level
  - Attrition by department
  - Tenure distribution
  - Gender distribution

### Interactive Dashboard Tabs

#### 1. Overview Tab
- Top 10 departments by headcount
- Job level distribution
- Tenure category distribution
- Attrition rate gauge

#### 2. Demographics Tab
- Gender distribution
- Age group distribution
- Comprehensive demographic analysis

#### 3. Attrition Tab
- Attrition by department
- Top attrition reasons
- Attrition trends analysis

#### 4. Performance Tab
- Performance rating distribution
- Satisfaction score distribution
- High performers vs. at-risk employees

## 🎯 Key Features

### Filters (Interactive Dashboard)
- **Department Filter**: Select specific departments
- **Job Level Filter**: Focus on specific levels
- **Tenure Range**: Filter by years of service

### KPI Metrics
All dashboards display:
- Total Employees
- Active Employees
- Attrition Rate (with color-coded status)
- Retention Rate
- Average Tenure
- Average Satisfaction Score

### Professional Styling
- Clean, corporate design
- Consistent color palette
- Responsive layouts
- High-quality visualizations
- Professional fonts and spacing

## 📁 File Structure

```
dashboards/
├── dashboard_config.py      # Color schemes, themes, and constants
├── kpi_card.py             # KPI card components
├── chart_components.py     # Professional chart templates
├── create_dashboard.py     # Static dashboard generator
├── streamlit_app.py        # Interactive dashboard app
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── run_dashboards.bat     # Windows launcher
└── output/                # Generated dashboard files
    └── executive_dashboard.html
```

## 🔧 Customization

### Modify Colors
Edit `dashboard_config.py` to change the color scheme:
```python
COLORS = {
    'primary': '#1E3A8A',
    'secondary': '#7C3AED',
    # ... customize as needed
}
```

### Add New KPIs
Add new KPI templates in `dashboard_config.py`:
```python
KPI_TEMPLATES = {
    'your_kpi': {
        'icon': '📊',
        'label': 'Your KPI',
        'format': '{:.1f}%',
        'color': COLORS['primary']
    }
}
```

### Create New Charts
Use the chart components in `chart_components.py`:
```python
from chart_components import create_bar_chart

fig = create_bar_chart(data, 'x_column', 'y_column', 'Title')
```

## 📊 Data Requirements

The dashboards expect the following processed datasets in `data/processed/`:
- `employees_master.csv`
- `attrition_events.csv`
- `performance_reviews.csv`
- `engagement_surveys.csv`
- `department_master.csv`
- `job_history.csv`
- `compensation_history.csv`
- `training_and_skills.csv`
- `attendance_records.csv`

## 🐛 Troubleshooting

### Issue: Module not found
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Data files not found
**Solution**: Ensure you have run the data cleaning pipeline first
```bash
cd ../scripts
python data_cleaning_pipeline.py
```

### Issue: Streamlit port already in use
**Solution**: Specify a different port
```bash
streamlit run streamlit_app.py --server.port 8502
```

## 📈 Performance Tips

1. **Large Datasets**: The dashboards use caching to improve performance
2. **Filters**: Use filters to focus on specific segments and improve load times
3. **Export**: Generate static HTML dashboards for faster sharing

## 🎓 Best Practices

1. **Regular Updates**: Refresh data regularly for accurate insights
2. **Filter Usage**: Use filters to drill down into specific areas
3. **Export Reports**: Generate static dashboards for presentations
4. **Customization**: Tailor colors and metrics to your organization's needs

## 📞 Support

For questions or issues:
1. Check the documentation in `docs/`
2. Review the data dictionary in `docs/DATA_DICTIONARY.md`
3. Examine the data cleaning summary in `docs/DATA_CLEANING_SUMMARY.md`

## 📝 License

This dashboard system is part of the Workforce Planning Analysis project.

---

**Built with:**
- Python 3.13+
- Plotly for visualizations
- Streamlit for interactive dashboards
- Pandas for data processing
