def get_recommendation(mental_state):
    """
    Return a recommendation based on the predicted mental state.
    """

    recommendations = {

        "Excellent": {
            "advice": "Your mental health appears excellent. Continue maintaining your healthy lifestyle, balanced diet, exercise, and regular sleep.",
            "risk_level": "Low"
        },

        "Good": {
            "advice": "Your mental health is good. Continue your healthy routine and practice mindfulness to maintain your well-being.",
            "risk_level": "Low"
        },

        "Moderate Stress": {
            "advice": "You appear to be experiencing moderate stress. Try regular exercise, meditation, proper sleep, and speak with trusted friends or family if needed.",
            "risk_level": "Medium"
        },

        "High Stress": {
            "advice": "Your stress level appears high. Consider reducing stressors, maintaining a healthy routine, and consulting a mental health professional if symptoms continue.",
            "risk_level": "High"
        },

        "Severe Risk": {
            "advice": "Your responses indicate a high level of distress. Please seek support from a qualified mental health professional as soon as possible.",
            "risk_level": "Critical"
        }

    }

    return recommendations.get(
        mental_state,
        {
            "advice": "No recommendation available.",
            "risk_level": "Unknown"
        }
    )