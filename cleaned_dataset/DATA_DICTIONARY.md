# Data Dictionary - Cleaned Workforce Planning Dataset

## 📘 Overview

This data dictionary provides comprehensive information about all tables, columns, data types, valid values, and business rules for the cleaned workforce planning dataset.

---

## 🗂️ Table of Contents

1. [employees_master_cleaned.csv](#1-employees_master_cleanedcsv)
2. [department_master_cleaned.csv](#2-department_master_cleanedcsv)
3. [job_history_cleaned.csv](#3-job_history_cleanedcsv)
4. [compensation_history_cleaned.csv](#4-compensation_history_cleanedcsv)
5. [attendance_records_cleaned.csv](#5-attendance_records_cleanedcsv)
6. [performance_reviews_cleaned.csv](#6-performance_reviews_cleanedcsv)
7. [engagement_surveys_cleaned.csv](#7-engagement_surveys_cleanedcsv)
8. [training_and_skills_cleaned.csv](#8-training_and_skills_cleanedcsv)
9. [attrition_events_cleaned.csv](#9-attrition_events_cleanedcsv)

---

## 1. employees_master_cleaned.csv

**Purpose**: Core employee demographic and employment information  
**Grain**: 1 row = 1 employee  
**Primary Key**: `employee_id`  
**Total Records**: 5,000

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| employee_id | Integer | Unique employee identifier | 1 to N | No | Primary Key |
| employee_code | String | Human-readable employee code | EMP##### | No | Format: EMP00001 |
| age | Integer | Employee age in years | 18-70 | No | Validated range |
| gender | String | Employee gender | Male, Female | No | Title-cased |
| marital_status | String | Marital status | Single, Married, Divorced | No | Title-cased |
| education_level | Integer | Education level (numeric) | 1-5 | No | 1=Below College, 5=Doctorate |
| education_field | String | Field of study | Various | No | e.g., HR, Life Sciences, Engineering |
| hire_date | DateTime | Date employee joined | YYYY-MM-DD HH:MM:SS | No | Standardized format |
| employment_type | String | Employment contract type | Full-time, Contract | No | - |
| business_travel | String | Travel frequency | Travel_Rarely, Travel_Frequently, Non-Travel | No | - |
| distance_from_home_km | Float | Commute distance in km | 0+ | No | Positive values |
| work_location | String | Primary work location | Office, Remote, Hybrid | No | - |
| department_id | Integer | Department reference | 1-20 | No | Foreign Key → department_master |
| job_role | String | Current job title | Various | No | e.g., Software Engineer, Manager |
| job_level | Integer | Job seniority level | 1-5 | No | 1=Entry, 5=Executive |
| manager_id | Integer | Reporting manager ID | 0 or valid employee_id | No | 0 = No manager (CEO/Top level) |
| status | String | Employment status | Active, Attrited | No | Synchronized with attrition_events |
| tenure_years | Float | Years at company | 0+ | No | **Derived**: Calculated from hire_date |
| tenure_category | String | Tenure bucket | 0-2 years, 2-5 years, 5-10 years, 10+ years | No | **Derived**: Categorized tenure |
| age_group | String | Age range bucket | 18-25, 26-35, 36-45, 46-55, 56+ | No | **Derived**: Categorized age |

### Business Rules
- Attrited employees must have matching record in attrition_events
- Active employees must NOT have record in attrition_events
- manager_id must exist as employee_id (self-referential) or be 0
- department_id must exist in department_master

---

## 2. department_master_cleaned.csv

**Purpose**: Department organizational structure  
**Grain**: 1 row = 1 department  
**Primary Key**: `department_id`  
**Total Records**: 20

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| department_id | Integer | Unique department identifier | 1-20 | No | Primary Key |
| department_name | String | Department name | Various meaningful names | No | Cleaned from generic names |
| business_unit | String | Business division | Technology, Corporate, Operations | Yes | - |
| region | String | Geographical region | APAC, EMEA, Americas | Yes | - |
| cost_center | String | Financial cost center | CC### | No | Format: CC001 |

### Department Names (Post-Cleaning)
1. Human Resources
2. Engineering
3. Sales
4. Marketing
5. Finance
6. Operations
7. Information Technology
8. Research & Development
9. Customer Service
10. Product Management
11. Legal
12. Supply Chain
13. Quality Assurance
14. Business Development
15. Analytics
16. Procurement
17. Corporate Strategy
18. Facilities
19. Training & Development
20. Security

---

## 3. job_history_cleaned.csv

**Purpose**: Employee role changes, promotions, transfers  
**Grain**: 1 row = 1 job assignment period  
**Primary Key**: `job_history_id`  
**Total Records**: 14,949

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| job_history_id | Integer | Unique job record ID | 1 to N | No | Primary Key |
| employee_id | Integer | Employee reference | Valid employee_id | No | Foreign Key → employees_master |
| department_id | Integer | Department during period | Valid department_id | No | Foreign Key → department_master |
| job_role | String | Role title | Various | No | - |
| job_level | Integer | Seniority level | 1-5 | No | - |
| start_date | DateTime | Job period start | YYYY-MM-DD HH:MM:SS | No | - |
| end_date | DateTime | Job period end | YYYY-MM-DD HH:MM:SS | Yes | NULL = Current role |
| promotion_flag | Boolean | Promotion indicator | True, False | No | - |
| job_change_reason | String | Reason for change | Promotion, Transfer, Role Change | No | - |

### Business Rules
- end_date must be >= start_date (when not NULL)
- Employee can have multiple records (job history timeline)
- Most recent record (end_date = NULL) should match current role in employees_master

---

## 4. compensation_history_cleaned.csv

**Purpose**: Salary changes and compensation events  
**Grain**: 1 row = 1 salary update  
**Primary Key**: `compensation_id`  
**Total Records**: 19,980

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| compensation_id | Integer | Unique compensation record | 1 to N | No | Primary Key |
| employee_id | Integer | Employee reference | Valid employee_id | No | Foreign Key → employees_master |
| effective_date | DateTime | Salary effective date | YYYY-MM-DD HH:MM:SS | No | - |
| monthly_income | Float | Monthly salary amount | > 0 | No | Positive values only |
| salary_band | String | Salary tier | Low, Medium, High | No | - |
| percent_hike | Float | Salary increase % | -20 to 100 | No | Can be negative (rare cases) |
| bonus_amount | Float | Annual bonus | >= 0 | No | Non-negative |
| stock_option_level | Integer | Stock benefit tier | 0-4 | No | 0=None, 4=Highest |

### Business Rules
- Employee can have multiple records (salary history timeline)
- Most recent effective_date represents current compensation

---

## 5. attendance_records_cleaned.csv

**Purpose**: Monthly attendance and work pattern tracking  
**Grain**: 1 row = 1 employee per month  
**Primary Key**: `attendance_id`  
**Total Records**: 299,880

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| attendance_id | Integer | Unique attendance record | 1 to N | No | Primary Key |
| employee_id | Integer | Employee reference | Valid employee_id | No | Foreign Key → employees_master |
| month | DateTime | Record month | YYYY-MM-DD | No | Standardized to first of month |
| days_present | Integer | Total days worked | 0-31 | No | - |
| days_absent | Integer | Total absences | 0-31 | No | - |
| overtime_hours | Float | Extra hours worked | >= 0 | No | - |
| work_from_home_days | Integer | Remote work days | 0-31 | No | - |
| leave_type | String | Leave category | Sick, Casual, Paid, None | No | - |

### Business Rules
- days_present + days_absent <= 31
- Multiple records per employee (monthly series)

---

## 6. performance_reviews_cleaned.csv

**Purpose**: Employee performance evaluations  
**Grain**: 1 row = 1 performance review  
**Primary Key**: `review_id`  
**Total Records**: 14,982

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| review_id | Integer | Unique review ID | 1 to N | No | Primary Key |
| employee_id | Integer | Employee reference | Valid employee_id | No | Foreign Key → employees_master |
| review_date | DateTime | Evaluation date | YYYY-MM-DD HH:MM:SS | No | - |
| performance_rating | Integer | Employee performance score | 1-5 | No | 1=Poor, 5=Excellent |
| manager_rating | Integer | Manager's rating | 1-5 | No | 1=Poor, 5=Excellent |
| goal_completion_pct | Float | Goals achieved % | 0-100 | No | - |
| promotion_recommendation | Boolean | Promotion recommended | True, False | No | - |

### Business Rules
- Employees typically have annual/semi-annual reviews
- Multiple records per employee (review timeline)

---

## 7. engagement_surveys_cleaned.csv

**Purpose**: Employee satisfaction and engagement feedback  
**Grain**: 1 row = 1 survey response  
**Primary Key**: `survey_id`  
**Total Records**: 9,987

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| survey_id | Integer | Unique survey ID | 1 to N | No | Primary Key |
| employee_id | Integer | Employee reference | Valid employee_id | No | Foreign Key → employees_master |
| survey_date | DateTime | Survey submission date | YYYY-MM-DD HH:MM:SS | No | - |
| job_satisfaction | Integer | Job satisfaction score | 1-5 | No | 1=Very Dissatisfied, 5=Very Satisfied |
| work_life_balance | Integer | Work-life balance rating | 1-5 | No | 1=Poor, 5=Excellent |
| manager_relationship | Integer | Manager relationship rating | 1-5 | No | 1=Poor, 5=Excellent |
| career_growth | Integer | Career growth rating | 1-5 | No | 1=Poor, 5=Excellent |
| engagement_score | Float | Average engagement score | 1-5 | No | **Calculated**: Average of 4 metrics |

### Business Rules
- engagement_score = AVERAGE(job_satisfaction, work_life_balance, manager_relationship, career_growth)
- Multiple surveys per employee (periodic surveys)

---

## 8. training_and_skills_cleaned.csv

**Purpose**: Employee skills and training records  
**Grain**: 1 row = 1 skill per employee  
**Primary Key**: `skill_id`  
**Total Records**: 19,988

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| skill_id | Integer | Unique skill record | 1 to N | No | Primary Key |
| employee_id | Integer | Employee reference | Valid employee_id | No | Foreign Key → employees_master |
| skill_name | String | Name of skill | Various | No | e.g., Python, Leadership, SQL |
| skill_category | String | Skill type | Technical, Soft | No | - |
| proficiency_level | Integer | Skill mastery level | 1-5 | No | 1=Beginner, 5=Expert |
| training_completed | Boolean | Training completion status | True, False | No | - |
| certification_flag | Boolean | Certification obtained | True, False | No | - |

### Business Rules
- Employees can have multiple skills (many-to-many relationship)

---

## 9. attrition_events_cleaned.csv

**Purpose**: Employee exit records and attrition tracking  
**Grain**: 1 row = 1 attrition event  
**Primary Key**: `attrition_id`  
**Total Records**: 1,200

### Columns

| Column Name | Data Type | Description | Valid Values | Nullable | Notes |
|------------|-----------|-------------|--------------|----------|-------|
| attrition_id | Integer | Unique attrition record | 1 to N | No | Primary Key |
| employee_id | Integer | Employee reference | Valid employee_id | No | Foreign Key → employees_master |
| attrition_flag | Boolean | Attrition indicator | True | No | Always True in this table |
| attrition_date | DateTime | Exit date | YYYY-MM-DD HH:MM:SS | No | Must be >= hire_date |
| attrition_reason | String | Reason for leaving | Various | No | See Attrition Reasons below |
| exit_interview_score | Integer | Exit feedback rating | 1-5 | No | 1=Very Negative, 5=Very Positive |
| rehire_eligible | Boolean | Rehire eligibility | True, False | No | - |

### Attrition Reasons
- Career Opportunity
- Compensation
- Work-Life Balance
- Management Issues
- Relocation
- Personal Reasons
- Retirement
- Performance Issues
- Company Culture

### Business Rules
- One record per attrited employee (no duplicates)
- attrition_date must be after employee's hire_date
- Employee must have status='Attrited' in employees_master

---

## 🔗 Table Relationships

```
employees_master (1) ←→ (Many) job_history
employees_master (1) ←→ (Many) compensation_history
employees_master (1) ←→ (Many) attendance_records
employees_master (1) ←→ (Many) performance_reviews
employees_master (1) ←→ (Many) engagement_surveys
employees_master (1) ←→ (Many) training_and_skills
employees_master (1) ←→ (0..1) attrition_events

department_master (1) ←→ (Many) employees_master
department_master (1) ←→ (Many) job_history
```

---

## 📊 Data Quality Standards

All cleaned data adheres to:
- ✅ No duplicate primary keys
- ✅ All foreign keys validated
- ✅ All dates in standard format
- ✅ All numeric values within valid ranges
- ✅ All boolean values standardized (True/False)
- ✅ All categorical values standardized
- ✅ Cross-table consistency enforced

---

## 📝 Notes

1. **Date Format**: All dates standardized to `YYYY-MM-DD HH:MM:SS`
2. **Boolean Format**: All flags as Python boolean (True/False), not strings
3. **Missing Values**: Intentional nulls only in specific fields (end_date, manager_id=0)
4. **Currency**: All monetary values assumed in local currency units
5. **Analysis Cutoff Date**: 2024-12-31 (for tenure calculations)

---

**Version**: 1.0  
**Last Updated**: 2026-01-31  
**Status**: Production-Ready
