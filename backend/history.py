from database import get_connection


def get_assessment_history(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            mental_state,
            mental_score,
            anxiety_score,
            depression_score,
            risk_level,
            recommendation,
            created_at
        FROM assessments
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]