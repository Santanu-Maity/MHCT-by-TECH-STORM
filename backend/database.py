import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_DIR = os.path.join(BASE_DIR, "database")
os.makedirs(DATABASE_DIR, exist_ok=True)

DB_PATH = os.path.join(DATABASE_DIR, "database.db")

print("BASE_DIR:", BASE_DIR)
print("DATABASE_DIR:", DATABASE_DIR)
print("DB_PATH:", DB_PATH)
print("DATABASE_DIR exists:", os.path.exists(DATABASE_DIR))


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # USERS TABLE
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ==========================
    # ASSESSMENTS TABLE
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        mental_state TEXT NOT NULL,

        mental_score REAL NOT NULL,

        anxiety_score REAL NOT NULL,

        depression_score REAL NOT NULL,

        risk_level TEXT NOT NULL,

        recommendation TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
    print("✅ Database Initialized Successfully")