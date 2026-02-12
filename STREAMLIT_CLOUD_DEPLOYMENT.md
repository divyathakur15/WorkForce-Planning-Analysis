# 🚀 Deploy to Streamlit Community Cloud (FREE)

## ⚡ Quick Deploy Guide

### **Step 1: Ensure Your GitHub Repo is Ready**

Your repository already has everything needed:
- ✅ `dashboards/streamlit_app.py` - Main app
- ✅ `dashboards/requirements.txt` - Dependencies
- ✅ Already pushed to GitHub

### **Step 2: Sign Up for Streamlit Cloud**

1. Go to: **https://streamlit.io/cloud**
2. Click **"Sign up"**
3. Choose **"Continue with GitHub"**
4. Authorize Streamlit to access your GitHub repos

### **Step 3: Deploy Your App**

1. Click **"New app"** button
2. Fill in the details:
   - **Repository:** `divyathakur15/WorkForce-Planning-Analysis`
   - **Branch:** `main`
   - **Main file path:** `dashboards/streamlit_app.py`
   - **App URL:** Choose your custom name (e.g., `workforce-analytics`)

3. Click **"Deploy!"**

### **Step 4: Wait for Deployment**
- First deployment takes 2-5 minutes
- You'll see build logs in real-time
- Once done, your app will be live!

### **Your App URL Will Be:**
```
https://workforce-analytics-[your-username].streamlit.app
```

---

## 📝 Important Files to Check

### **1. Requirements.txt Location**
Make sure `dashboards/requirements.txt` exists with all dependencies:

```txt
streamlit>=1.31.0
pandas>=2.0.0
plotly>=5.18.0
numpy>=1.24.0
```

### **2. Data Files Path**
Update `dashboards/streamlit_app.py` to use relative paths:

```python
# Instead of absolute paths, use:
DATA_PATH = "../Raw dataset/"
```

---

## 🔧 Advanced Configuration (Optional)

### **Create `.streamlit/config.toml`**
For custom theming and settings:

```toml
[theme]
primaryColor = "#2563EB"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F9FF"
textColor = "#1E293B"
font = "sans serif"

[server]
headless = true
enableCORS = false
enableXsrfProtection = true
```

### **Create `dashboards/.streamlit/secrets.toml`** (if needed)
For sensitive data (API keys, passwords):

```toml
# This file is gitignored and only on Streamlit Cloud
[secrets]
api_key = "your-api-key"
```

---

## 🎯 Post-Deployment Steps

### **1. Test Your Live App**
- Click through all 5 tabs
- Test filters and interactions
- Verify all charts load correctly

### **2. Share Your App**
Once deployed, share the URL:
- Add to your GitHub README
- Share on LinkedIn
- Add to your portfolio
- Include in resume

### **3. Monitor Usage**
- Check Streamlit Cloud dashboard for:
  - Number of visitors
  - App performance
  - Resource usage
  - Error logs

---

## 🔄 Automatic Updates

Once deployed, any changes you push to GitHub will automatically redeploy:

```bash
# Make changes to your code
git add .
git commit -m "Update dashboard features"
git push origin main

# Streamlit Cloud will automatically redeploy! 🎉
```

---

## 💰 Cost

**Streamlit Community Cloud:**
- ✅ **FREE** for public repositories
- ✅ Unlimited apps
- ✅ 1 GB RAM per app
- ✅ Shared CPU resources

**Streamlit for Teams** (if you need more):
- 💰 $250/month for team features
- More resources and private repos

---

## 🆘 Troubleshooting

### **Issue 1: Module Not Found**
**Solution:** Add missing package to `dashboards/requirements.txt`

### **Issue 2: File Not Found**
**Solution:** Use relative paths, not absolute Windows paths

### **Issue 3: Memory Limit Exceeded**
**Solution:** Optimize data loading (use caching)

### **Issue 4: App Won't Start**
**Solution:** Check logs on Streamlit Cloud dashboard

---

## 📊 Expected Deployment Result

After deployment, you'll have:
- 🌐 **Live URL:** `https://your-app.streamlit.app`
- 📱 **Mobile-responsive** dashboard
- 🔄 **Auto-updates** from GitHub
- 📈 **Analytics** on usage
- 🎨 **Professional** appearance

---

## 🎉 Success!

Your Workforce Planning Dashboard will be:
- ✅ Accessible worldwide 24/7
- ✅ Professional portfolio piece
- ✅ Shareable with employers/clients
- ✅ Automatically updated from GitHub

---

**Ready to deploy? Visit:** https://streamlit.io/cloud

*Deployment Guide Created: February 13, 2026*
