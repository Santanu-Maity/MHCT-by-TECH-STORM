# MHCT-by-TECH-STORM
# 🧠 Mental Health Counseling Tool (MHCT)

A Machine Learning-based Mental Health Counseling Tool that predicts a user's mental health status based on lifestyle, personal, and psychological factors. The system provides a mental health assessment along with a risk level and personalized recommendations through a Flask REST API.

---

# 📌 Project Overview

Mental health has become an important concern for students and working professionals. This project uses Machine Learning to analyze various lifestyle and mental health indicators and predicts the user's mental health condition.

The backend is developed using Flask, while the Machine Learning model is trained using Scikit-learn. The frontend (developed separately) communicates with the backend through REST APIs.

---

# 🎯 Objectives

* Predict an individual's mental health status.
* Estimate Mental Score, Anxiety Score, and Depression Score.
* Provide personalized recommendations based on prediction.
* Demonstrate the integration of Machine Learning with a web application.

---

# ✨ Features

* Machine Learning-based prediction.
* RESTful API using Flask.
* Random Forest Classifier.
* Synthetic dataset generation (3000 records).
* Input validation.
* Mental Score calculation.
* Anxiety Score calculation.
* Depression Score calculation.
* Personalized recommendations.
* Health check endpoint.
* Easy frontend integration.

---

# 🛠️ Technology Stack

## Backend

* Python
* Flask
* Flask-CORS

## Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

## Frontend

* HTML
* CSS
* JavaScript

---

# 📂 Project Structure

```
MHCT-by-TECH-STORM/
│
├── backend/
│   ├── app.py
│   ├── predictor.py
│   ├── recommendation.py
│   └── utils.py
│
├── database/
│   └── database.db
│
├── frontend/
│   ├── static/
│   └── templates/
│
├── ml/
│   ├── dataset/
│   │   ├── dataset.csv
│   │   └── generate_dataset.py
│   │
│   ├── models/
│   │   ├── model.pkl
│   │   ├── evaluate.py
│   │   └── predict.py
│   │
│   └── train_model.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Santanu-Maity/MHCT-by-TECH-STORM.git
```

Move into the project folder:

```bash
cd MHCT-by-TECH-STORM
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Backend

Start the Flask server:

```bash
python backend/app.py
```

The backend will run at:

```
http://127.0.0.1:5000
```

---

# 🔗 API Endpoints

## Home

**GET /**

Returns the API status.

---

## Health Check

**GET /health**

Example Response:

```json
{
    "status": "healthy",
    "service": "Mental Health Counseling Tool API",
    "model_loaded": true
}
```

---

## Predict Mental Health

**POST /predict**

Request Body:

```json
{
    "age":22,
    "gender":"Male",
    "employment_status":"Student",
    "relationship_status":"Single",
    "sleep_hours":7,
    "sleep_quality":4,
    "food_quality":4,
    "water_intake":4,
    "exercise_hours":2,
    "screen_time":6,
    "hobbies_time":2,
    "work_stress":5,
    "academic_pressure":6,
    "financial_stress":2,
    "social_interaction":4,
    "family_support":4,
    "daily_productivity":7,
    "health_issues":0
}
```

Example Response:

```json
{
    "status":"success",
    "mental_state":"Moderate Stress",
    "mental_score":100,
    "anxiety_score":83,
    "depression_score":45,
    "risk_level":"Medium",
    "recommendation":"You appear to be experiencing moderate stress. Try regular exercise, meditation, proper sleep, and speak with trusted friends or family if needed."
}
```

---

# 🤖 Machine Learning Model

* Algorithm: Random Forest Classifier
* Dataset Size: 3000 Records
* Model Serialization: Joblib (`model.pkl`)
* Data Processing:

  * One-Hot Encoding
  * Numerical Feature Processing
  * Train-Test Split
* Target Variable:

  * Good
  * Moderate Stress
  * High Stress
  * Severe Risk

---

# 📈 Future Enhancements

* User authentication.
* Real-world clinical dataset integration.
* Dashboard with charts and analytics.
* Appointment booking with counselors.
* Email notifications.
* AI chatbot integration.
* Deployment to a cloud platform.

---

# 👨‍💻 Team

**Project:** Mental Health Counseling Tool (MHCT)

Developed by **TECH STORM** as a B.Tech final-year project.

---

# 📄 License

This project is developed for educational and academic purposes.
