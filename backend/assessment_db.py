from database import get_connection


def save_assessment(
    user_id,
    mental_state,
    mental_score,
    anxiety_score,
    depression_score,
    risk_level,
    recommendation
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO assessments(
            user_id,
            mental_state,
            mental_score,
            anxiety_score,
            depression_score,
            risk_level,
            recommendation
        )
        VALUES(?,?,?,?,?,?,?)
    """, (
        user_id,
        mental_state,
        mental_score,
        anxiety_score,
        depression_score,
        risk_level,
        recommendation
    ))

    conn.commit()
    conn.close()