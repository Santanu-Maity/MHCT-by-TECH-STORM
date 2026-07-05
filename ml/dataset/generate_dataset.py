import os
import pandas as pd
import numpy as np

# Generate same random values every time
np.random.seed(42)

# Number of users
n_samples = 3000

# Store all records here
data = []

# ============================================
# Generate one user at a time
# ============================================
for i in range(n_samples):

    # ----------------------------
    # Basic Information
    # ----------------------------
    age = np.random.randint(18, 61)

    gender = np.random.choice([
        "Male",
        "Female",
        "Other"
    ])

    employment_status = np.random.choice([
        "Student",
        "Employed",
        "Self-Employed",
        "Unemployed"
    ])

    relationship_status = np.random.choice([
        "Single",
        "Married",
        "In a Relationship"
    ])

    # ----------------------------
    # Lifestyle Features
    # ----------------------------
    sleep_hours = np.random.randint(3, 11)

    sleep_quality = np.random.randint(1, 6)

    food_quality = np.random.randint(1, 6)

    water_intake = np.random.randint(1, 6)

    exercise_hours = np.random.randint(0, 5)

    screen_time = np.random.randint(2, 16)

    hobbies_time = np.random.randint(0, 5)

    # ----------------------------
    # Mental Health Factors
    # ----------------------------
    work_stress = np.random.randint(1, 11)

    academic_pressure = np.random.randint(1, 11)

    financial_stress = np.random.randint(1, 6)

    social_interaction = np.random.randint(1, 6)

    family_support = np.random.randint(1, 6)

    daily_productivity = np.random.randint(1, 11)

    health_issues = np.random.choice(
        [0, 1],
        p=[0.8, 0.2]
    )

    # ----------------------------
    # Mental Wellness Score
    # ----------------------------
    mental_score = 50

    # Positive factors
    mental_score += sleep_hours * 2
    mental_score += sleep_quality * 3
    mental_score += food_quality * 2
    mental_score += water_intake
    mental_score += exercise_hours * 4
    mental_score += social_interaction * 3
    mental_score += family_support * 4
    mental_score += daily_productivity * 2
    mental_score += hobbies_time * 3

    # Negative factors
    mental_score -= work_stress * 3
    mental_score -= academic_pressure * 2
    mental_score -= financial_stress * 3
    mental_score -= screen_time

    if health_issues == 1:
        mental_score -= 10

    # Keep between 0 and 100
    mental_score = max(0, min(100, mental_score))

    # ----------------------------
    # Anxiety Score
    # ----------------------------
    anxiety_score = (
        work_stress * 5 +
        academic_pressure * 4 +
        financial_stress * 4 +
        screen_time * 2 +
        (6 - sleep_quality) * 4 +
        (4 - exercise_hours) * 3
    )

    anxiety_score = max(0, min(100, anxiety_score))

    # ----------------------------
    # Depression Score
    # ----------------------------
    depression_score = (
        (10 - sleep_hours) * 4 +
        (5 - social_interaction) * 5 +
        (5 - family_support) * 5 +
        (10 - daily_productivity) * 3 +
        (4 - hobbies_time) * 4 +
        (4 - exercise_hours) * 3 +
        health_issues * 15
    )

    depression_score = max(0, min(100, depression_score))

    # ----------------------------
    # Mental State
    # ----------------------------
    # ----------------------------

    if mental_score >= 85 and anxiety_score <= 25 and depression_score <= 25:
        mental_state = "Excellent"

    elif mental_score >= 70 and anxiety_score <= 40 and depression_score <= 40:
        mental_state = "Good"

    elif mental_score >= 50:
        mental_state = "Moderate Stress"

    elif mental_score >= 30:
        mental_state = "High Stress"

    else:
        mental_state = "Severe Risk"

    # ----------------------------
    # Save Record
    # ----------------------------
    data.append({
        "age": age,
        "gender": gender,
        "employment_status": employment_status,
        "relationship_status": relationship_status,

        "sleep_hours": sleep_hours,
        "sleep_quality": sleep_quality,
        "food_quality": food_quality,
        "water_intake": water_intake,
        "exercise_hours": exercise_hours,
        "screen_time": screen_time,
        "hobbies_time": hobbies_time,

        "work_stress": work_stress,
        "academic_pressure": academic_pressure,
        "financial_stress": financial_stress,
        "social_interaction": social_interaction,
        "family_support": family_support,
        "daily_productivity": daily_productivity,
        "health_issues": health_issues,

        "mental_score": mental_score,
        "anxiety_score": anxiety_score,
        "depression_score": depression_score,
        "mental_state": mental_state
    })

# ============================================
# OUTSIDE THE LOOP
# ============================================

# Create DataFrame
df = pd.DataFrame(data)

# Create output directory if it doesn't exist
os.makedirs("ml/dataset", exist_ok=True)

# Save dataset
df.to_csv("ml/dataset/dataset.csv", index=False)

# Print Information
print("=" * 50)
print("Dataset generated successfully!")
print(f"Total Records : {len(df)}")
print("Saved as : ml/dataset/dataset.csv")
print("=" * 50)

print("\nFirst 5 Records:\n")
print(df.head())