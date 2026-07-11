# 🧠 MindCare AI – Mental Health Counseling Tool

MindCare AI is an AI-powered Mental Health Counseling Tool that helps users assess their mental well-being through a structured questionnaire and Machine Learning prediction model. The application provides personalized recommendations, tracks assessment history, visualizes progress, and generates downloadable PDF reports.

---

## 📌 Features

* 🔐 User Authentication (Signup/Login)
* 📝 Mental Health Assessment
* 🤖 Machine Learning Based Prediction
* 📊 Interactive Dashboard
* 📈 Progress & Trend Analysis
* 💬 AI Chatbot Support
* 📄 PDF Assessment Report Generation
* 👤 User Profile Management
* 📚 Assessment History
* 📱 Responsive Modern UI

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Backend

* Python
* Flask
* Flask-CORS

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

### Database

* SQLite

### Other Libraries

* ReportLab
* Bcrypt
* Matplotlib

---

## 📂 Project Structure

```text
MHCT-by-TECH-STORM/
│
├── backend/
│   ├── app.py
│   ├── auth.py
│   ├── predictor.py
│   ├── chatbot.py
│   ├── recommendation.py
│   ├── database.py
│   ├── dashboard.py
│   ├── assessment_db.py
│   ├── history.py
│   ├── profile.py
│   ├── chart.py
│   ├── trend.py
│   ├── pdf_report.py
│   └── utils.py
│
├── frontend/
│   ├── templates/
│   └── static/
│       ├── css/
│       └── js/
│
├── ml/
│   ├── dataset/
│   ├── models/
│   ├── utils/
│   └── train_model.py
│
├── database/
│   └── database.db
│
├── docs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Santanu-Maity/MHCT-by-TECH-STORM.git
```

### 2. Move into the Project Directory

```bash
cd MHCT-by-TECH-STORM
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask Server

```bash
cd backend
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## 🚀 Deployment

The project is deployed using:

* Backend: Render
* Repository: GitHub

---

## 🧠 Machine Learning Model

The prediction model analyzes user responses based on lifestyle, stress, sleep, work, social interaction, and health-related factors.

Possible prediction categories include:

* Healthy
* Mild Stress
* Moderate Stress
* Severe Stress

---

## 📊 System Modules

* User Authentication
* Mental Health Assessment
* ML Prediction Engine
* Recommendation System
* Dashboard Analytics
* Trend Analysis
* Assessment History
* Profile Management
* AI Chatbot
* PDF Report Generation

---

## 🔒 Security Features

* Password Hashing using Bcrypt
* Session-Based Authentication
* Server-side Validation
* Input Validation
* Secure Database Access

---

## 📄 API Endpoints

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | /                | Landing Page             |
| GET    | /login           | Login Page               |
| GET    | /signup          | Signup Page              |
| POST   | /login           | User Login               |
| POST   | /signup          | User Registration        |
| POST   | /logout          | Logout                   |
| POST   | /predict         | Mental Health Prediction |
| GET    | /dashboard-data  | Dashboard Statistics     |
| GET    | /chart-data      | Assessment Chart         |
| GET    | /trend-data      | Trend Analysis           |
| GET    | /history         | Assessment History       |
| GET    | /profile-data    | User Profile             |
| POST   | /chat            | AI Chatbot               |
| GET    | /download-report | Download PDF Report      |
| GET    | /health          | Health Check             |

---

## 📈 Future Enhancements

* Email Notifications
* Multi-language Support
* Doctor Dashboard
* Appointment Scheduling
* Emotion Detection
* Voice-based Assessment
* Cloud Database Integration
* Mobile Application
* Advanced AI Chatbot using LLMs

---

## 👨‍💻 Team

**TECH STORM**

Project: **MindCare AI – Mental Health Counseling Tool**

---

## 📜 License

This project is developed for educational and academic purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
