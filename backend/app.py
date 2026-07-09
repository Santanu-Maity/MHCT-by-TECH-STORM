from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    session,
    redirect,
    send_file
)

from backend.pdf_report import generate_pdf
from flask_cors import CORS


from backend.chatbot import chatbot_response
from backend.trend import get_trend
from backend.predictor import predict_mental_state
from backend.utils import calculate_scores
from backend.recommendation import get_recommendation
from backend.auth import auth
from backend.dashboard import get_dashboard_stats
from backend.chart import get_chart_data
from backend.assessment_db import save_assessment
from backend.history import get_assessment_history
from backend.profile import get_user_profile

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

CORS(app)

app.secret_key = "mindcare_ai_secret_key_2026"

app.register_blueprint(auth)


# ==========================
# Home Route
# ==========================
@app.route("/", methods=["GET"])
def home():
    return render_template("landing.html")


# ==========================
# Signup Page
# ==========================
@app.route("/signup")
def signup_page():
    return render_template("signup.html")


# ==========================
# Login Page
# ==========================
@app.route("/login")
def login_page():
    return render_template("login.html")


# ==========================
# Dashboard Page
# ==========================
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("dashboard.html")

# ==========================
# Assessment Page
# ==========================
@app.route("/assessment")
def assessment():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("assessment.html")


# ==========================
# Profile Page
# ==========================
@app.route("/profile")
def profile_page():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("profile.html")

# ==========================
# Chatbot Page
# ==========================
@app.route("/chatbot")
def chatbot():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("chatbot.html")


# ==========================
# History Page
# ==========================
@app.route("/history-page")
def history_page():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("history.html")


# ==========================
# Assessment History API
# ==========================
@app.route("/history")
def history():

    # Logged-in user
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "status": "error",
            "message": "Please login first."
        }), 401

    history = get_assessment_history(user_id)

    return jsonify({
        "status": "success",
        "history": history
    })


@app.route("/profile-data")
def profile_data():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "status": "error",
            "message": "Please login first."
        }), 401

    user = get_user_profile(user_id)

    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found."
        }), 404

    return jsonify({
        "status": "success",
        "user": user
    })


# ==========================
# Dashboard API
# ==========================
@app.route("/dashboard-data")
def dashboard_data():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "status": "error",
            "message": "Please login first."
        }), 401

    stats = get_dashboard_stats(user_id)

    return jsonify({
        "status": "success",
        "dashboard": stats
    })


# ==========================
# Dashboard Chart API
# ==========================
@app.route("/chart-data")
def chart_data():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "status": "error",
            "message": "Please login first."
        }), 401

    chart = get_chart_data(user_id)

    return jsonify({
        "status": "success",
        "chart": chart
    })


# ==========================
# Trend API
# ==========================
@app.route("/trend-data")
def trend_data():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "status": "error",
            "message": "Please login first."
        }), 401

    trend = get_trend(user_id)

    return jsonify({
        "status": "success",
        "trend": trend
    })

# ==========================
# Chatbot API
# ==========================
@app.route("/chat", methods=["POST"])
def chat():

    if "user_id" not in session:
        return jsonify({
            "status": "error",
            "message": "Please login first."
        }), 401

    data = request.get_json()

    message = data.get("message", "")

    reply = chatbot_response(message)

    return jsonify({
        "status": "success",
        "reply": reply
    })


# ==========================
# Download PDF Report
# ==========================
@app.route("/download-report")
def download_report():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "status": "error",
            "message": "Please login first."
        }), 401

    pdf = generate_pdf(user_id)

    return send_file(
        pdf,
        as_attachment=True,
        download_name="MindCare_AI_Report.pdf",
        mimetype="application/pdf"
    )


# ==========================
# Health Route
# ==========================
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "Mental Health Counseling Tool API",
        "model_loaded": True
    })


# ==========================
# Prediction Route
# ==========================
@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "No JSON data received."
            }), 400

        # Required Fields
        required_fields = [
            "age",
            "gender",
            "employment_status",
            "relationship_status",
            "sleep_hours",
            "sleep_quality",
            "food_quality",
            "water_intake",
            "exercise_hours",
            "screen_time",
            "hobbies_time",
            "work_stress",
            "academic_pressure",
            "financial_stress",
            "social_interaction",
            "family_support",
            "daily_productivity",
            "health_issues"
        ]

        # Validate Required Fields
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status": "error",
                    "message": f"Missing field: {field}"
                }), 400

        # Validate Numeric Ranges
        validations = {
            "sleep_hours": (0, 24),
            "sleep_quality": (1, 5),
            "food_quality": (1, 5),
            "water_intake": (1, 5),
            "exercise_hours": (0, 24),
            "screen_time": (0, 24),
            "hobbies_time": (0, 24),
            "work_stress": (1, 10),
            "academic_pressure": (1, 10),
            "financial_stress": (1, 5),
            "social_interaction": (1, 5),
            "family_support": (1, 5),
            "daily_productivity": (1, 10),
            "health_issues": (0, 1)
        }

        for field, (minimum, maximum) in validations.items():

            value = data[field]

            if not isinstance(value, (int, float)):
                return jsonify({
                    "status": "error",
                    "message": f"{field} must be a number."
                }), 400

            if value < minimum or value > maximum:
                return jsonify({
                    "status": "error",
                    "message": f"{field} must be between {minimum} and {maximum}."
                }), 400

        # Calculate Scores
        scores = calculate_scores(data)

        # Add Scores for Prediction
        data["mental_score"] = scores["mental_score"]
        data["anxiety_score"] = scores["anxiety_score"]
        data["depression_score"] = scores["depression_score"]

        # Predict
        prediction = predict_mental_state(data)

        # Recommendation
        recommendation = get_recommendation(prediction)

        # ====================================
        # SAVE ASSESSMENT
        # ====================================

        # Logged-in user
        user_id = session.get("user_id")

        if not user_id:
            return jsonify({
                "status": "error",
                "message": "Please login first."
            }), 401

        save_assessment(
            user_id=user_id,
            mental_state=prediction,
            mental_score=scores["mental_score"],
            anxiety_score=scores["anxiety_score"],
            depression_score=scores["depression_score"],
            risk_level=recommendation["risk_level"],
            recommendation=recommendation["advice"]
        )

        return jsonify({
            "status": "success",
            "mental_state": prediction,
            "mental_score": scores["mental_score"],
            "anxiety_score": scores["anxiety_score"],
            "depression_score": scores["depression_score"],
            "risk_level": recommendation["risk_level"],
            "recommendation": recommendation["advice"]
        })

    except Exception as e:
        import traceback

        print("\n========== ERROR IN /predict ==========")
        traceback.print_exc()
        print("=======================================\n")

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

print("\n========== REGISTERED ROUTES ==========")
for rule in app.url_map.iter_rules():
    print(rule)
print("=======================================\n")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)