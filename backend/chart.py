from database import get_connection


def get_chart_data(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            created_at,
            mental_score
        FROM assessments
        WHERE user_id=?
        ORDER BY created_at
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    labels = []
    scores = []

    for row in rows:
        labels.append(row["created_at"])
        scores.append(row["mental_score"])

    return {
        "labels": labels,
        "scores": scores
    }