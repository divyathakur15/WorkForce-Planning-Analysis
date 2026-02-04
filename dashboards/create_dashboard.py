"""
Static Dashboard Generator for Workforce Planning Analysis
Generates professional HTML dashboards with KPIs and visualizations
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dashboard_config import COLORS, FONTS
from kpi_card import create_kpi_card, create_kpi_row
from chart_components import (
    create_bar_chart, create_pie_chart, create_donut_chart,
    create_line_chart, create_heatmap, create_gauge_chart,
    create_grouped_bar_chart, create_stacked_bar_chart
)


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
    
    return data


def calculate_kpis(data):
    """Calculate key performance indicators"""
    
    employees = data['employees']
    attrition = data['attrition']
    engagement = data['engagement']
    performance = data['performance']
    
    # Total employees
    total_employees = len(employees)
    
    # Active employees
    active_employees = len(employees[employees['status'] == 'Active']) if 'status' in employees.columns else total_employees
    
    # Attrition rate
    attrition_count = len(attrition)
    attrition_rate = (attrition_count / total_employees) * 100
    
    # Retention rate
    retention_rate = 100 - attrition_rate
    
    # Average tenure (from employees)
    avg_tenure = employees['tenure_years'].mean()
    
    # Average satisfaction (from engagement)
    if 'overall_satisfaction' in engagement.columns and not engagement.empty:
        avg_satisfaction = engagement['overall_satisfaction'].mean()
    else:
        avg_satisfaction = 3.5  # Default
    
    # High risk employees (low satisfaction and performance)
    if not engagement.empty and not performance.empty:
        recent_engagement = engagement.sort_values('survey_date').groupby('employee_id').last()
        recent_performance = performance.sort_values('review_date').groupby('employee_id').last()
        
        high_risk = 0
        for emp_id in employees[employees['status'] == 'Active']['employee_id'].values:
            if emp_id in recent_engagement.index and emp_id in recent_performance.index:
                if 'overall_satisfaction' in recent_engagement.columns and 'overall_rating' in recent_performance.columns:
                    satisfaction = recent_engagement.loc[emp_id, 'overall_satisfaction']
                    perf_rating = recent_performance.loc[emp_id, 'overall_rating']
                    if satisfaction < 3 and perf_rating < 3:
                        high_risk += 1
    else:
        high_risk = 0
    
    kpis = {
        'total_employees': total_employees,
        'active_employees': active_employees,
        'attrition_rate': attrition_rate,
        'retention_rate': retention_rate,
        'avg_tenure': avg_tenure,
        'avg_satisfaction': avg_satisfaction,
        'high_risk': high_risk
    }
    
    return kpis


def create_executive_dashboard(data, kpis):
    """Create executive summary dashboard"""
    
    employees = data['employees']
    departments = data['departments']
    attrition = data['attrition']
    
    # Merge employees with departments
    emp_dept = employees.merge(departments, on='department_id', how='left')
    
    # Create figure with subplots
    fig = make_subplots(
        rows=3, cols=3,
        subplot_titles=(
            'Key Performance Indicators', 'Attrition by Department', 'Employees by Job Level',
            'Attrition Rate Gauge', 'Headcount by Department', 'Tenure Distribution',
            'Age Distribution', 'Gender Distribution', 'Performance Summary'
        ),
        specs=[
            [{'type': 'table', 'colspan': 3}, None, None],
            [{'type': 'indicator'}, {'type': 'bar'}, {'type': 'pie'}],
            [{'type': 'bar'}, {'type': 'histogram'}, {'type': 'pie'}]
        ],
        row_heights=[0.2, 0.4, 0.4],
        vertical_spacing=0.12
    )
    
    # Row 1: KPI Table
    kpi_table = go.Table(
        header=dict(
            values=['Metric', 'Value'],
            fill_color=COLORS['primary'],
            font=dict(color='white', size=14),
            align='left'
        ),
        cells=dict(
            values=[
                ['Total Employees', 'Active Employees', 'Attrition Rate', 'Retention Rate', 
                 'Avg Tenure', 'Avg Satisfaction', 'High Risk Employees'],
                [f"{kpis['total_employees']:,}", f"{kpis['active_employees']:,}", 
                 f"{kpis['attrition_rate']:.1f}%", f"{kpis['retention_rate']:.1f}%",
                 f"{kpis['avg_tenure']:.1f} years", f"{kpis['avg_satisfaction']:.1f}/5",
                 f"{kpis['high_risk']:,}"]
            ],
            fill_color='white',
            font=dict(size=12),
            align='left',
            height=30
        )
    )
    fig.add_trace(kpi_table, row=1, col=1)
    
    # Row 2, Col 1: Attrition Rate Gauge
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=kpis['attrition_rate'],
        title={'text': "Attrition Rate (%)", 'font': {'size': 16}},
        gauge={
            'axis': {'range': [0, 50]},
            'bar': {'color': COLORS['danger']},
            'steps': [
                {'range': [0, 15], 'color': 'rgba(16, 185, 129, 0.2)'},
                {'range': [15, 25], 'color': 'rgba(245, 158, 11, 0.2)'},
                {'range': [25, 50], 'color': 'rgba(239, 68, 68, 0.2)'}
            ]
        }
    ), row=2, col=1)
    
    # Row 2, Col 2: Headcount by Department
    dept_counts = emp_dept['department_name'].value_counts().head(10)
    fig.add_trace(go.Bar(
        x=dept_counts.values,
        y=dept_counts.index,
        orientation='h',
        marker=dict(color=COLORS['primary']),
        text=dept_counts.values,
        textposition='auto'
    ), row=2, col=2)
    
    # Row 2, Col 3: Employees by Job Level
    job_level_counts = employees['job_level'].value_counts()
    fig.add_trace(go.Pie(
        labels=job_level_counts.index,
        values=job_level_counts.values,
        hole=0.4,
        marker=dict(colors=COLORS['chart_colors'])
    ), row=2, col=3)
    
    # Row 3, Col 1: Attrition by Department
    attrition_dept = attrition.merge(employees[['employee_id', 'department_id']], on='employee_id')
    attrition_dept = attrition_dept.merge(departments, on='department_id')
    dept_attr_counts = attrition_dept['department_name'].value_counts().head(10)
    
    fig.add_trace(go.Bar(
        x=dept_attr_counts.index,
        y=dept_attr_counts.values,
        marker=dict(color=COLORS['danger']),
        text=dept_attr_counts.values,
        textposition='auto'
    ), row=3, col=1)
    
    # Row 3, Col 2: Tenure Distribution
    fig.add_trace(go.Histogram(
        x=employees['tenure_years'],
        nbinsx=20,
        marker=dict(color=COLORS['info']),
        name='Tenure'
    ), row=3, col=2)
    
    # Row 3, Col 3: Gender Distribution
    gender_counts = employees['gender'].value_counts()
    fig.add_trace(go.Pie(
        labels=gender_counts.index,
        values=gender_counts.values,
        marker=dict(colors=[COLORS['primary'], COLORS['secondary']])
    ), row=3, col=3)
    
    # Update layout
    fig.update_layout(
        height=1200,
        title_text="<b>Executive Workforce Dashboard</b>",
        title_font=dict(size=28, color=COLORS['dark']),
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family=FONTS['body']['family'])
    )
    
    return fig


def generate_dashboards():
    """Generate all dashboards and save to HTML"""
    
    print("Loading data...")
    data = load_data()
    
    print("Calculating KPIs...")
    kpis = calculate_kpis(data)
    
    print("\nKey Performance Indicators:")
    print(f"  Total Employees: {kpis['total_employees']:,}")
    print(f"  Active Employees: {kpis['active_employees']:,}")
    print(f"  Attrition Rate: {kpis['attrition_rate']:.1f}%")
    print(f"  Retention Rate: {kpis['retention_rate']:.1f}%")
    print(f"  Average Tenure: {kpis['avg_tenure']:.1f} years")
    print(f"  Average Satisfaction: {kpis['avg_satisfaction']:.1f}/5")
    print(f"  High Risk Employees: {kpis['high_risk']:,}")
    
    print("\nGenerating Executive Dashboard...")
    exec_dashboard = create_executive_dashboard(data, kpis)
    
    # Save dashboards
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    exec_path = os.path.join(output_dir, 'executive_dashboard.html')
    exec_dashboard.write_html(exec_path)
    print(f"✓ Executive Dashboard saved to: {exec_path}")
    
    print("\n" + "="*60)
    print("Dashboard generation complete!")
    print("="*60)
    print(f"\nOpen the following file in your browser:")
    print(f"  {exec_path}")


if __name__ == "__main__":
    generate_dashboards()
