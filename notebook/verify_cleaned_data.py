"""
Data Validation & Verification Script
Purpose: Verify cleaned data quality and generate final statistics
"""

import pandas as pd
import numpy as np

print("="*80)
print("DATA VALIDATION & VERIFICATION REPORT")
print("="*80)

import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLEANED_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), "cleaned_dataset") + os.sep

# Load all cleaned data
print("\n[1] Loading cleaned datasets...")
employees = pd.read_csv(f"{CLEANED_PATH}employees_master_cleaned.csv")
departments = pd.read_csv(f"{CLEANED_PATH}department_master_cleaned.csv")
attrition = pd.read_csv(f"{CLEANED_PATH}attrition_events_cleaned.csv")
job_history = pd.read_csv(f"{CLEANED_PATH}job_history_cleaned.csv")
compensation = pd.read_csv(f"{CLEANED_PATH}compensation_history_cleaned.csv")
attendance = pd.read_csv(f"{CLEANED_PATH}attendance_records_cleaned.csv")
performance = pd.read_csv(f"{CLEANED_PATH}performance_reviews_cleaned.csv")
engagement = pd.read_csv(f"{CLEANED_PATH}engagement_surveys_cleaned.csv")
training = pd.read_csv(f"{CLEANED_PATH}training_and_skills_cleaned.csv")

print("✓ All datasets loaded successfully")

# Verification Tests
print("\n" + "="*80)
print("[2] RUNNING VERIFICATION TESTS")
print("="*80)

tests_passed = 0
tests_total = 0

def test(name, condition):
    global tests_passed, tests_total
    tests_total += 1
    if condition:
        print(f"✓ PASS: {name}")
        tests_passed += 1
    else:
        print(f"✗ FAIL: {name}")
    return condition

# Test 1: Check for duplicates
print("\n--- Duplicate Checks ---")
test("Employees: No duplicate IDs", employees['employee_id'].is_unique)
test("Departments: No duplicate IDs", departments['department_id'].is_unique)
test("Attrition: No duplicate employee_ids", attrition['employee_id'].is_unique)

# Test 2: Referential integrity
print("\n--- Referential Integrity ---")
test("All employee department_ids exist in departments", 
     employees['department_id'].isin(departments['department_id']).all())
test("All attrition employee_ids exist in employees", 
     attrition['employee_id'].isin(employees['employee_id']).all())
test("All job_history employee_ids exist in employees", 
     job_history['employee_id'].isin(employees['employee_id']).all())
test("All compensation employee_ids exist in employees", 
     compensation['employee_id'].isin(employees['employee_id']).all())

# Test 3: Data ranges
print("\n--- Data Range Validation ---")
test("Employee ages between 18-70", 
     (employees['age'] >= 18).all() and (employees['age'] <= 70).all())
test("Job levels between 1-5", 
     (employees['job_level'] >= 1).all() and (employees['job_level'] <= 5).all())
test("Performance ratings between 1-5", 
     (performance['performance_rating'] >= 1).all() and (performance['performance_rating'] <= 5).all())
test("Engagement scores between 1-5", 
     (engagement['engagement_score'] >= 1).all() and (engagement['engagement_score'] <= 5).all())

# Test 4: Department names are meaningful
print("\n--- Department Name Validation ---")
generic_names = departments['department_name'].str.contains('Department_', na=False).any()
test("No generic department names (Department_X)", not generic_names)

# Test 5: Status consistency
print("\n--- Status Consistency ---")
attrited_in_master = set(employees[employees['status'] == 'Attrited']['employee_id'])
attrited_in_events = set(attrition['employee_id'])
test("Attrition status matches between tables", attrited_in_master == attrited_in_events)

# Test 6: Boolean standardization
print("\n--- Boolean Standardization ---")
test("Attrition flags are boolean type", 
     attrition['attrition_flag'].dtype == bool or attrition['attrition_flag'].isin([True, False]).all())
test("Rehire eligible are boolean type", 
     attrition['rehire_eligible'].dtype == bool or attrition['rehire_eligible'].isin([True, False]).all())

# Test 7: No missing critical values
print("\n--- Missing Values Check ---")
test("No missing employee_ids", employees['employee_id'].notna().all())
test("No missing hire_dates", employees['hire_date'].notna().all())
test("No missing attrition_dates", attrition['attrition_date'].notna().all())

# Print Summary Statistics
print("\n" + "="*80)
print("[3] SUMMARY STATISTICS")
print("="*80)

print(f"\n📊 Dataset Sizes:")
print(f"   Total Employees: {len(employees):,}")
print(f"   Active Employees: {(employees['status'] == 'Active').sum():,}")
print(f"   Attrited Employees: {(employees['status'] == 'Attrited').sum():,}")
print(f"   Departments: {len(departments):,}")
print(f"   Job History Records: {len(job_history):,}")
print(f"   Compensation Records: {len(compensation):,}")
print(f"   Attendance Records: {len(attendance):,}")
print(f"   Performance Reviews: {len(performance):,}")
print(f"   Engagement Surveys: {len(engagement):,}")
print(f"   Training Records: {len(training):,}")
print(f"   Attrition Events: {len(attrition):,}")

print(f"\n📈 Key Metrics:")
print(f"   Attrition Rate: {(len(attrition) / len(employees) * 100):.2f}%")
print(f"   Average Age: {employees['age'].mean():.1f} years")
print(f"   Average Tenure: {employees['tenure_years'].mean():.2f} years")
print(f"   Gender Distribution: {employees['gender'].value_counts().to_dict()}")

print(f"\n🏢 Top 5 Departments by Size:")
dept_size = employees.merge(departments, on='department_id')['department_name'].value_counts().head()
for dept, count in dept_size.items():
    print(f"   {dept}: {count:,} employees")

print(f"\n📉 Top 5 Attrition Reasons:")
attrition_reasons = attrition['attrition_reason'].value_counts().head()
for reason, count in attrition_reasons.items():
    print(f"   {reason}: {count:,} cases")

print(f"\n⭐ Average Performance Rating: {performance['performance_rating'].mean():.2f}/5")
print(f"⭐ Average Engagement Score: {engagement['engagement_score'].mean():.2f}/5")
print(f"⭐ Average Job Satisfaction: {engagement['job_satisfaction'].mean():.2f}/5")

# Test Results Summary
print("\n" + "="*80)
print("[4] TEST RESULTS SUMMARY")
print("="*80)
print(f"\nTests Passed: {tests_passed}/{tests_total}")
print(f"Success Rate: {(tests_passed/tests_total*100):.1f}%")

if tests_passed == tests_total:
    print("\n🎉 ALL TESTS PASSED - DATASET IS PRODUCTION READY! 🎉")
else:
    print(f"\n⚠️  {tests_total - tests_passed} test(s) failed. Review issues above.")

print("\n" + "="*80)
print("VERIFICATION COMPLETE")
print("="*80)
