from flask import jsonify

def chatbot_response(message):
    """
    Simple rule-based chatbot.
    """

    message = message.lower()

    if any(word in message for word in ["sad", "depressed", "unhappy"]):
        return (
            "I'm sorry you're feeling this way. 💙 "
            "Remember that you're not alone. Try talking to someone you trust, "
            "taking a short walk, or practicing deep breathing."
        )

    elif any(word in message for word in ["stress", "stressed", "pressure"]):
        return (
            "Stress can be overwhelming. 🌿 "
            "Take short breaks, stay hydrated, and focus on one task at a time."
        )

    elif any(word in message for word in ["anxiety", "anxious", "panic"]):
        return (
            "Try taking slow deep breaths. "
            "Focus on your surroundings and remember that anxious feelings often pass."
        )

    elif any(word in message for word in ["happy", "good", "great", "fine"]):
        return (
            "That's wonderful to hear! 😊 "
            "Keep taking care of yourself and maintain those healthy habits."
        )

    elif any(word in message for word in ["hello", "hi", "hey"]):
        return (
            "Hello! 👋 How are you feeling today?"
        )

    else:
        return (
            "Thank you for sharing. 💙 "
            "Can you tell me a little more about how you're feeling?"
        )