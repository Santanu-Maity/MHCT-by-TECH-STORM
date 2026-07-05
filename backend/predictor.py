import joblib
import pandas as pd

# Load the trained ML model only once
MODEL_PATH = "ml/models/model.pkl"

model = joblib.load(MODEL_PATH)


def predict_mental_state(user_data):
    """
    Predict the user's mental state using the trained model.
    """

    input_df = pd.DataFrame([user_data])

    prediction = model.predict(input_df)[0]

    return prediction