# Employee Attrition & Retention Strategy – Dataset Description

## Overview
This project dataset is designed for **end-to-end HR Analytics, Workforce Planning, and Employee Attrition Prediction**.  
The dataset is structured in a **relational format** with multiple CSV files to simulate a real-world enterprise HR database.

The data supports:
- Data Analytics
- Data Visualization (Power BI / Excel)
- SQL Joins & Querying
- Machine Learning & Prediction
- Workforce Planning
- Employee Retention Analysis

---

# Dataset Structure

The dataset consists of the following CSV files:

1. employees_master.csv  
2. department_master.csv  
3. job_history.csv  
4. compensation_history.csv  
5. attendance_records.csv  
6. performance_reviews.csv  
7. engagement_surveys.csv  
8. training_and_skills.csv  
9. attrition_events.csv  

Each file represents a specific business domain within Human Resources.

---

## 1. employees_master.csv
**Description:**  
Contains the primary information of all employees. This acts as the **main dimension table** for analysis.

**Grain:** 1 row = 1 employee

### Columns
| Column | Description |
|--------|-------------|
employee_id | Unique identifier for each employee |
employee_code | Human-readable employee code |
age | Age of employee |
gender | Gender of employee |
marital_status | Single / Married / Divorced |
education_level | Numeric education level (1–5) |
education_field | Field of education |
hire_date | Date employee joined company |
employment_type | Full-time or Contract |
business_travel | Travel frequency requirement |
distance_from_home_km | Commute distance in kilometers |
work_location | Office / Hybrid / Remote |
department_id | Reference to department_master |
job_role | Employee job title |
job_level | Job seniority level (1–5) |
manager_id | Reporting manager employee ID |
status | Active or Attrited |

---

## 2. department_master.csv
**Description:**  
Contains information about company departments and business units.

**Grain:** 1 row = 1 department

### Columns
| Column | Description |
|--------|-------------|
department_id | Unique department ID |
department_name | Name of department |
business_unit | Business division |
region | Geographical region |
cost_center | Financial cost center code |

---

## 3. job_history.csv
**Description:**  
Tracks employee role changes, promotions, and department transfers over time.

**Grain:** 1 row = 1 job assignment period

### Columns
| Column | Description |
|--------|-------------|
job_history_id | Unique job record ID |
employee_id | Employee reference |
department_id | Department during job period |
job_role | Role title |
job_level | Seniority level |
start_date | Job start date |
end_date | Job end date |
promotion_flag | Indicates if promotion occurred |
job_change_reason | Promotion / Transfer / Role Change |

---

## 4. compensation_history.csv
**Description:**  
Stores employee salary revisions and compensation growth.

**Grain:** 1 row = 1 salary update

### Columns
| Column | Description |
|--------|-------------|
compensation_id | Unique compensation record |
employee_id | Employee reference |
effective_date | Date salary becomes active |
monthly_income | Monthly salary |
salary_band | Low / Medium / High |
percent_hike | Percentage salary increase |
bonus_amount | Annual bonus amount |
stock_option_level | Stock benefit tier |

---

## 5. attendance_records.csv
**Description:**  
Contains monthly attendance, absenteeism, and overtime records.

**Grain:** 1 row = 1 employee per month

### Columns
| Column | Description |
|--------|-------------|
attendance_id | Unique attendance record |
employee_id | Employee reference |
month | Month of record |
days_present | Total days worked |
days_absent | Total absences |
overtime_hours | Extra hours worked |
work_from_home_days | Remote working days |
leave_type | Sick / Casual / Paid / None |

---

## 6. performance_reviews.csv
**Description:**  
Captures employee performance evaluations and promotion recommendations.

**Grain:** 1 row = 1 performance review

### Columns
| Column | Description |
|--------|-------------|
review_id | Unique review ID |
employee_id | Employee reference |
review_date | Date of evaluation |
performance_rating | Employee performance score (1–5) |
manager_rating | Manager's rating (1–5) |
goal_completion_pct | Percentage of goals achieved |
promotion_recommendation | True / False flag |

---

## 7. engagement_surveys.csv
**Description:**  
Employee satisfaction and engagement feedback surveys.

**Grain:** 1 row = 1 survey response

### Columns
| Column | Description |
|--------|-------------|
survey_id | Unique survey ID |
employee_id | Employee reference |
survey_date | Survey submission date |
job_satisfaction | Satisfaction score (1–5) |
work_life_balance | Work-life balance rating |
manager_relationship | Relationship rating |
career_growth | Career growth rating |
engagement_score | Average engagement score |

---

## 8. training_and_skills.csv
**Description:**  
Stores employee skills, certifications, and training completion details.

**Grain:** 1 row = 1 skill per employee

### Columns
| Column | Description |
|--------|-------------|
skill_id | Unique skill record |
employee_id | Employee reference |
skill_name | Name of skill |
skill_category | Technical / Soft |
proficiency_level | Skill level (1–5) |
training_completed | Training completion status |
certification_flag | Certification status |

---

## 9. attrition_events.csv
**Description:**  
Records employees who left the organization and exit information.

**Grain:** 1 row = 1 attrition event

### Columns
| Column | Description |
|--------|-------------|
attrition_id | Unique attrition record |
employee_id | Employee reference |
attrition_flag | Indicates attrition |
attrition_date | Date employee exited |
attrition_reason | Reason for leaving |
exit_interview_score | Exit feedback rating |
rehire_eligible | Rehire eligibility status |

---

# Data Relationships
- `employee_id` is the primary key across all employee-related tables.
- `department_id` links employees and job history to departments.
- Designed for **SQL Joins, Star Schema Modeling, and BI Dashboards**.

---

# Usage Scenarios
- Employee Attrition Prediction
- Workforce Planning
- Salary Growth Analysis
- Employee Engagement Analysis
- Attendance & Burnout Detection
- Skill Gap Identification
- Performance Trend Analysis

---

# Tools Supported
- **Python** – Data Cleaning, EDA, Machine Learning
- **SQL** – Queries, Joins, Aggregations
- **Excel** – Pivot Tables, KPI Sheets
- **Power BI** – Dashboards, DAX Measures

---

This dataset simulates a **real enterprise HR analytics environment** and is suitable for portfolio projects, hackathons, and professional data analytics demonstrations.
