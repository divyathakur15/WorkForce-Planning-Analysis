"""
Rebuild the dashboard with all improvements while keeping tab structure
This will create a clean version with:
- Compact spacing
- Graphics and emojis
- Bolder axes
- Interactive and attractive design
- Tab navigation (NOT single page)
"""

# The complete clean dashboard code
dashboard_code = '''"""
Interactive Streamlit Dashboard for Workforce Planning Analysis
Professional dashboard with filters, KPIs, and dynamic visualizations
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dashboard_config import COLORS, FONTS
from kpi_card import create_kpi_card
from chart_components import (
    create_bar_chart, create_pie_chart, create_donut_chart,
    create_line_chart, create_gauge_chart, create_grouped_bar_chart
)

# Page configuration
st.set_page_config(
    page_title="Workforce Planning Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling with vibrant colors and COMPACT layout
st.markdown("""
    <style>
    /* Main background with gradient */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Content wrapper - EXTRA COMPACT */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
        max-width: 98% !important;
    }
    
    /* Metrics styling - COMPACT */
    .stMetric {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.9) 100%);
        padding: 12px !important;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border-left: 4px solid #2563EB;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .stMetric:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    /* Reduce spacing AGGRESSIVELY */
    .element-container {
        margin-bottom: 0.2rem !important;
        margin-top: 0.2rem !important;
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 24px !important;
        font-weight: 700;
        color: #2563EB;
        animation: fadeIn 0.5s;
    }
    
    div[data-testid="stMetricLabel"] {
        font-size: 11px !important;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Headers - COMPACT */
    h1 {
        color: white;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        margin-bottom: 0.2rem !important;
        margin-top: 0.2rem !important;
        padding: 0 !important;
        animation: slideInDown 0.6s;
    }
    
    h2, h3 {
        color: #1F2937;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 600;
        margin-top: 0.3rem !important;
        margin-bottom: 0.3rem !important;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2563EB 0%, #1E40AF 100%);
    }
    
    section[data-testid="stSidebar"] > div {
        padding-top: 1rem;
    }
    
    /* Sidebar text - all white and bold */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: white !important;
        font-weight: 600 !important;
    }
    
    /* Sidebar labels specific styling */
    section[data-testid="stSidebar"] label {
        font-size: 14px !important;
        margin-bottom: 8px !important;
        margin-top: 16px !important;
        letter-spacing: 0.5px;
    }
    
    /* Filter widgets styling */
    section[data-testid="stSidebar"] .stMultiSelect,
    section[data-testid="stSidebar"] .stSelectbox {
        margin-bottom: 20px !important;
    }
    
    /* Selectbox and multiselect - white background for contrast */
    section[data-testid="stSidebar"] .stMultiSelect > div,
    section[data-testid="stSidebar"] .stSelectbox > div {
        background-color: white;
        border-radius: 8px;
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    /* Slider in sidebar */
    section[data-testid="stSidebar"] .stSlider {
        padding: 20px 0;
    }
    
    section[data-testid="stSidebar"] .stSlider > label {
        color: white !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    
    /* Selectbox and multiselect */
    .stSelectbox, .stMultiSelect {
        background-color: rgba(255,255,255,0.95);
        border-radius: 8px;
    }
    
    /* Tabs styling - MODERN & ATTRACTIVE */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255,255,255,0.9);
        border-radius: 10px;
        padding: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        border-radius: 8px;
        color: #64748B;
        font-weight: 600;
        font-size: 14px;
        padding: 0 20px;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(37, 99, 235, 0.1);
        transform: translateY(-2px);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    
    /* Chart containers - COMPACT */
    .js-plotly-plot {
        background: white;
        border-radius: 12px;
        padding: 8px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        margin-bottom: 0.5rem !important;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .js-plotly-plot:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.12);
    }
    
    /* Info boxes */
    .stAlert {
        background: rgba(255,255,255,0.9);
        border-left: 4px solid #8B5CF6;
        border-radius: 8px;
        margin-bottom: 0.5rem !important;
    }
    
    /* Reduce overall spacing EVERYWHERE */
    .stMarkdown {
        margin-bottom: 0.2rem !important;
        margin-top: 0.2rem !important;
    }
    
    /* Slider styling */
    .stSlider {
        padding-top: 0.3rem !important;
        padding-bottom: 0.3rem !important;
    }
    
    /* Remove excessive padding */
    .row-widget {
        margin-top: 0.2rem !important;
        margin-bottom: 0.2rem !important;
    }
    
    /* Compact columns */
    [data-testid="column"] {
        padding: 0.3rem !important;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideInDown {
        from {
            transform: translateY(-20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    </style>
""", unsafe_allow_html=True)


# ============================================================================
# DATA MAPPINGS - Convert numeric codes to meaningful labels
# ============================================================================

JOB_LEVEL_MAPPING = {
    1: 'Entry Level',
    2: 'Mid Level',
    3: 'Senior Level',
    4: 'Lead/Principal',
    5: 'Executive'
}

PERFORMANCE_RATING_MAPPING = {
    1: 'Poor',
    2: 'Below Expectations',
    3: 'Meets Expectations',
    4: 'Exceeds Expectations',
    5: 'Excellent'
}

MANAGER_RATING_MAPPING = {
    1: 'Poor',
    2: 'Below Average',
    3: 'Average',
    4: 'Above Average',
    5: 'Excellent'
}

EDUCATION_LEVEL_MAPPING = {
    1: 'Below College',
    2: "Bachelor's Degree",
    3: "Master's Degree",
    4: 'Professional Degree',
    5: 'Doctorate (PhD)'
}

EXIT_INTERVIEW_SCORE_MAPPING = {
    1: 'Very Dissatisfied',
    2: 'Dissatisfied',
    3: 'Neutral',
    4: 'Satisfied',
    5: 'Very Satisfied'
}

SATISFACTION_SCORE_MAPPING = {
    1: 'Very Low',
    2: 'Low',
    3: 'Medium',
    4: 'High',
    5: 'Very High'
}


@st.cache_data
def load_data():
    """Load all processed datasets"""
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed')
    
    data = {
        'employees': pd.read_csv(os.path.join(base_path, 'employees_master_cleaned.csv')),
        'attrition': pd.read_csv(os.path.join(base_path, 'attrition_events_cleaned.csv')),
        'performance': pd.read_csv(os.path.join(base_path, 'performance_reviews_cleaned.csv')),
        'engagement': pd.read_csv(os.path.join(base_path, 'engagement_surveys_cleaned.csv')),
        'departments': pd.read_csv(os.path.join(base_path, 'department_master_cleaned.csv')),
        'job_history': pd.read_csv(os.path.join(base_path, 'job_history_cleaned.csv')),
        'compensation': pd.read_csv(os.path.join(base_path, 'compensation_history_cleaned.csv')),
        'training': pd.read_csv(os.path.join(base_path, 'training_and_skills_cleaned.csv')),
        'attendance': pd.read_csv(os.path.join(base_path, 'attendance_records_cleaned.csv'))
    }
    
    # Merge employees with departments
    data['employees'] = data['employees'].merge(data['departments'], on='department_id', how='left')
    
    # Apply mappings to convert numeric codes to readable labels
    data['employees']['job_level_label'] = data['employees']['job_level'].map(JOB_LEVEL_MAPPING)
    data['employees']['education_level_label'] = data['employees']['education_level'].map(EDUCATION_LEVEL_MAPPING)
    
    data['performance']['performance_rating_label'] = data['performance']['performance_rating'].map(PERFORMANCE_RATING_MAPPING)
    data['performance']['manager_rating_label'] = data['performance']['manager_rating'].map(MANAGER_RATING_MAPPING)
    
    data['attrition']['exit_interview_score_label'] = data['attrition']['exit_interview_score'].map(EXIT_INTERVIEW_SCORE_MAPPING)
    
    data['engagement']['job_satisfaction_label'] = data['engagement']['job_satisfaction'].map(SATISFACTION_SCORE_MAPPING)
    data['engagement']['engagement_score_label'] = data['engagement']['engagement_score'].map(SATISFACTION_SCORE_MAPPING)
    
    return data


def apply_filters(data, departments, job_levels, tenure_range):
    """Apply user-selected filters to the data"""
    
    employees = data['employees'].copy()
    
    # Department filter
    if departments:
        employees = employees[employees['department_name'].isin(departments)]
    
    # Job level filter
    if job_levels:
        employees = employees[employees['job_level'].isin(job_levels)]
    
    # Tenure filter
    employees = employees[
        (employees['tenure_years'] >= tenure_range[0]) & 
        (employees['tenure_years'] <= tenure_range[1])
    ]
    
    # Update filtered data
    filtered_data = data.copy()
    filtered_data['employees'] = employees
    
    # Filter related tables
    employee_ids = employees['employee_id'].tolist()
    filtered_data['attrition'] = data['attrition'][data['attrition']['employee_id'].isin(employee_ids)]
    filtered_data['performance'] = data['performance'][data['performance']['employee_id'].isin(employee_ids)]
    filtered_data['engagement'] = data['engagement'][data['engagement']['employee_id'].isin(employee_ids)]
    
    return filtered_data


def calculate_kpis(data):
    """Calculate key performance indicators"""
    
    employees = data['employees']
    attrition = data['attrition']
    engagement = data['engagement']
    
    total_employees = len(employees)
    active_employees = len(employees[employees['status'] == 'Active']) if 'status' in employees.columns else total_employees
    attrition_count = len(attrition)
    attrition_rate = (attrition_count / total_employees * 100) if total_employees > 0 else 0
    retention_rate = 100 - attrition_rate
    avg_tenure = employees['tenure_years'].mean() if not employees.empty else 0
    
    # Check for correct satisfaction column name
    if 'engagement_score' in engagement.columns and not engagement.empty:
        avg_satisfaction = engagement['engagement_score'].mean()
    elif 'job_satisfaction' in engagement.columns and not engagement.empty:
        avg_satisfaction = engagement['job_satisfaction'].mean()
    else:
        avg_satisfaction = 0
    
    return {
        'total_employees': total_employees,
        'active_employees': active_employees,
        'attrition_rate': attrition_rate,
        'retention_rate': retention_rate,
        'avg_tenure': avg_tenure,
        'avg_satisfaction': avg_satisfaction
    }


def main():
    """Main dashboard application"""
    
    # COMPACT HEADER WITH GRAPHICS
    st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.05) 100%); 
                    border-radius: 15px; padding: 0.8rem 2rem 0.6rem 2rem; margin-bottom: 0.5rem;
                    border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 8px 32px rgba(0,0,0,0.1);'>
            <div style='text-align: center;'>
                <div style='font-size: 2.8rem; margin-bottom: 0.2rem; animation: pulse 2s infinite;'>
                    📊 💼 👥 📈
                </div>
                <h1 style='font-size: 2.2rem; margin: 0; padding: 0; line-height: 1.2;'>
                    Workforce Planning Dashboard
                </h1>
                <p style='font-size: 0.95rem; color: rgba(255,255,255,0.95); margin: 0.2rem 0 0 0; 
                          font-weight: 500; letter-spacing: 1px;'>
                    ⚡ Real-time HR Analytics & Strategic Insights ⚡
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Load data
    with st.spinner("Loading data..."):
        data = load_data()
    
    # Sidebar filters with better styling
    st.sidebar.markdown("""
        <div style='text-align: center; padding: 1rem 0 0.8rem 0;'>
            <div style='font-size: 2rem; margin-bottom: 0.3rem;'>🔍</div>
            <h1 style='color: white; font-size: 1.8rem; margin: 0; font-weight: 700;'>FILTERS</h1>
            <p style='color: rgba(255,255,255,0.8); margin: 0.3rem 0 0 0; font-size: 0.85rem;'>
                Customize your view
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("<div style='height: 2px; background: rgba(255,255,255,0.3); margin: 1rem 0;'></div>", unsafe_allow_html=True)
    
    # Department filter with label
    st.sidebar.markdown("""
        <div style='margin-bottom: 0.5rem;'>
            <p style='color: white; font-weight: 600; font-size: 14px; margin: 0; letter-spacing: 0.5px;'>
                🏢 DEPARTMENTS
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Department filter
    all_departments = sorted(data['employees']['department_name'].unique())
    selected_departments = st.sidebar.multiselect(
        "Select departments to analyze",
        options=all_departments,
        default=all_departments,
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown("<div style='margin: 1rem 0;'></div>", unsafe_allow_html=True)
    
    # Job level filter with label
    st.sidebar.markdown("""
        <div style='margin-bottom: 0.5rem;'>
            <p style='color: white; font-weight: 600; font-size: 14px; margin: 0; letter-spacing: 0.5px;'>
                👔 JOB LEVELS
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Job level filter - show meaningful labels but use numeric values for filtering
    all_job_levels = sorted(data['employees']['job_level'].unique())
    job_level_options = {level: JOB_LEVEL_MAPPING[level] for level in all_job_levels}
    selected_job_level_labels = st.sidebar.multiselect(
        "Select job levels to analyze",
        options=list(job_level_options.values()),
        default=list(job_level_options.values()),
        label_visibility="collapsed"
    )
    # Convert back to numeric values for filtering
    selected_job_levels = [k for k, v in job_level_options.items() if v in selected_job_level_labels]
    
    st.sidebar.markdown("<div style='margin: 1rem 0;'></div>", unsafe_allow_html=True)
    
    # Tenure filter with label
    st.sidebar.markdown("""
        <div style='margin-bottom: 0.5rem;'>
            <p style='color: white; font-weight: 600; font-size: 14px; margin: 0; letter-spacing: 0.5px;'>
                📅 TENURE RANGE
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Tenure filter
    max_tenure = int(data['employees']['tenure_years'].max())
    tenure_range = st.sidebar.slider(
        "Select tenure range in years",
        min_value=0,
        max_value=max_tenure,
        value=(0, max_tenure),
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown("<div style='height: 2px; background: rgba(255,255,255,0.3); margin: 1.5rem 0 1rem 0;'></div>", unsafe_allow_html=True)
    
    # Filter summary
    st.sidebar.markdown(f"""
        <div style='background: rgba(255,255,255,0.15); padding: 0.8rem; border-radius: 10px; margin-top: 1rem; 
                    border: 1px solid rgba(255,255,255,0.2);'>
            <p style='color: white; font-size: 0.85rem; margin: 0 0 0.4rem 0; font-weight: 600;'>
                📊 ACTIVE FILTERS
            </p>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.8rem; margin: 0.3rem 0; line-height: 1.4;'>
                • <b>{len(selected_departments)}</b> of {len(all_departments)} Departments
            </p>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.8rem; margin: 0.3rem 0; line-height: 1.4;'>
                • <b>{len(selected_job_levels)}</b> of {len(all_job_levels)} Job Levels
            </p>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.8rem; margin: 0.3rem 0; line-height: 1.4;'>
                • Tenure: <b>{tenure_range[0]}-{tenure_range[1]}</b> years
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("<div style='margin: 1rem 0;'></div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 0.8rem; border-radius: 10px; border: 1px solid rgba(255,255,255,0.2);'>
            <p style='color: white; font-size: 0.85rem; margin: 0; line-height: 1.5;'>
                💡 <b>Quick Tip:</b><br/>
                <span style='color: rgba(255,255,255,0.85); font-size: 0.8rem;'>
                Use filters to drill down into specific workforce segments and discover actionable insights!
                </span>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Apply filters
    filtered_data = apply_filters(data, selected_departments, selected_job_levels, tenure_range)
    
    # Calculate KPIs
    kpis = calculate_kpis(filtered_data)
    
    # KPI Cards - COMPACT
    st.markdown("""
        <div style='background: rgba(255,255,255,0.95); padding: 0.5rem 1rem; border-radius: 10px; 
                    margin-bottom: 0.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h3 style='margin: 0; color: #2563EB; font-size: 1.1rem;'>📈 Key Performance Indicators</h3>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.metric(
            label="👥 Total Employees",
            value=f"{kpis['total_employees']:,}",
            delta=None
        )
    
    with col2:
        st.metric(
            label="✓ Active Employees",
            value=f"{kpis['active_employees']:,}",
            delta=None
        )
    
    with col3:
        st.metric(
            label="📉 Attrition Rate",
            value=f"{kpis['attrition_rate']:.1f}%",
            delta=f"{kpis['attrition_rate'] - 24:.1f}%" if kpis['attrition_rate'] > 0 else None,
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            label="📈 Retention Rate",
            value=f"{kpis['retention_rate']:.1f}%",
            delta=None
        )
    
    with col5:
        st.metric(
            label="📅 Avg Tenure",
            value=f"{kpis['avg_tenure']:.1f} yrs",
            delta=None
        )
    
    with col6:
        st.metric(
            label="😊 Avg Satisfaction",
            value=f"{kpis['avg_satisfaction']:.1f}/5",
            delta=None
        )
    
    # Main visualizations with TABS (keeping tab structure)
    st.markdown("<div style='margin: 0.5rem 0;'></div>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "👥 Demographics", "📉 Attrition Analysis", "💼 Performance & Engagement"])
    
    with tab1:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 100%); 
                        padding: 0.6rem 1.5rem; border-radius: 10px; margin-bottom: 0.6rem;
                        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);'>
                <h3 style='margin: 0; color: white; font-size: 1.2rem; font-weight: 700;'>📊 Overview Analytics</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Department headcount
            dept_counts = filtered_data['employees']['department_name'].value_counts().head(10)
            fig = create_bar_chart(
                pd.DataFrame({'department': dept_counts.index, 'count': dept_counts.values}),
                'department', 'count',
                'Top 10 Departments by Headcount',
                color=COLORS['primary']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Job level distribution
            job_level_counts = filtered_data['employees']['job_level_label'].value_counts()
            fig = create_donut_chart(
                pd.DataFrame({'level': job_level_counts.index, 'count': job_level_counts.values}),
                'count', 'level',
                'Employees by Job Level',
                colors=COLORS['chart_colors']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            # Tenure distribution
            tenure_dist = filtered_data['employees']['tenure_category'].value_counts()
            fig = create_bar_chart(
                pd.DataFrame({'category': tenure_dist.index, 'count': tenure_dist.values}),
                'category', 'count',
                'Tenure Distribution',
                color=COLORS['info']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col4:
            # Attrition rate gauge
            fig = create_gauge_chart(
                kpis['attrition_rate'],
                'Attrition Rate (%)',
                min_val=0,
                max_val=50,
                threshold_low=15,
                threshold_high=25
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #10B981 0%, #06B6D4 100%); 
                        padding: 0.6rem 1.5rem; border-radius: 10px; margin-bottom: 0.6rem;
                        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);'>
                <h3 style='margin: 0; color: white; font-size: 1.2rem; font-weight: 700;'>👥 Demographic Analytics</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Gender distribution
            gender_counts = filtered_data['employees']['gender'].value_counts()
            fig = create_pie_chart(
                pd.DataFrame({'gender': gender_counts.index, 'count': gender_counts.values}),
                'count', 'gender',
                'Gender Distribution',
                colors=[COLORS['primary'], COLORS['secondary']]
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Age group distribution
            age_group_counts = filtered_data['employees']['age_group'].value_counts()
            fig = create_bar_chart(
                pd.DataFrame({'age_group': age_group_counts.index, 'count': age_group_counts.values}),
                'age_group', 'count',
                'Age Group Distribution',
                color=COLORS['secondary']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Second row for more demographics
        col3, col4 = st.columns(2)
        
        with col3:
            # Marital Status distribution
            if 'marital_status' in filtered_data['employees'].columns:
                marital_counts = filtered_data['employees']['marital_status'].value_counts()
                fig = create_donut_chart(
                    pd.DataFrame({'status': marital_counts.index, 'count': marital_counts.values}),
                    'count', 'status',
                    'Marital Status Distribution',
                    colors=COLORS['chart_colors']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col4:
            # Education Level distribution
            if 'education_level_label' in filtered_data['employees'].columns:
                edu_counts = filtered_data['employees']['education_level_label'].value_counts()
                # Sort by original numeric order
                sort_order = ['Below College', "Bachelor's Degree", "Master's Degree", 'Professional Degree', 'Doctorate (PhD)']
                edu_counts = edu_counts.reindex([x for x in sort_order if x in edu_counts.index])
                fig = create_bar_chart(
                    pd.DataFrame({'level': edu_counts.index, 'count': edu_counts.values}),
                    'level', 'count',
                    'Education Level Distribution',
                    color=COLORS['info']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # Third row
        col5, col6 = st.columns(2)
        
        with col5:
            # Employment Type
            if 'employment_type' in filtered_data['employees'].columns:
                emp_type_counts = filtered_data['employees']['employment_type'].value_counts()
                fig = create_pie_chart(
                    pd.DataFrame({'type': emp_type_counts.index, 'count': emp_type_counts.values}),
                    'count', 'type',
                    'Employment Type Distribution',
                    colors=COLORS['chart_colors']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col6:
            # Work Location
            if 'work_location' in filtered_data['employees'].columns:
                location_counts = filtered_data['employees']['work_location'].value_counts()
                fig = create_bar_chart(
                    pd.DataFrame({'location': location_counts.index, 'count': location_counts.values}),
                    'location', 'count',
                    'Work Location Distribution',
                    color=COLORS['accent']
                )
                st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #EF4444 0%, #F59E0B 100%); 
                        padding: 0.6rem 1.5rem; border-radius: 10px; margin-bottom: 0.6rem;
                        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);'>
                <h3 style='margin: 0; color: white; font-size: 1.2rem; font-weight: 700;'>📉 Attrition Analytics</h3>
            </div>
        """, unsafe_allow_html=True)
        
        employees = filtered_data['employees']
        attrition = filtered_data['attrition']
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Attrition by department
            attrition_dept = attrition.merge(employees[['employee_id', 'department_name']], on='employee_id', how='left')
            dept_attr = attrition_dept['department_name'].value_counts().head(10)
            fig = create_bar_chart(
                pd.DataFrame({'department': dept_attr.index, 'count': dept_attr.values}),
                'department', 'count',
                'Attrition by Department',
                color=COLORS['danger'],
                horizontal=True
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Attrition by reason
            if 'attrition_reason' in attrition.columns and not attrition.empty:
                reason_counts = attrition['attrition_reason'].value_counts().head(8)
                fig = create_donut_chart(
                    pd.DataFrame({'reason': reason_counts.index, 'count': reason_counts.values}),
                    'count', 'reason',
                    'Top Attrition Reasons',
                    colors=COLORS['chart_colors']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # Additional row for more insights
        col3, col4 = st.columns(2)
        
        with col3:
            # Exit interview scores
            if 'exit_interview_score_label' in attrition.columns and not attrition.empty:
                exit_scores = attrition['exit_interview_score_label'].value_counts()
                # Sort by satisfaction level
                sort_order = ['Very Dissatisfied', 'Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
                exit_scores = exit_scores.reindex([x for x in sort_order if x in exit_scores.index])
                fig = create_bar_chart(
                    pd.DataFrame({'score': exit_scores.index, 'count': exit_scores.values}),
                    'score', 'count',
                    'Exit Interview Satisfaction',
                    color=COLORS['warning']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col4:
            # Rehire eligibility
            if 'rehire_eligible' in attrition.columns and not attrition.empty:
                rehire_counts = attrition['rehire_eligible'].value_counts()
                fig = create_pie_chart(
                    pd.DataFrame({'eligible': rehire_counts.index, 'count': rehire_counts.values}),
                    'count', 'eligible',
                    'Rehire Eligibility',
                    colors=[COLORS['success'], COLORS['danger']]
                )
                st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%); 
                        padding: 0.6rem 1.5rem; border-radius: 10px; margin-bottom: 0.6rem;
                        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);'>
                <h3 style='margin: 0; color: white; font-size: 1.2rem; font-weight: 700;'>💼 Performance & Engagement Analytics</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Performance rating distribution
            performance = filtered_data['performance']
            if not performance.empty and 'performance_rating_label' in performance.columns:
                perf_counts = performance['performance_rating_label'].value_counts()
                # Sort by performance level
                sort_order = ['Poor', 'Below Expectations', 'Meets Expectations', 'Exceeds Expectations', 'Excellent']
                perf_counts = perf_counts.reindex([x for x in sort_order if x in perf_counts.index])
                fig = create_bar_chart(
                    pd.DataFrame({'rating': perf_counts.index, 'count': perf_counts.values}),
                    'rating', 'count',
                    'Performance Rating Distribution',
                    color=COLORS['success']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Manager rating distribution
            if not performance.empty and 'manager_rating_label' in performance.columns:
                manager_counts = performance['manager_rating_label'].value_counts()
                # Sort by rating level
                sort_order = ['Poor', 'Below Average', 'Average', 'Above Average', 'Excellent']
                manager_counts = manager_counts.reindex([x for x in sort_order if x in manager_counts.index])
                fig = create_bar_chart(
                    pd.DataFrame({'rating': manager_counts.index, 'count': manager_counts.values}),
                    'rating', 'count',
                    'Manager Rating Distribution',
                    color=COLORS['info']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # Second row
        col3, col4 = st.columns(2)
        
        with col3:
            # Job Satisfaction distribution
            engagement = filtered_data['engagement']
            if not engagement.empty and 'job_satisfaction_label' in engagement.columns:
                satisfaction_counts = engagement['job_satisfaction_label'].value_counts()
                # Sort by satisfaction level
                sort_order = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
                satisfaction_counts = satisfaction_counts.reindex([x for x in sort_order if x in satisfaction_counts.index])
                fig = create_bar_chart(
                    pd.DataFrame({'satisfaction': satisfaction_counts.index, 'count': satisfaction_counts.values}),
                    'satisfaction', 'count',
                    'Job Satisfaction Levels',
                    color=COLORS['primary']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col4:
            # Engagement Score distribution
            if not engagement.empty and 'engagement_score_label' in engagement.columns:
                engagement_counts = engagement['engagement_score_label'].value_counts()
                # Sort by engagement level
                sort_order = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
                engagement_counts = engagement_counts.reindex([x for x in sort_order if x in engagement_counts.index])
                fig = create_bar_chart(
                    pd.DataFrame({'score': engagement_counts.index, 'count': engagement_counts.values}),
                    'score', 'count',
                    'Overall Engagement Levels',
                    color=COLORS['secondary']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # Third row
        col5, col6 = st.columns(2)
        
        with col5:
            # Goal Completion
            if not performance.empty and 'goal_completion_pct' in performance.columns:
                # Create bins for goal completion
                performance['goal_bin'] = pd.cut(performance['goal_completion_pct'], 
                                                bins=[0, 25, 50, 75, 100], 
                                                labels=['0-25%', '26-50%', '51-75%', '76-100%'])
                goal_counts = performance['goal_bin'].value_counts().sort_index()
                fig = create_bar_chart(
                    pd.DataFrame({'completion': goal_counts.index.astype(str), 'count': goal_counts.values}),
                    'completion', 'count',
                    'Goal Completion Distribution',
                    color=COLORS['accent']
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col6:
            # Promotion recommendations
            if not performance.empty and 'promotion_recommendation' in performance.columns:
                promo_counts = performance['promotion_recommendation'].value_counts()
                fig = create_donut_chart(
                    pd.DataFrame({'recommended': promo_counts.index, 'count': promo_counts.values}),
                    'count', 'recommended',
                    'Promotion Recommendations',
                    colors=[COLORS['success'], COLORS['medium']]
                )
                st.plotly_chart(fig, use_container_width=True)
    
    # Footer with gradient
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 100%); 
                    padding: 1.5rem; border-radius: 12px; text-align: center; margin-top: 1rem;
                    box-shadow: 0 8px 24px rgba(0,0,0,0.15);'>
            <h3 style='color: white; margin: 0 0 0.5rem 0; font-size: 1.3rem;'>✨ Workforce Planning Dashboard ✨</h3>
            <p style='color: rgba(255,255,255,0.9); margin: 0; font-size: 0.95rem;'>
                Powered by Python, Streamlit & Plotly | Real-time HR Analytics
            </p>
            <p style='color: rgba(255,255,255,0.7); margin: 0.5rem 0 0 0; font-size: 0.85rem;'>
                © 2026 HR Analytics Team | Built with ❤️ for Data-Driven Decisions
            </p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
'''

# Write the clean dashboard
with open('streamlit_app.py', 'w', encoding='utf-8') as f:
    f.write(dashboard_code)

print("✅ Dashboard successfully rebuilt with all improvements!")
print("✅ Kept tab navigation structure")
print("✅ Applied compact spacing")
print("✅ Added graphics and emojis")
print("✅ Made charts interactive with hover effects")
print("✅ Bolder axis titles already applied in chart_components.py")
print("\n🎉 Your dashboard is ready! Streamlit should auto-reload.")
