from flask import Blueprint, request, jsonify, session
import bcrypt

from backend.database import get_connection

auth = Blueprint("auth", __name__)


# ====================================
# SIGN UP
# ====================================

@auth.route("/signup", methods=["POST"])
def signup():

    data = request.get_json()

    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")

    if not full_name or not email or not password:
        return jsonify({
            "status": "error",
            "message": "All fields are required."
        }), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE email=?",
        (email,)
    )

    existing = cursor.fetchone()

    if existing:
        conn.close()
        return jsonify({
            "status": "error",
            "message": "Email already registered."
        }), 400

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        INSERT INTO users(full_name,email,password)
        VALUES(?,?,?)
        """,
        (
            full_name,
            email,
            hashed_password.decode()
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "message": "Account created successfully."
    })


# ====================================
# LOGIN
# ====================================

@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "status": "error",
            "message": "Email and password are required."
        }), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        return jsonify({
            "status": "error",
            "message": "Invalid email or password."
        }), 401

    if bcrypt.checkpw(
        password.encode(),
        user["password"].encode()
    ):

        # ==========================
        # Create Login Session
        # ==========================
        session["user_id"] = user["id"]
        session["full_name"] = user["full_name"]
        session["email"] = user["email"]

        return jsonify({
            "status": "success",
            "message": "Login successful.",
            "user": {
                "id": user["id"],
                "full_name": user["full_name"],
                "email": user["email"]
            }
        })

    return jsonify({
        "status": "error",
        "message": "Invalid email or password."
    }), 401
    # ====================================
# LOGOUT
# ====================================

@auth.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({
        "status": "success",
        "message": "Logged out successfully."
    })