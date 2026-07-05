import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ==============================
# Load Dataset
# ==============================

df = pd.read_csv("ml/dataset/dataset.csv")

print("Dataset Loaded Successfully")
print(df.head())
print(df["mental_state"].value_counts())

# ==============================
# Features & Target
# ==============================

X = df.drop(columns=[
    "mental_state",
    "mental_score",
    "anxiety_score",
    "depression_score"
])

y = df["mental_state"]

# ==============================
# Categorical Columns
# ==============================

categorical_columns = [
    "gender",
    "employment_status",
    "relationship_status"
]

# ==============================
# Numerical Columns
# ==============================

numerical_columns = [
    col for col in X.columns
    if col not in categorical_columns
]

# ==============================
# Preprocessing
# ==============================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),
        (
            "num",
            "passthrough",
            numerical_columns
        )
    ]
)

# ==============================
# Random Forest Model
# ==============================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", model)
])

# ==============================
# Train/Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==============================
# Train Model
# ==============================

pipeline.fit(X_train, y_train)

# ==============================
# Predictions
# ==============================

predictions = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

# ==============================
# Save Model
# ==============================

os.makedirs("ml/models", exist_ok=True)

joblib.dump(
    pipeline,
    "ml/models/model.pkl"
)

print("\nModel Saved Successfully!")