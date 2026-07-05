from flask import Flask, request, jsonify
from flask_cors import CORS

from predictor import predict_mental_state
from utils import calculate_scores
from recommendation import get_recommendation

app = Flask(__name__)
CORS(app)

# ==========================
# Home Route
# ==========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "Mental Health Counseling Tool Backend is Running"
    })


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
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)