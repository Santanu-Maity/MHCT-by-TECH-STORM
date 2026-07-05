def calculate_scores(data):
    """
    Calculate Mental Score, Anxiety Score and Depression Score
    """

    mental_score = 50

    # Positive Factors
    mental_score += data["sleep_hours"] * 2
    mental_score += data["sleep_quality"] * 3
    mental_score += data["food_quality"] * 2
    mental_score += data["water_intake"]
    mental_score += data["exercise_hours"] * 4
    mental_score += data["social_interaction"] * 3
    mental_score += data["family_support"] * 4
    mental_score += data["daily_productivity"] * 2
    mental_score += data["hobbies_time"] * 3

    # Negative Factors
    mental_score -= data["work_stress"] * 3
    mental_score -= data["academic_pressure"] * 2
    mental_score -= data["financial_stress"] * 3
    mental_score -= data["screen_time"]

    if data["health_issues"] == 1:
        mental_score -= 10

    mental_score = max(0, min(100, mental_score))

    anxiety_score = (
        data["work_stress"] * 5 +
        data["academic_pressure"] * 4 +
        data["financial_stress"] * 4 +
        data["screen_time"] * 2 +
        (6 - data["sleep_quality"]) * 4 +
        (4 - data["exercise_hours"]) * 3
    )

    anxiety_score = max(0, min(100, anxiety_score))

    depression_score = (
        (10 - data["sleep_hours"]) * 4 +
        (5 - data["social_interaction"]) * 5 +
        (5 - data["family_support"]) * 5 +
        (10 - data["daily_productivity"]) * 3 +
        (4 - data["hobbies_time"]) * 4 +
        (4 - data["exercise_hours"]) * 3 +
        data["health_issues"] * 15
    )

    depression_score = max(0, min(100, depression_score))

    return {
        "mental_score": mental_score,
        "anxiety_score": anxiety_score,
        "depression_score": depression_score
    }