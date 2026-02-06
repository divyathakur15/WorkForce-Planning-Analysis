"""
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

# Custom CSS for professional styling with vibrant colors and compact layout
st.markdown("""
    <style>
    /* Main background with subtle gradient */
    .main {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 50%, #f0fdf4 100%);
        background-attachment: fixed;
    }
    
    /* Content wrapper - EXTRA COMPACT */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
        max-width: 98% !important;
    }
    
    /* Metrics styling */
    .stMetric {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.9) 100%);
        padding: 15px !important;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border-left: 4px solid #2563EB;
        transition: transform 0.2s;
    }
    
    .stMetric:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    /* Reduce spacing AGGRESSIVELY */
    .element-container {
        margin-bottom: 0.2rem !important;
        margin-top: 0.2rem !important;
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 26px !important;
        font-weight: 700;
        color: #2563EB;
    }
    
    div[data-testid="stMetricLabel"] {
        font-size: 12px !important;
        font-weight: 600;
        color: #1e293b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Headers - COMPACT */
    h1 {
        color: #1e293b;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0.2rem !important;
        margin-top: 0.2rem !important;
        padding: 0 !important;
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
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255,255,255,0.9);
        border-radius: 10px;
        padding: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        border-radius: 8px;
        color: #64748B;
        font-weight: 600;
        font-size: 14px;
        padding: 0 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 100%);
        color: white;
    }
    
    /* Chart containers - COMPACT */
    .js-plotly-plot {
        background: white;
        border-radius: 12px;
        padding: 8px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        margin-bottom: 0.5rem !important;
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
    
    /* Compact chart titles */
    .plotly .gtitle {
        font-weight: 700 !important;
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
    
    # Compact header with graphics
    st.markdown("""
        <div style='background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 50%, #EC4899 100%); 
                    border-radius: 15px; padding: 1rem 2rem 0.8rem 2rem; margin-bottom: 0.5rem;
                    border: 2px solid rgba(255,255,255,0.3); box-shadow: 0 8px 32px rgba(37, 99, 235, 0.3);'>
            <div style='text-align: center;'>
                <div style='font-size: 3.5rem; margin-bottom: 0.3rem; animation: pulse 2s ease-in-out infinite;'>
                    📊 💼 👥
                </div>
                <h1 style='font-size: 2.5rem; margin: 0; padding: 0; line-height: 1.2; color: white;'>
                    Workforce Planning Dashboard
                </h1>
                <p style='font-size: 1rem; color: rgba(255,255,255,0.95); margin: 0.3rem 0 0 0; 
                          font-weight: 500; letter-spacing: 1px;'>
                    ⚡ Real-time HR Analytics & Strategic Insights ⚡
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Load data
    with st.spinner("Loading data..."):
        data = load_data()
    
    # Sidebar filters with better styling - Compact and attractive
    st.sidebar.markdown("""
        <div style='text-align: center; padding: 0.5rem 0 0.5rem 0; 
                    background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 50%, #EC4899 100%);
                    border-radius: 12px; margin: -1rem -1rem 1rem -1rem; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);'>
            <div style='font-size: 2rem; margin-bottom: 0.2rem; animation: pulse 2s ease-in-out infinite;'>
                🔍
            </div>
            <h1 style='color: white; font-size: 1.6rem; margin: 0; font-weight: 700; letter-spacing: 2px;'>FILTERS</h1>
            <p style='color: rgba(255,255,255,0.95); margin: 0.2rem 0 0 0; font-size: 0.85rem; font-weight: 500;'>
                ⚡ Customize Your View ⚡
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("<div style='margin: 1rem 0 0.5rem 0;'></div>", unsafe_allow_html=True)
    
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
    
    st.sidebar.markdown("<div style='margin: 0.8rem 0;'></div>", unsafe_allow_html=True)
    
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
    
    st.sidebar.markdown("<div style='margin: 0.8rem 0;'></div>", unsafe_allow_html=True)
    
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
    
    st.sidebar.markdown("<div style='height: 2px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent); margin: 1.2rem 0 1rem 0;'></div>", unsafe_allow_html=True)
    
    # Filter summary
    st.sidebar.markdown(f"""
        <div style='background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 10px; margin-top: 1rem; border: 1px solid rgba(255,255,255,0.2);'>
            <p style='color: white; font-size: 0.85rem; margin: 0 0 0.5rem 0; font-weight: 600;'>
                📊 ACTIVE FILTERS
            </p>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.8rem; margin: 0.3rem 0; line-height: 1.5;'>
                • <b>{len(selected_departments)}</b> of {len(all_departments)} Departments
            </p>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.8rem; margin: 0.3rem 0; line-height: 1.5;'>
                • <b>{len(selected_job_levels)}</b> of {len(all_job_levels)} Job Levels
            </p>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.8rem; margin: 0.3rem 0; line-height: 1.5;'>
                • Tenure: <b>{tenure_range[0]}-{tenure_range[1]}</b> years
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; border: 1px solid rgba(255,255,255,0.2);'>
            <p style='color: white; font-size: 0.85rem; margin: 0; line-height: 1.6;'>
                💡 <b>Quick Tip:</b><br/>
                <span style='color: rgba(255,255,255,0.85); font-size: 0.8rem;'>
                Use filters to drill down into specific workforce segments and discover actionable insights for strategic decision-making.
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
        # Industry benchmark for attrition is 15%
        industry_benchmark = 15.0
        attrition_delta = kpis['attrition_rate'] - industry_benchmark
        
        st.metric(
            label="📉 Attrition Rate",
            value=f"{kpis['attrition_rate']:.1f}%",
            delta=f"{attrition_delta:+.1f}% vs Industry (15%)" if kpis['attrition_rate'] > 0 else None,
            delta_color="inverse",
            help="Comparing against industry benchmark of 15%. Higher delta means higher attrition risk."
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
    
    # Explanation box for KPI deltas
    st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%); 
                    padding: 0.6rem 1rem; border-radius: 8px; margin: 0.5rem 0; 
                    border-left: 4px solid #3B82F6;'>
            <p style='margin: 0; font-size: 0.85rem; color: #1e293b; line-height: 1.5;'>
                <strong>ℹ️ Understanding Attrition Delta:</strong> The attrition rate shows 
                <strong style='color: #EF4444;'>{attrition_delta:+.1f}%</strong> compared to the industry benchmark of 
                <strong>15%</strong>. 
                {"⚠️ This means your attrition is HIGHER than industry average - retention strategies needed!" if attrition_delta > 0 else "✅ Great! Your attrition is BELOW industry average - keep up current practices!"}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Main visualizations with TABS
    st.markdown("<div style='margin: 0.5rem 0;'></div>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "👥 Demographics", "📉 Attrition Analysis", "💼 Performance & Engagement", "📈 Insights & Recommendations"])
    
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
            st.markdown("""
                <div style='background: rgba(37, 99, 235, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #2563EB; margin-bottom: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Horizontal Bar Chart</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Number of Employees | <strong>Y-Axis:</strong> Department Names</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Top 10 departments with highest employee count</p>
                </div>
            """, unsafe_allow_html=True)
            
            dept_counts = filtered_data['employees']['department_name'].value_counts().head(10)
            fig = create_bar_chart(
                pd.DataFrame({'department': dept_counts.index, 'count': dept_counts.values}),
                'department', 'count',
                'Top 10 Departments by Headcount',
                color=COLORS['primary']
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown(f"""
                <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                    <em>{dept_counts.index[0]}</em> has the largest workforce with <strong>{dept_counts.values[0]:,}</strong> employees, 
                    representing <strong>{(dept_counts.values[0]/dept_counts.sum()*100):.1f}%</strong> of top 10 departments.</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Job level distribution
            st.markdown("""
                <div style='background: rgba(139, 92, 246, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #8B5CF6; margin-bottom: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Donut Chart</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Segments:</strong> Job Level Categories | <strong>Size:</strong> Employee Count</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Distribution of employees across organizational hierarchy</p>
                </div>
            """, unsafe_allow_html=True)
            
            job_level_counts = filtered_data['employees']['job_level_label'].value_counts()
            # Remove any NaN or undefined values
            job_level_counts = job_level_counts[job_level_counts.index.notna()]
            fig = create_donut_chart(
                pd.DataFrame({'level': job_level_counts.index, 'count': job_level_counts.values}),
                'count', 'level',
                'Employees by Job Level',
                colors=COLORS['chart_colors']
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown(f"""
                <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                    Majority of workforce is at <em>{job_level_counts.index[0]}</em> level (<strong>{(job_level_counts.values[0]/job_level_counts.sum()*100):.1f}%</strong>), 
                    indicating a {"healthy pyramid structure" if job_level_counts.index[0] in ["Entry Level", "Mid Level"] else "top-heavy organization"}.</p>
                </div>
            """, unsafe_allow_html=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            # Tenure distribution
            st.markdown("""
                <div style='background: rgba(59, 130, 246, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #3B82F6; margin-bottom: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Vertical Bar Chart</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Tenure Categories | <strong>Y-Axis:</strong> Number of Employees</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> How long employees have been with the organization</p>
                </div>
            """, unsafe_allow_html=True)
            
            tenure_dist = filtered_data['employees']['tenure_category'].value_counts()
            fig = create_bar_chart(
                pd.DataFrame({'category': tenure_dist.index, 'count': tenure_dist.values}),
                'category', 'count',
                'Tenure Distribution',
                color=COLORS['info']
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown(f"""
                <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                    Most employees fall in <em>{tenure_dist.index[0]}</em> category, suggesting {"high retention" if "5+" in tenure_dist.index[0] else "recent hiring growth"}. 
                    Average tenure is <strong>{kpis['avg_tenure']:.1f} years</strong>.</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col4:
            # Attrition rate gauge
            st.markdown("""
                <div style='background: rgba(239, 68, 68, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #EF4444; margin-bottom: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Gauge Chart</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Range:</strong> 0% to 50% | <strong>Zones:</strong> Green (0-15%), Yellow (15-25%), Red (25-50%)</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Current attrition rate vs industry benchmark of 15%</p>
                </div>
            """, unsafe_allow_html=True)
            
            fig = create_gauge_chart(
                kpis['attrition_rate'],
                'Attrition Rate (%)',
                min_val=0,
                max_val=50,
                threshold_low=15,
                threshold_high=25
            )
            st.plotly_chart(fig, use_container_width=True)
            
            attrition_status = "🟢 Excellent" if kpis['attrition_rate'] < 15 else ("🟡 Moderate" if kpis['attrition_rate'] < 25 else "🔴 High")
            benchmark_diff = kpis['attrition_rate'] - 15  # 15% is industry benchmark
            st.markdown(f"""
                <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                    Attrition rate is <strong>{kpis['attrition_rate']:.1f}%</strong> ({attrition_status}), which is 
                    <strong>{abs(benchmark_diff):.1f}% {"ABOVE" if benchmark_diff > 0 else "BELOW"}</strong> the industry benchmark (15%). 
                    {
                        "This is within healthy range - maintain current retention practices!" if kpis['attrition_rate'] < 15 else
                        "Moderate concern - implement proactive retention strategies." if kpis['attrition_rate'] < 25 else
                        "⚠️ Critical! Immediate action needed to reduce turnover and retain talent."
                    }</p>
                </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #10B981 0%, #06B6D4 100%); padding: 0.8rem 1.5rem; border-radius: 10px; margin-bottom: 1rem;'>
                <h3 style='margin: 0; color: white; font-size: 1.2rem;'>👥 Demographic Analytics</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Gender distribution
            st.markdown("""
                <div style='background: rgba(37, 99, 235, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #2563EB; margin-bottom: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Pie Chart</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Segments:</strong> Gender Categories | <strong>Size:</strong> Employee Count</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Gender diversity across the organization</p>
                </div>
            """, unsafe_allow_html=True)
            
            gender_counts = filtered_data['employees']['gender'].value_counts()
            fig = create_pie_chart(
                pd.DataFrame({'gender': gender_counts.index, 'count': gender_counts.values}),
                'count', 'gender',
                'Gender Distribution',
                colors=[COLORS['primary'], COLORS['secondary']]
            )
            st.plotly_chart(fig, use_container_width=True)
            
            total_gender = gender_counts.sum()
            male_pct = (gender_counts.get('Male', 0) / total_gender * 100) if total_gender > 0 else 0
            female_pct = (gender_counts.get('Female', 0) / total_gender * 100) if total_gender > 0 else 0
            st.markdown(f"""
                <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                    Workforce is <strong>{male_pct:.1f}% Male</strong> and <strong>{female_pct:.1f}% Female</strong>. 
                    {
                        "Excellent gender balance! 🎉" if abs(male_pct - 50) < 10 else
                        "Moving toward better gender diversity." if abs(male_pct - 50) < 20 else
                        "⚠️ Consider diversity initiatives to improve gender balance."
                    }</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Age group distribution
            st.markdown("""
                <div style='background: rgba(139, 92, 246, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #8B5CF6; margin-bottom: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Vertical Bar Chart</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Age Groups | <strong>Y-Axis:</strong> Number of Employees</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Age distribution and generational mix</p>
                </div>
            """, unsafe_allow_html=True)
            
            age_group_counts = filtered_data['employees']['age_group'].value_counts()
            fig = create_bar_chart(
                pd.DataFrame({'age_group': age_group_counts.index, 'count': age_group_counts.values}),
                'age_group', 'count',
                'Age Group Distribution',
                color=COLORS['secondary']
            )
            st.plotly_chart(fig, use_container_width=True)
            
            dominant_age = age_group_counts.index[0]
            dominant_age_pct = (age_group_counts.values[0] / age_group_counts.sum() * 100)
            st.markdown(f"""
                <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                    <em>{dominant_age}</em> is the largest age group with <strong>{dominant_age_pct:.1f}%</strong> of workforce. 
                    {
                        "Strong mix of experience and fresh perspectives!" if "31-40" in dominant_age or "41-50" in dominant_age else
                        "Young, energetic workforce with growth potential!" if "25-30" in dominant_age else
                        "Experienced team - focus on knowledge transfer."
                    }</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Second row for more demographics
        col3, col4 = st.columns(2)
        
        with col3:
            # Marital Status distribution
            if 'marital_status' in filtered_data['employees'].columns:
                st.markdown("""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #10B981; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Donut Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Segments:</strong> Marital Status | <strong>Size:</strong> Employee Count</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Family status of workforce</p>
                    </div>
                """, unsafe_allow_html=True)
                
                marital_counts = filtered_data['employees']['marital_status'].value_counts()
                fig = create_donut_chart(
                    pd.DataFrame({'status': marital_counts.index, 'count': marital_counts.values}),
                    'count', 'status',
                    'Marital Status Distribution',
                    colors=COLORS['chart_colors']
                )
                st.plotly_chart(fig, use_container_width=True)
                
                married_pct = (marital_counts.get('Married', 0) / marital_counts.sum() * 100) if marital_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{married_pct:.1f}%</strong> of employees are married. 
                        {
                            "Consider family-friendly benefits and flexible work options." if married_pct > 50 else
                            "Mix of family structures - ensure diverse benefit options."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col4:
            # Education Level distribution
            if 'education_level_label' in filtered_data['employees'].columns:
                st.markdown("""
                    <div style='background: rgba(59, 130, 246, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #3B82F6; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Horizontal Bar Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Number of Employees | <strong>Y-Axis:</strong> Education Levels</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Educational qualifications of workforce</p>
                    </div>
                """, unsafe_allow_html=True)
                
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
                
                top_edu = edu_counts.index[0]
                top_edu_pct = (edu_counts.values[0] / edu_counts.sum() * 100)
                advanced_degrees = edu_counts.get("Master's Degree", 0) + edu_counts.get('Professional Degree', 0) + edu_counts.get('Doctorate (PhD)', 0)
                advanced_pct = (advanced_degrees / edu_counts.sum() * 100) if edu_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        Most employees have <em>{top_edu}</em>. <strong>{advanced_pct:.1f}%</strong> hold advanced degrees. 
                        {
                            "🎓 Highly educated workforce - leverage for innovation!" if advanced_pct > 30 else
                            "Consider upskilling programs for career development."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        # Third row
        col5, col6 = st.columns(2)
        
        with col5:
            # Employment Type
            if 'employment_type' in filtered_data['employees'].columns:
                st.markdown("""
                    <div style='background: rgba(245, 158, 11, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #F59E0B; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Pie Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Segments:</strong> Employment Types | <strong>Size:</strong> Employee Count</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Full-time vs Part-time vs Contract distribution</p>
                    </div>
                """, unsafe_allow_html=True)
                
                emp_type_counts = filtered_data['employees']['employment_type'].value_counts()
                fig = create_pie_chart(
                    pd.DataFrame({'type': emp_type_counts.index, 'count': emp_type_counts.values}),
                    'count', 'type',
                    'Employment Type Distribution',
                    colors=COLORS['chart_colors']
                )
                st.plotly_chart(fig, use_container_width=True)
                
                fulltime_pct = (emp_type_counts.get('Full-time', 0) / emp_type_counts.sum() * 100) if emp_type_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{fulltime_pct:.1f}%</strong> are full-time employees. 
                        {
                            "Strong core workforce with stable employment." if fulltime_pct > 80 else
                            "Flexible workforce mix - balance benefits and costs effectively."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col6:
            # Work Location
            if 'work_location' in filtered_data['employees'].columns:
                st.markdown("""
                    <div style='background: rgba(236, 72, 153, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #EC4899; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Vertical Bar Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Location Types | <strong>Y-Axis:</strong> Number of Employees</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Office vs Remote vs Hybrid work arrangements</p>
                    </div>
                """, unsafe_allow_html=True)
                
                location_counts = filtered_data['employees']['work_location'].value_counts()
                fig = create_bar_chart(
                    pd.DataFrame({'location': location_counts.index, 'count': location_counts.values}),
                    'location', 'count',
                    'Work Location Distribution',
                    color=COLORS['accent']
                )
                st.plotly_chart(fig, use_container_width=True)
                
                remote_pct = (location_counts.get('Remote', 0) / location_counts.sum() * 100) if location_counts.sum() > 0 else 0
                hybrid_pct = (location_counts.get('Hybrid', 0) / location_counts.sum() * 100) if location_counts.sum() > 0 else 0
                flexible_pct = remote_pct + hybrid_pct
                st.markdown(f"""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{flexible_pct:.1f}%</strong> work remotely or hybrid. 
                        {
                            "🏠 Modern, flexible work culture supporting work-life balance!" if flexible_pct > 50 else
                            "Traditional office setup - consider flexible options for retention."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #EF4444 0%, #F59E0B 100%); padding: 0.8rem 1.5rem; border-radius: 10px; margin-bottom: 1rem;'>
                <h3 style='margin: 0; color: white; font-size: 1.2rem;'>📉 Attrition Analytics</h3>
            </div>
        """, unsafe_allow_html=True)
        
        employees = filtered_data['employees']
        attrition = filtered_data['attrition']
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Attrition by department
            st.markdown("""
                <div style='background: rgba(239, 68, 68, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #EF4444; margin-bottom: 0.5rem;'>
                    <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Horizontal Bar Chart</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Number of Exits | <strong>Y-Axis:</strong> Department Names</p>
                    <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Which departments have highest employee turnover</p>
                </div>
            """, unsafe_allow_html=True)
            
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
            
            if not dept_attr.empty:
                top_attrition_dept = dept_attr.index[0]
                top_attr_count = dept_attr.values[0]
                st.markdown(f"""
                    <div style='background: rgba(239, 68, 68, 0.15); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem; border: 1px solid rgba(239, 68, 68, 0.3);'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>⚠️ Alert:</strong> 
                        <em>{top_attrition_dept}</em> has highest attrition with <strong>{top_attr_count}</strong> exits. 
                        Conduct department-specific analysis and implement targeted retention strategies immediately.</p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # Attrition by reason
            if 'attrition_reason' in attrition.columns and not attrition.empty:
                st.markdown("""
                    <div style='background: rgba(245, 158, 11, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #F59E0B; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Donut Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Segments:</strong> Reasons for Leaving | <strong>Size:</strong> Number of Employees</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Top reasons why employees are leaving the organization</p>
                    </div>
                """, unsafe_allow_html=True)
                
                reason_counts = attrition['attrition_reason'].value_counts().head(8)
                fig = create_donut_chart(
                    pd.DataFrame({'reason': reason_counts.index, 'count': reason_counts.values}),
                    'count', 'reason',
                    'Top Attrition Reasons',
                    colors=COLORS['chart_colors']
                )
                st.plotly_chart(fig, use_container_width=True)
                
                top_reason = reason_counts.index[0]
                top_reason_pct = (reason_counts.values[0] / reason_counts.sum() * 100)
                st.markdown(f"""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <em>"{top_reason}"</em> is the #1 reason (<strong>{top_reason_pct:.1f}%</strong> of exits). 
                        {
                            "Address compensation concerns through market benchmarking." if "compensation" in top_reason.lower() or "salary" in top_reason.lower() else
                            "Improve career development and advancement opportunities." if "career" in top_reason.lower() or "growth" in top_reason.lower() else
                            "Focus on management training and leadership development." if "management" in top_reason.lower() or "manager" in top_reason.lower() else
                            "Enhance work-life balance and flexible work policies." if "balance" in top_reason.lower() or "hours" in top_reason.lower() else
                            "Conduct deeper analysis to address this root cause."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        # Additional row for more insights
        col3, col4 = st.columns(2)
        
        with col3:
            # Exit interview scores
            if 'exit_interview_score_label' in attrition.columns and not attrition.empty:
                st.markdown("""
                    <div style='background: rgba(245, 158, 11, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #F59E0B; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Bar Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Satisfaction Levels | <strong>Y-Axis:</strong> Number of Exits</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> How satisfied departing employees were with their experience</p>
                    </div>
                """, unsafe_allow_html=True)
                
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
                
                dissatisfied_count = exit_scores.get('Dissatisfied', 0) + exit_scores.get('Very Dissatisfied', 0)
                dissatisfied_pct = (dissatisfied_count / exit_scores.sum() * 100) if exit_scores.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(239, 68, 68, 0.15); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem; border: 1px solid rgba(239, 68, 68, 0.3);'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>⚠️ Concern:</strong> 
                        <strong>{dissatisfied_pct:.1f}%</strong> of departing employees reported dissatisfaction. 
                        {
                            "This high dissatisfaction rate requires immediate attention to prevent further attrition." if dissatisfied_pct > 40 else
                            "Monitor exit interview feedback and implement improvements based on common themes." if dissatisfied_pct > 20 else
                            "Maintain current employee experience initiatives while addressing specific concerns."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col4:
            # Rehire eligibility
            if 'rehire_eligible' in attrition.columns and not attrition.empty:
                st.markdown("""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #10B981; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Pie Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Segments:</strong> Yes/No Eligibility | <strong>Size:</strong> Percentage of Exits</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Proportion of former employees eligible for rehire</p>
                    </div>
                """, unsafe_allow_html=True)
                
                rehire_counts = attrition['rehire_eligible'].value_counts()
                fig = create_pie_chart(
                    pd.DataFrame({'eligible': rehire_counts.index, 'count': rehire_counts.values}),
                    'count', 'eligible',
                    'Rehire Eligibility',
                    colors=[COLORS['success'], COLORS['danger']]
                )
                st.plotly_chart(fig, use_container_width=True)
                
                eligible_count = rehire_counts.get('Yes', 0)
                eligible_pct = (eligible_count / rehire_counts.sum() * 100) if rehire_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{eligible_pct:.1f}%</strong> of departing employees are eligible for rehire, indicating 
                        {
                            "excellent separation processes and positive employer reputation. Consider boomerang recruitment programs." if eligible_pct > 75 else
                            "good professional relationships. Maintain alumni network and consider rehire programs." if eligible_pct > 50 else
                            "need for improved exit processes and performance management. Review eligibility criteria."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%); padding: 0.8rem 1.5rem; border-radius: 10px; margin-bottom: 1rem;'>
                <h3 style='margin: 0; color: white; font-size: 1.2rem;'>💼 Performance & Engagement Analytics</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Performance rating distribution
            performance = filtered_data['performance']
            if not performance.empty and 'performance_rating_label' in performance.columns:
                st.markdown("""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #10B981; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Bar Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Performance Rating Categories | <strong>Y-Axis:</strong> Number of Employees</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Distribution of employee performance ratings from latest reviews</p>
                    </div>
                """, unsafe_allow_html=True)
                
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
                
                high_performers = perf_counts.get('Exceeds Expectations', 0) + perf_counts.get('Excellent', 0)
                high_perf_pct = (high_performers / perf_counts.sum() * 100) if perf_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{high_perf_pct:.1f}%</strong> of employees are high performers (Exceeds/Excellent). 
                        {
                            "Outstanding! Implement retention programs and succession planning for top talent." if high_perf_pct > 30 else
                            "Good performance levels. Focus on developing more high performers through mentorship." if high_perf_pct > 20 else
                            "Performance improvement needed. Invest in training, coaching, and development programs."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # Manager rating distribution
            if not performance.empty and 'manager_rating_label' in performance.columns:
                st.markdown("""
                    <div style='background: rgba(59, 130, 246, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #3B82F6; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Bar Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Manager Rating Categories | <strong>Y-Axis:</strong> Number of Managers</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> How managers are rated by their direct reports</p>
                    </div>
                """, unsafe_allow_html=True)
                
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
                
                excellent_managers = manager_counts.get('Excellent', 0) + manager_counts.get('Above Average', 0)
                excellent_pct = (excellent_managers / manager_counts.sum() * 100) if manager_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(59, 130, 246, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{excellent_pct:.1f}%</strong> of managers rated Above Average or Excellent. 
                        {
                            "Strong leadership! Leverage these managers as mentors and coaches for others." if excellent_pct > 60 else
                            "Good leadership quality. Implement manager development programs for continuous improvement." if excellent_pct > 40 else
                            "Leadership development critical. Invest in management training and 360-degree feedback."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        # Second row
        col3, col4 = st.columns(2)
        
        with col3:
            # Job Satisfaction distribution
            engagement = filtered_data['engagement']
            if not engagement.empty and 'job_satisfaction_label' in engagement.columns:
                st.markdown("""
                    <div style='background: rgba(139, 92, 246, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #8B5CF6; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Bar Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Satisfaction Levels | <strong>Y-Axis:</strong> Number of Employees</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> How satisfied employees are with their current role and workplace</p>
                    </div>
                """, unsafe_allow_html=True)
                
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
                
                high_satisfaction = satisfaction_counts.get('High', 0) + satisfaction_counts.get('Very High', 0)
                high_sat_pct = (high_satisfaction / satisfaction_counts.sum() * 100) if satisfaction_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(139, 92, 246, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{high_sat_pct:.1f}%</strong> report high job satisfaction. 
                        {
                            "Excellent! Continue current practices and share success stories." if high_sat_pct > 70 else
                            "Positive trend. Address specific pain points to boost satisfaction further." if high_sat_pct > 50 else
                            "Concerning levels. Conduct pulse surveys and implement immediate improvement actions."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col4:
            # Engagement Score distribution
            if not engagement.empty and 'engagement_score_label' in engagement.columns:
                st.markdown("""
                    <div style='background: rgba(236, 72, 153, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #EC4899; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Bar Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Engagement Levels | <strong>Y-Axis:</strong> Number of Employees</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Overall employee engagement and commitment to organization</p>
                    </div>
                """, unsafe_allow_html=True)
                
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
                
                high_engagement = engagement_counts.get('High', 0) + engagement_counts.get('Very High', 0)
                high_eng_pct = (high_engagement / engagement_counts.sum() * 100) if engagement_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(236, 72, 153, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{high_eng_pct:.1f}%</strong> highly engaged employees. 
                        {
                            "Outstanding engagement! Maintain momentum with recognition and growth opportunities." if high_eng_pct > 65 else
                            "Good foundation. Enhance career development and autonomy to increase engagement." if high_eng_pct > 45 else
                            "Engagement crisis. Immediate intervention needed - focus on communication, recognition, and purpose."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        # Third row
        col5, col6 = st.columns(2)
        
        with col5:
            # Goal Completion
            if not performance.empty and 'goal_completion_pct' in performance.columns:
                st.markdown("""
                    <div style='background: rgba(14, 165, 233, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #0EA5E9; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Bar Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>X-Axis:</strong> Completion Percentage Ranges | <strong>Y-Axis:</strong> Number of Employees</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Distribution of goal/objective completion rates across workforce</p>
                    </div>
                """, unsafe_allow_html=True)
                
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
                
                high_completion = goal_counts.get('76-100%', 0)
                high_comp_pct = (high_completion / goal_counts.sum() * 100) if goal_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(14, 165, 233, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{high_comp_pct:.1f}%</strong> of employees achieving 76-100% goal completion. 
                        {
                            "Excellent execution! Recognize top performers and share best practices." if high_comp_pct > 60 else
                            "Moderate achievement. Review goal-setting process and provide more support." if high_comp_pct > 35 else
                            "Low completion rates. Reassess goal difficulty, resources, and alignment with priorities."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col6:
            # Promotion recommendations
            if not performance.empty and 'promotion_recommendation' in performance.columns:
                st.markdown("""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border-left: 4px solid #10B981; margin-bottom: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>📊 Chart Type:</strong> Donut Chart</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Segments:</strong> Yes/No Recommendation | <strong>Size:</strong> Percentage of Employees</p>
                        <p style='margin: 0; font-size: 0.85rem; color: #475569;'><strong>Shows:</strong> Proportion of employees recommended for promotion by managers</p>
                    </div>
                """, unsafe_allow_html=True)
                
                promo_counts = performance['promotion_recommendation'].value_counts()
                fig = create_donut_chart(
                    pd.DataFrame({'recommended': promo_counts.index, 'count': promo_counts.values}),
                    'count', 'recommended',
                    'Promotion Recommendations',
                    colors=[COLORS['success'], COLORS['medium']]
                )
                st.plotly_chart(fig, use_container_width=True)
                
                recommended = promo_counts.get('Yes', 0)
                recommended_pct = (recommended / promo_counts.sum() * 100) if promo_counts.sum() > 0 else 0
                st.markdown(f"""
                    <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <p style='margin: 0; font-size: 0.85rem; color: #1e293b;'><strong>💡 Key Insight:</strong> 
                        <strong>{recommended_pct:.1f}%</strong> recommended for promotion. 
                        {
                            "High promotion pipeline! Ensure succession planning and development plans are in place." if recommended_pct > 25 else
                            "Healthy talent pipeline. Create clear promotion paths and development opportunities." if recommended_pct > 15 else
                            "Limited promotion pipeline. Invest in talent development and create advancement opportunities to retain top performers."
                        }</p>
                    </div>
                """, unsafe_allow_html=True)
    
    # ============================================================================
    # NEW TAB 5: INSIGHTS & RECOMMENDATIONS
    # ============================================================================
    with tab5:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #F59E0B 0%, #EC4899 100%); 
                        padding: 0.6rem 1.5rem; border-radius: 10px; margin-bottom: 0.6rem;
                        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);'>
                <h3 style='margin: 0; color: white; font-size: 1.2rem; font-weight: 700;'>📈 Insights & Recommendations</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Executive Summary Cards
        st.markdown("### 🎯 Executive Summary")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                <div style='background: linear-gradient(135deg, rgba(37, 99, 235, 0.1) 0%, rgba(37, 99, 235, 0.05) 100%); 
                            padding: 1rem; border-radius: 12px; border-left: 5px solid #2563EB; height: 100%;'>
                    <h4 style='color: #2563EB; margin: 0 0 0.5rem 0; font-size: 1.1rem;'>📊 Workforce Health</h4>
                    <p style='color: #475569; font-size: 0.9rem; margin: 0; line-height: 1.6;'>
                        Your organization has <strong>TOTAL_EMP</strong> employees with an average tenure of 
                        <strong>AVG_TENURE years</strong>. The workforce is STABILITY_STATUS.
                    </p>
                </div>
            """.replace("TOTAL_EMP", f"{kpis['total_employees']:,}")
               .replace("AVG_TENURE", f"{kpis['avg_tenure']:.1f}")
               .replace("STABILITY_STATUS", "relatively stable" if kpis['avg_tenure'] > 3 else "experiencing high turnover"), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div style='background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%); 
                            padding: 1rem; border-radius: 12px; border-left: 5px solid #EF4444; height: 100%;'>
                    <h4 style='color: #EF4444; margin: 0 0 0.5rem 0; font-size: 1.1rem;'>⚠️ Attrition Alert</h4>
                    <p style='color: #475569; font-size: 0.9rem; margin: 0; line-height: 1.6;'>
                        Current attrition rate is <strong>ATTR_RATE%</strong>. This is ATTR_STATUS. 
                        ATTR_ACTION
                    </p>
                </div>
            """.replace("ATTR_RATE", f"{kpis['attrition_rate']:.1f}")
               .replace("ATTR_STATUS", "within acceptable range" if kpis['attrition_rate'] < 20 else "ABOVE industry average")
               .replace("ATTR_ACTION", "Continue monitoring trends." if kpis['attrition_rate'] < 20 else "⚠️ Immediate retention strategies needed!"),
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
                <div style='background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%); 
                            padding: 1rem; border-radius: 12px; border-left: 5px solid #10B981; height: 100%;'>
                    <h4 style='color: #10B981; margin: 0 0 0.5rem 0; font-size: 1.1rem;'>😊 Employee Satisfaction</h4>
                    <p style='color: #475569; font-size: 0.9rem; margin: 0; line-height: 1.6;'>
                        Average engagement score is <strong>SAT_SCORE/5</strong>. Employees are SAT_STATUS. 
                        SAT_TREND
                    </p>
                </div>
            """.replace("SAT_SCORE", f"{kpis['avg_satisfaction']:.1f}")
               .replace("SAT_STATUS", "highly engaged" if kpis['avg_satisfaction'] >= 4 else ("moderately satisfied" if kpis['avg_satisfaction'] >= 3 else "showing low engagement"))
               .replace("SAT_TREND", "Great work! 🎉" if kpis['avg_satisfaction'] >= 4 else "Focus on improvement initiatives."),
            unsafe_allow_html=True)
        
        st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
        
        # Key Insights Section
        st.markdown("### 💡 Key Insights from Your Data")
        
        employees = filtered_data['employees']
        attrition = filtered_data['attrition']
        performance = filtered_data['performance']
        engagement = filtered_data['engagement']
        
        # Calculate insights
        dept_counts = employees['department_name'].value_counts()
        largest_dept = dept_counts.index[0]
        largest_dept_pct = (dept_counts.values[0] / dept_counts.sum() * 100)
        
        # Attrition by department
        attrition_dept = attrition.merge(employees[['employee_id', 'department_name']], on='employee_id', how='left')
        attrition_by_dept = attrition_dept['department_name'].value_counts()
        high_attrition_dept = attrition_by_dept.index[0] if not attrition_by_dept.empty else "N/A"
        
        # Job level insights
        job_level_counts = employees['job_level_label'].value_counts()
        dominant_level = job_level_counts.index[0]
        
        # Performance insights
        if not performance.empty and 'performance_rating' in performance.columns:
            high_performers = len(performance[performance['performance_rating'] >= 4])
            high_performer_pct = (high_performers / len(performance) * 100) if len(performance) > 0 else 0
        else:
            high_performer_pct = 0
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
                <div style='background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); margin-bottom: 1rem;'>
                    <h4 style='color: #2563EB; margin: 0 0 0.5rem 0;'>📊 1. Department Distribution</h4>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; line-height: 1.6;'>
                        • <strong>{largest_dept}</strong> is your largest department with <strong>{dept_counts.values[0]:,}</strong> employees 
                        ({largest_dept_pct:.1f}% of top departments)<br>
                        • This concentration suggests {
                            "a healthy balance across departments" if largest_dept_pct < 30 else 
                            "⚠️ potential over-reliance on one department"
                        }<br>
                        • Consider workforce planning to ensure business continuity
                    </p>
                </div>
                
                <div style='background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); margin-bottom: 1rem;'>
                    <h4 style='color: #8B5CF6; margin: 0 0 0.5rem 0;'>👥 2. Organizational Structure</h4>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; line-height: 1.6;'>
                        • Majority of employees are at <strong>{dominant_level}</strong> level<br>
                        • {
                            "✅ Healthy pyramid structure supports growth and succession planning" if dominant_level in ["Entry Level", "Mid Level"] else
                            "⚠️ Top-heavy structure may limit advancement opportunities"
                        }<br>
                        • {"Strong foundation for future leadership development" if dominant_level == "Entry Level" else "Consider creating more senior roles for career progression"}
                    </p>
                </div>
                
                <div style='background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.07);'>
                    <h4 style='color: #10B981; margin: 0 0 0.5rem 0;'>⏱️ 3. Tenure & Retention</h4>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; line-height: 1.6;'>
                        • Average tenure is <strong>{kpis['avg_tenure']:.1f} years</strong><br>
                        • {
                            "✅ Strong retention indicates positive work environment" if kpis['avg_tenure'] > 5 else
                            "⚠️ Lower tenure suggests need for retention strategies" if kpis['avg_tenure'] > 2 else
                            "🔴 High turnover requires immediate attention"
                        }<br>
                        • Retention rate is <strong>{kpis['retention_rate']:.1f}%</strong> - {
                            "excellent performance!" if kpis['retention_rate'] > 85 else
                            "room for improvement" if kpis['retention_rate'] > 75 else
                            "needs urgent action"
                        }
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div style='background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); margin-bottom: 1rem;'>
                    <h4 style='color: #EF4444; margin: 0 0 0.5rem 0;'>📉 4. Attrition Analysis</h4>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; line-height: 1.6;'>
                        • <strong>{high_attrition_dept}</strong> has highest attrition<br>
                        • Current attrition rate: <strong>{kpis['attrition_rate']:.1f}%</strong> vs industry benchmark of 20-25%<br>
                        • {
                            "🟢 Below industry average - excellent retention!" if kpis['attrition_rate'] < 15 else
                            "🟡 Within normal range but monitor closely" if kpis['attrition_rate'] < 25 else
                            "🔴 Above acceptable levels - urgent intervention needed"
                        }<br>
                        • Focus retention efforts on {high_attrition_dept} department
                    </p>
                </div>
                
                <div style='background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); margin-bottom: 1rem;'>
                    <h4 style='color: #F59E0B; margin: 0 0 0.5rem 0;'>⭐ 5. Performance Metrics</h4>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; line-height: 1.6;'>
                        • <strong>{high_performer_pct:.1f}%</strong> of employees are high performers (rating 4-5)<br>
                        • {
                            "✅ Strong performance culture in place!" if high_performer_pct > 60 else
                            "Moderate performance - opportunities for coaching" if high_performer_pct > 40 else
                            "⚠️ Performance improvement initiatives needed"
                        }<br>
                        • {"Recognize and retain top talent to maintain momentum" if high_performer_pct > 50 else "Invest in training and development programs"}
                    </p>
                </div>
                
                <div style='background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.07);'>
                    <h4 style='color: #06B6D4; margin: 0 0 0.5rem 0;'>😊 6. Employee Engagement</h4>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; line-height: 1.6;'>
                        • Overall satisfaction: <strong>{kpis['avg_satisfaction']:.1f}/5.0</strong><br>
                        • {
                            "🌟 Excellent! Employees are highly engaged" if kpis['avg_satisfaction'] >= 4.0 else
                            "👍 Good engagement but room for improvement" if kpis['avg_satisfaction'] >= 3.5 else
                            "⚠️ Low engagement - immediate action required" if kpis['avg_satisfaction'] >= 2.5 else
                            "🔴 Critical: Major engagement issues to address"
                        }<br>
                        • {"Continue with current engagement strategies" if kpis['avg_satisfaction'] >= 4.0 else "Conduct surveys to identify improvement areas"}
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
        # Actionable Recommendations
        st.markdown("### 🎯 Actionable Recommendations")
        
        st.markdown("""
            <div style='background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 100%); padding: 1.5rem; border-radius: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.1); margin-bottom: 1.5rem;'>
                <h4 style='color: white; margin: 0 0 1rem 0; font-size: 1.2rem;'>🚀 Priority Actions (Next 30 Days)</h4>
        """, unsafe_allow_html=True)
        
        recommendations = []
        
        # Generate dynamic recommendations based on data
        if kpis['attrition_rate'] > 20:
            recommendations.append({
                'priority': '🔴 CRITICAL',
                'title': 'Reduce Attrition Rate',
                'actions': [
                    f"Focus on {high_attrition_dept} department - conduct exit interviews to identify root causes",
                    "Implement stay interviews with high-value employees to understand retention factors",
                    "Review compensation and benefits packages against market rates",
                    "Launch immediate employee engagement initiatives"
                ]
            })
        
        if kpis['avg_satisfaction'] < 3.5:
            recommendations.append({
                'priority': '🟡 HIGH',
                'title': 'Improve Employee Engagement',
                'actions': [
                    "Conduct comprehensive engagement surveys to identify pain points",
                    "Create employee feedback forums and act on suggestions",
                    "Enhance work-life balance initiatives (flexible working, wellness programs)",
                    "Improve internal communication and transparency from leadership"
                ]
            })
        
        if high_performer_pct < 50:
            recommendations.append({
                'priority': '🟡 HIGH',
                'title': 'Boost Performance Levels',
                'actions': [
                    "Implement structured coaching and mentoring programs",
                    "Provide targeted training for skill development",
                    "Set clear performance expectations and regular feedback cycles",
                    "Create performance improvement plans for underperformers"
                ]
            })
        
        if kpis['avg_tenure'] < 3:
            recommendations.append({
                'priority': '🟠 MEDIUM',
                'title': 'Strengthen Retention Strategies',
                'actions': [
                    "Develop clear career progression paths and communicate them",
                    "Launch employee recognition and rewards programs",
                    "Create internal mobility opportunities before external hiring",
                    "Conduct 6-month and 1-year check-ins with new hires"
                ]
            })
        
        recommendations.append({
            'priority': '🟢 ONGOING',
            'title': 'Succession Planning',
            'actions': [
                "Identify critical roles and develop backup talent pipelines",
                "Create leadership development programs for high-potential employees",
                "Document key processes and knowledge transfer plans",
                f"Focus on {dominant_level} level employees for upskilling opportunities"
            ]
        })
        
        recommendations.append({
            'priority': '🟢 ONGOING',
            'title': 'Data-Driven Decision Making',
            'actions': [
                "Schedule monthly workforce analytics reviews with leadership",
                "Set up automated alerts for attrition rate thresholds",
                "Track leading indicators (engagement, satisfaction) to predict attrition",
                "Benchmark against industry standards quarterly"
            ]
        })
        
        # Display recommendations
        for i, rec in enumerate(recommendations, 1):
            st.markdown(f"""
                <div style='background: white; padding: 1rem 1.5rem; border-radius: 10px; margin-bottom: 1rem; border-left: 5px solid {"#EF4444" if "CRITICAL" in rec["priority"] else "#F59E0B" if "HIGH" in rec["priority"] else "#3B82F6" if "MEDIUM" in rec["priority"] else "#10B981"};'>
                    <h5 style='color: #1e293b; margin: 0 0 0.5rem 0;'>{rec['priority']} | {i}. {rec['title']}</h5>
                    <ul style='color: #475569; font-size: 0.9rem; margin: 0; padding-left: 1.5rem; line-height: 1.8;'>
            """, unsafe_allow_html=True)
            
            for action in rec['actions']:
                st.markdown(f"<li>{action}</li>", unsafe_allow_html=True)
            
            st.markdown("</ul></div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # ROI Calculator Section
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        st.markdown("### 💰 Estimated Impact of Improvements")
        
        col1, col2, col3 = st.columns(3)
        
        avg_salary = 75000  # Assume average salary
        replacement_cost = avg_salary * 1.5  # 150% of salary
        potential_attrition = int(kpis['total_employees'] * (kpis['attrition_rate'] / 100))
        current_cost = potential_attrition * replacement_cost
        
        with col1:
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, rgba(239, 68, 68, 0.15) 0%, rgba(239, 68, 68, 0.05) 100%); 
                            padding: 1.5rem; border-radius: 12px; text-align: center; border: 2px solid rgba(239, 68, 68, 0.3);'>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; font-weight: 600;'>Current Attrition Cost</p>
                    <h3 style='color: #EF4444; margin: 0; font-size: 2rem;'>${current_cost:,.0f}</h3>
                    <p style='color: #64748B; font-size: 0.8rem; margin: 0.5rem 0 0 0;'>Based on {potential_attrition} potential exits</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            reduced_attrition = max(15, kpis['attrition_rate'] - 5)  # Target 5% reduction
            new_potential_attrition = int(kpis['total_employees'] * (reduced_attrition / 100))
            improved_cost = new_potential_attrition * replacement_cost
            
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(245, 158, 11, 0.05) 100%); 
                            padding: 1.5rem; border-radius: 12px; text-align: center; border: 2px solid rgba(245, 158, 11, 0.3);'>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; font-weight: 600;'>If Reduced to {reduced_attrition:.1f}%</p>
                    <h3 style='color: #F59E0B; margin: 0; font-size: 2rem;'>${improved_cost:,.0f}</h3>
                    <p style='color: #64748B; font-size: 0.8rem; margin: 0.5rem 0 0 0;'>With {new_potential_attrition} exits</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            savings = current_cost - improved_cost
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(16, 185, 129, 0.05) 100%); 
                            padding: 1.5rem; border-radius: 12px; text-align: center; border: 2px solid rgba(16, 185, 129, 0.3);'>
                    <p style='color: #64748B; font-size: 0.9rem; margin: 0 0 0.5rem 0; font-weight: 600;'>💰 Potential Savings</p>
                    <h3 style='color: #10B981; margin: 0; font-size: 2rem;'>${savings:,.0f}</h3>
                    <p style='color: #64748B; font-size: 0.8rem; margin: 0.5rem 0 0 0;'>Annual cost reduction</p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background: rgba(59, 130, 246, 0.1); padding: 1rem; border-radius: 10px; margin-top: 1rem; border-left: 4px solid #3B82F6;'>
                <p style='color: #475569; font-size: 0.85rem; margin: 0; line-height: 1.6;'>
                    <strong>📊 Methodology:</strong> Calculations assume average salary of $75,000 and replacement cost of 150% of annual salary 
                    (including recruitment, training, and productivity loss). Actual costs may vary based on role and industry.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Footer with gradient
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 100%); padding: 2rem; border-radius: 12px; text-align: center; margin-top: 2rem;'>
            <h3 style='color: white; margin: 0 0 0.5rem 0; font-size: 1.3rem;'>Workforce Planning Dashboard</h3>
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
