from database import get_connection


def get_dashboard_stats(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    # Total Assessments
    cursor.execute("""
        SELECT COUNT(*)
        FROM assessments
        WHERE user_id=?
    """, (user_id,))

    total = cursor.fetchone()[0]

    # Latest Assessment
    cursor.execute("""
        SELECT
            mental_state,
            risk_level,
            created_at
        FROM assessments
        WHERE user_id=?
        ORDER BY created_at DESC
        LIMIT 1
    """, (user_id,))

    latest = cursor.fetchone()

    # Highest Risk
    cursor.execute("""
        SELECT risk_level
        FROM assessments
        WHERE user_id=?
        ORDER BY
        CASE risk_level
            WHEN 'High' THEN 3
            WHEN 'Medium' THEN 2
            ELSE 1
        END DESC
        LIMIT 1
    """, (user_id,))

    highest = cursor.fetchone()

    conn.close()

    return {
        "total_assessments": total,
        "latest_state": latest["mental_state"] if latest else "-",
        "latest_date": latest["created_at"] if latest else "-",
        "highest_risk": highest["risk_level"] if highest else "-"
    }