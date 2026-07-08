from database import get_connection


def get_trend(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT mental_score
        FROM assessments
        WHERE user_id=?
        ORDER BY created_at DESC
        LIMIT 2
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    if len(rows) < 2:
        return {
            "trend": "Not enough data",
            "change": 0
        }

    latest = rows[0]["mental_score"]
    previous = rows[1]["mental_score"]

    difference = latest - previous

    if difference >= 10:
        trend = "Improving 📈"

    elif difference <= -10:
        trend = "Needs Attention 📉"

    else:
        trend = "Stable ➖"

    return {
        "trend": trend,
        "change": difference
    }