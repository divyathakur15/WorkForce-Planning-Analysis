# 🎯 DASHBOARD ACCESS GUIDE

## ⚡ How to Access the Live Dashboard

### **Quick Start (3 Steps):**

```bash
# 1. Navigate to dashboards folder
cd dashboards

# 2. Install dependencies (first time only)
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run streamlit_app.py
```

### **4. Open Your Browser:**
Streamlit will automatically open, or manually go to:
```
http://localhost:8501
```

---

## 🌐 What You'll See

Once the dashboard loads at `http://localhost:8501`, you'll have:

### **📊 4 Interactive Tabs:**
1. **Overview** - Headcount trends, department distribution, job levels
2. **Demographics** - Age, gender, education, work location breakdown
3. **Attrition Analysis** - Turnover patterns, exit interviews, reasons
4. **Performance & Engagement** - Ratings, satisfaction, goal completion

### **🎯 6 Real-Time KPIs:**
- Total Employees
- Active Employees  
- Attrition Rate
- Avg Performance Score
- Avg Engagement Score
- Avg Satisfaction Score

### **🔍 Dynamic Filters (Left Sidebar):**
- **Department** - Filter by specific departments
- **Job Level** - Entry Level, Mid Level, Senior, Lead, Executive
- **Tenure Range** - Years of experience slider

### **✨ Key Features:**
- ✅ **Meaningful Labels** - No confusing numbers!
  - Job Levels: Entry → Executive
  - Performance: Poor → Excellent
  - Satisfaction: Very Low → Very High
- ✅ **Interactive Charts** - Hover for details, zoom, pan
- ✅ **Real-Time Updates** - Change filters, see instant results
- ✅ **Professional UI** - Vibrant colors, modern design
- ✅ **Export Ready** - Take screenshots, share insights

---

## 🎬 First Time Setup

### **Prerequisites:**
```bash
# Check Python version (need 3.8+)
python --version

# Check pip is installed
pip --version
```

### **Install Dependencies:**
```bash
cd dashboards
pip install -r requirements.txt
```

**Dependencies installed:**
- `streamlit` - Dashboard framework
- `pandas` - Data manipulation
- `plotly` - Interactive visualizations
- `numpy` - Numerical computing

### **Launch Dashboard:**
```bash
streamlit run streamlit_app.py
```

**You'll see:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

---

## 🔧 Troubleshooting

### **Issue: Port 8501 already in use**
```bash
# Kill existing Streamlit process
taskkill /F /IM streamlit.exe

# Or use different port
streamlit run streamlit_app.py --server.port 8502
```

### **Issue: Module not found**
```bash
# Make sure you're in dashboards folder
cd dashboards

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### **Issue: Data not loading**
```bash
# Check data path - should see:
# ../data/processed/*.csv files

# Verify from dashboards folder:
dir ..\data\processed
```

### **Issue: Email prompt on startup**
**Solution:** Just press Enter (leave blank)
- Streamlit asks for email for updates
- It's optional - just press Enter to skip
- Config file already set to skip this

---

## 🎨 Dashboard Features in Detail

### **Overview Tab:**
- **Headcount Over Time** - Line chart showing employee growth
- **Department Distribution** - Pie chart of employees per department
- **Job Level Distribution** - Donut chart with clear labels (Entry → Executive)
- **Location Distribution** - Bar chart of Office/Remote/Hybrid split

### **Demographics Tab:**
- **Gender Distribution** - Gender breakdown pie chart
- **Age Groups** - Histogram of age distribution
- **Marital Status** - Marital status breakdown
- **Education Levels** - From Below College → Doctorate
- **Employment Type** - Full-time vs Contract
- **Work Location** - Office, Remote, Hybrid distribution

### **Attrition Analysis Tab:**
- **Attrition by Department** - Which departments have most turnover
- **Attrition Reasons** - Why employees leave (Work-Life, Salary, etc.)
- **Exit Interview Satisfaction** - Very Dissatisfied → Very Satisfied
- **Rehire Eligibility** - Percentage eligible for rehire

### **Performance & Engagement Tab:**
- **Performance Ratings** - Poor → Excellent distribution
- **Manager Ratings** - How well managers are rated
- **Job Satisfaction** - Very Low → Very High levels
- **Engagement Scores** - Employee engagement levels
- **Goal Completion** - Percentage ranges (0-25%, 26-50%, etc.)
- **Promotion Recommendations** - Who's ready for promotion

---

## ⚠️ Common Confusion: outputs vs dashboards

### **❌ Don't Use:** `notebook/outputs/outputs/`
- **What it is:** Static PNG images and old HTML from initial EDA
- **Purpose:** Reference only, documentation of analysis process
- **Problem:** No interactivity, outdated, confusing numbers

### **✅ Use Instead:** `dashboards/streamlit_app.py`
- **What it is:** Live, interactive dashboard application
- **Purpose:** Real-time analysis, filtering, exploration
- **Benefits:** Interactive, meaningful labels, professional UI

### **Visual Comparison:**

```
❌ OLD (Static):
notebook/outputs/outputs/interactive_dashboard.html
↓
Opens in browser: Static charts, no filters, numbers (1,2,3,4,5)

✅ NEW (Live):
dashboards/streamlit_app.py → http://localhost:8501
↓
Opens in browser: Interactive filters, clear labels, real-time KPIs
```

---

## 📖 Quick Reference

### **To Start Dashboard:**
```bash
cd dashboards && streamlit run streamlit_app.py
```

### **To Stop Dashboard:**
- Press `Ctrl + C` in terminal
- Or close terminal window

### **To Restart Dashboard:**
- Just run the command again
- Changes auto-reload (file watching enabled)

### **Default URL:**
```
http://localhost:8501
```

### **Documentation:**
- Dashboard features: `dashboards/README.md`
- Label improvements: `dashboards/LABEL_IMPROVEMENTS.md`
- Data dictionary: `docs/DATA_DICTIONARY.md`

---

## 🚀 Share Your Dashboard

### **Local Network Access:**
When you run the dashboard, Streamlit shows:
```
Network URL: http://192.168.x.x:8501
```

**Others on your network can access using that URL!**

### **For Production Deployment:**
- Deploy to Streamlit Cloud (free)
- Deploy to Heroku
- Deploy to AWS/Azure
- See: `dashboards/README.md` for deployment guide

---

## 🎯 Best Practices

1. **Always use `dashboards/streamlit_app.py`** for analysis
2. **Bookmark:** `http://localhost:8501` in your browser
3. **Keep terminal open** while using dashboard
4. **Use filters** to explore specific segments
5. **Hover on charts** for detailed tooltips
6. **Take screenshots** for presentations/reports

---

## 📊 Summary

| Aspect | Information |
|--------|-------------|
| **Dashboard Location** | `dashboards/streamlit_app.py` |
| **Access URL** | `http://localhost:8501` |
| **Command** | `streamlit run streamlit_app.py` |
| **Tabs** | 4 (Overview, Demographics, Attrition, Performance) |
| **Visualizations** | 20 interactive charts |
| **KPIs** | 6 real-time metrics |
| **Filters** | Department, Job Level, Tenure |
| **Features** | Meaningful labels, interactive, professional |

---

**Need help?** Check `dashboards/README.md` for detailed documentation!

**Last Updated:** February 5, 2026
