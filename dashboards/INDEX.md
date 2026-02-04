# 📊 Dashboard System - File Structure

## 📁 Directory Structure

```
dashboards/
├── 📄 Core Dashboard Files
│   ├── streamlit_app.py          # Main interactive dashboard (PRIMARY)
│   ├── create_dashboard.py       # Static HTML dashboard generator
│   ├── dashboard_config.py       # Color schemes, themes, constants
│   ├── kpi_card.py               # KPI card components
│   └── chart_components.py       # Chart templates (12 types)
│
├── 📄 Configuration Files
│   ├── requirements.txt          # Python dependencies
│   ├── .gitignore               # Git ignore patterns
│   └── .streamlit/
│       └── config.toml          # Streamlit configuration
│
├── 📄 Documentation
│   ├── README.md                # Main documentation (START HERE)
│   ├── INDEX.md                 # This file - Structure overview
│   ├── DASHBOARD_CREATION_SUMMARY.md  # Creation process summary
│   └── VISUAL_ENHANCEMENTS.md   # Visual improvements log
│
├── 📄 Launch Scripts
│   └── run_dashboards.bat       # Windows launcher menu
│
└── 📁 Output Directory
    └── output/                  # Generated dashboard files
        └── executive_dashboard.html (generated)
```

---

## 🚀 Quick Start Guide

### Option 1: Interactive Dashboard (Recommended)
```bash
cd dashboards
streamlit run streamlit_app.py
```
**Opens:** http://localhost:8501

### Option 2: Static Dashboard
```bash
cd dashboards
python create_dashboard.py
```
**Generates:** `output/executive_dashboard.html`

### Option 3: Windows Menu
```bash
cd dashboards
run_dashboards.bat
```
**Provides:** Interactive menu with all options

---

## 📄 File Descriptions

### 🎯 Core Dashboard Files

#### `streamlit_app.py` (PRIMARY)
**Purpose:** Main interactive web dashboard application  
**Size:** ~500 lines  
**Features:**
- 20 interactive visualizations
- 6 KPI cards with real-time calculations
- Dynamic filters (Department, Job Level, Tenure)
- 4 analytical tabs (Overview, Demographics, Attrition, Performance)
- Gradient backgrounds and modern styling
- Responsive layout

**Dependencies:** streamlit, plotly, pandas, dashboard_config, kpi_card, chart_components

#### `create_dashboard.py`
**Purpose:** Static HTML dashboard generator  
**Size:** ~300 lines  
**Features:**
- Generates standalone HTML file
- Executive summary dashboard
- Shareable via email/file system
- No server required

**Dependencies:** plotly, pandas, dashboard_config, kpi_card, chart_components

#### `dashboard_config.py`
**Purpose:** Centralized configuration for colors, themes, and styling  
**Size:** ~200 lines  
**Contents:**
- Color palette (10 vibrant colors)
- Typography settings (5 font configurations)
- Layout constants (margins, padding, heights)
- Chart configuration defaults
- KPI templates
- Theme definitions (light, dark, corporate)

**Used by:** All dashboard files

#### `kpi_card.py`
**Purpose:** KPI card component generator  
**Size:** ~150 lines  
**Components:**
- `create_kpi_card()` - Single KPI with trend
- `create_kpi_row()` - Multiple KPIs in row
- `create_metric_card()` - Multi-metric card

**Features:** Icons, trends, color coding, professional styling

#### `chart_components.py`
**Purpose:** Professional chart templates library  
**Size:** ~400 lines  
**Chart Types (12):**
1. Bar Charts (horizontal/vertical)
2. Line Charts (single/multi-line)
3. Pie Charts
4. Donut Charts
5. Stacked Bar Charts
6. Grouped Bar Charts
7. Heatmaps
8. Gauge Charts
9. Scatter Plots
10. Histograms
11. Box Plots
12. Multi-line Charts

**All charts include:** Vibrant colors, responsive sizing, interactive tooltips

---

### ⚙️ Configuration Files

#### `requirements.txt`
**Purpose:** Python package dependencies  
**Packages:**
- plotly >= 5.17.0 (Visualizations)
- streamlit >= 1.28.0 (Web framework)
- pandas >= 2.1.0 (Data processing)
- numpy >= 1.24.0 (Numerical operations)

**Install:** `pip install -r requirements.txt`

#### `.streamlit/config.toml`
**Purpose:** Streamlit configuration  
**Settings:**
- Disables usage stats collection
- Sets headless mode
- Configures port 8501

#### `.gitignore`
**Purpose:** Git ignore patterns  
**Ignores:** Cache files, virtual environments, output files, IDE files

---

### 📚 Documentation Files

#### `README.md` (START HERE)
**Purpose:** Comprehensive user guide  
**Sections:**
- Installation instructions
- Quick start guide
- Feature descriptions
- Customization guide
- Troubleshooting tips
- API reference

**Audience:** End users and developers

#### `INDEX.md` (This File)
**Purpose:** File structure and organization  
**Sections:**
- Directory structure
- File descriptions
- Quick reference
- Maintenance guide

**Audience:** Developers and maintainers

