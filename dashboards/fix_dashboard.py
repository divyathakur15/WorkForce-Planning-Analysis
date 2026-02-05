"""
Script to fix the streamlit_app.py dashboard file
Removes duplicate code and tab references, converts to single-page layout
"""

import re

# Read the backup file
with open('streamlit_app_backup.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position where main visualizations start
sections_start = content.find("# ====================================================================================")
if sections_start == -1:
    sections_start = content.find("# Main visualizations")

# Keep everything before the main visualizations
header_content = content[:sections_start]

# Single-page layout to append
single_page_layout = '''    # ====================================================================================
    # SINGLE-PAGE LAYOUT WITH ALL CHARTS
    # ====================================================================================
    
    st.markdown("<div style='margin: 0.5rem 0;'></div>", unsafe_allow_html=True)
    
    # SECTION 1: OVERVIEW ANALYTICS
    st.markdown("""
        <div style='background: linear-gradient(135deg, #2563EB 0%, #8B5CF6 100%); 
                    padding: 0.6rem 1.5rem; border-radius: 10px; margin: 0.5rem 0;
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
    
    # SECTION 2: DEMOGRAPHIC ANALYTICS
    st.markdown("""
        <div style='background: linear-gradient(135deg, #10B981 0%, #06B6D4 100%); 
                    padding: 0.6rem 1.5rem; border-radius: 10px; margin: 0.8rem 0 0.5rem 0;
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
    
    # SECTION 3: ATTRITION ANALYTICS
    st.markdown("""
        <div style='background: linear-gradient(135deg, #EF4444 0%, #F59E0B 100%); 
                    padding: 0.6rem 1.5rem; border-radius: 10px; margin: 0.8rem 0 0.5rem 0;
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
    
    # SECTION 4: PERFORMANCE & ENGAGEMENT ANALYTICS
    st.markdown("""
        <div style='background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%); 
                    padding: 0.6rem 1.5rem; border-radius: 10px; margin: 0.8rem 0 0.5rem 0;
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
                    padding: 1.5rem; border-radius: 12px; text-align: center; margin-top: 1rem;'>
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
'''

# Write the combined content
with open('streamlit_app.py', 'w', encoding='utf-8') as f:
    f.write(header_content + single_page_layout)

print("✅ Dashboard file successfully fixed!")
print("✅ Converted from tabs to single-page layout")
print("✅ All charts now visible on one scrollable page")
print("✅ Spacing tightened and graphics added")
