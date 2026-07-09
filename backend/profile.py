from backend.database import get_connection


def get_user_profile(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            full_name,
            email,
            created_at
        FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()

    conn.close()

    if user:
        return dict(user)

    return None