#### `DASHBOARD_CREATION_SUMMARY.md`
**Purpose:** Technical implementation summary  
**Contents:**
- Components created
- Design decisions
- Color schemes
- Architecture overview
- KPI metrics

**Audience:** Technical documentation

#### `VISUAL_ENHANCEMENTS.md`
**Purpose:** Visual improvement changelog  
**Contents:**
- Color palette changes
- Gradient additions
- Layout improvements
- Space optimization
- Before/after comparisons

**Audience:** Design documentation

---

### 🎬 Launch Scripts

#### `run_dashboards.bat`
**Purpose:** Windows launcher with interactive menu  
**Options:**
1. Generate static HTML dashboard
2. Launch interactive Streamlit dashboard
3. Install dependencies
4. Exit

**Platform:** Windows only (PowerShell/CMD)

---

### 📂 Output Directory

#### `output/`
**Purpose:** Generated dashboard files storage  
**Contents:**
- `executive_dashboard.html` (generated by create_dashboard.py)
- Future exports (PDFs, PNGs)

**Note:** Contents not tracked in Git (see .gitignore)

---

## 🔄 File Dependencies

```
streamlit_app.py
├── dashboard_config.py
├── kpi_card.py
│   └── dashboard_config.py
└── chart_components.py
    └── dashboard_config.py

create_dashboard.py
├── dashboard_config.py
├── kpi_card.py
│   └── dashboard_config.py
└── chart_components.py
    └── dashboard_config.py
```

**Key Point:** `dashboard_config.py` is the foundation for all other files

---

## 📊 Data Flow

```
data/processed/*.csv
        ↓
[streamlit_app.py or create_dashboard.py]
        ↓
    Load Data
        ↓
  Calculate KPIs
        ↓
Apply Filters (Streamlit only)
        ↓
  Generate Charts
        ↓
   Render Dashboard
        ↓
[Browser Display or HTML File]
```

---

## 🎨 Styling Hierarchy

```
dashboard_config.py (Global Styles)
        ↓
    ┌────────┴────────┐
    ↓                 ↓
Components       App Styles
(kpi_card,       (streamlit_app
chart_components) custom CSS)
```

---

## 🛠️ Maintenance Guide

### Adding a New Chart Type
1. Add function to `chart_components.py`
2. Use `COLORS` and `CHART_CONFIG` from `dashboard_config.py`
3. Follow existing pattern (height=350, margins, etc.)
4. Import in `streamlit_app.py` or `create_dashboard.py`

### Changing Colors
1. Edit `COLORS` dictionary in `dashboard_config.py`
2. All dashboards will update automatically
3. Test both static and interactive versions

### Adding New KPI
1. Calculate in `calculate_kpis()` function
2. Add to KPI row in `streamlit_app.py`
3. Use `create_kpi_card()` for custom styling

### Modifying Layout
1. Update `LAYOUT` in `dashboard_config.py`
2. Chart heights, margins, padding centrally controlled

---

## 📝 Code Style Guidelines

### Python
- **PEP 8** compliant
- **Docstrings** for all functions
- **Type hints** where applicable
- **Comments** for complex logic

### File Organization
- **Imports** at top (standard, third-party, local)
- **Constants** after imports
- **Functions** before main execution
- **Main block** at bottom (`if __name__ == "__main__"`)

---

## 🔍 Quick Reference

### Most Important Files (Priority Order)
1. **`streamlit_app.py`** - Main dashboard (use this!)
2. **`README.md`** - Documentation
3. **`dashboard_config.py`** - Configuration
4. **`requirements.txt`** - Dependencies
5. **`chart_components.py`** - Chart library

### File Sizes
- streamlit_app.py: ~500 lines
- chart_components.py: ~400 lines
- create_dashboard.py: ~300 lines
- dashboard_config.py: ~200 lines
- kpi_card.py: ~150 lines

### Lines of Code
- **Total Dashboard Code:** ~1,550 lines
- **Total Documentation:** ~2,000 lines
- **Code-to-Doc Ratio:** 1.3:1 (well documented!)

---

## 🎯 Usage Statistics

### Dashboard Features
- **KPI Cards:** 6
- **Chart Types:** 12
- **Total Visualizations:** 20
- **Filter Options:** 3 (Department, Job Level, Tenure)
- **Data Tables:** 9 (employees, attrition, performance, etc.)

### Supported Platforms
- **Windows:** ✅ Full support (batch file included)
- **macOS:** ✅ Full support (command line)
- **Linux:** ✅ Full support (command line)
- **Web:** ✅ Browser-based (Chrome, Firefox, Safari, Edge)

---

## 📞 Support

### For Issues
1. Check `README.md` for troubleshooting
2. Verify dependencies: `pip install -r requirements.txt`
3. Check Python version: 3.8+ required
4. Review data files in `../data/processed/`

### For Customization
1. See `dashboard_config.py` for colors/themes
2. See `chart_components.py` for chart templates
3. See `streamlit_app.py` for layout modifications

---

**Last Updated:** February 5, 2026  
**Version:** 1.0  
**Maintainer:** HR Analytics Team
