
import sys
import pandas as pd
import joblib
from pathlib import Path

# Locate the existing trained model
MODEL_PATH = (
    Path.home() / "motor-ai" / "motor_model.pkl"
)

# Load the trained model
model = joblib.load(MODEL_PATH)


def predict_motor(motor_data):
    """Predict motor condition using the trained AI model."""

    readings = pd.DataFrame(
        [[
            motor_data["temperature"],
            motor_data["current"],
            motor_data["vibration"],
            motor_data["speed"]
        ]],
        columns=[
            "temperature",
            "current",
            "vibration",
            "speed"
        ]
    )

    prediction = model.predict(readings)[0]
    probabilities = model.predict_proba(readings)[0]

    confidence = {
        condition: round(float(probability) * 100, 2)
        for condition, probability in zip(
            model.classes_,
            probabilities
        )
    }

    if prediction == "Normal":
        recommendation = "Continue routine monitoring."
    elif prediction == "Warning":
        recommendation = "Inspect the motor and monitor sensor trends."
    else:
        recommendation = "Investigate the motor promptly."

    return {
        "condition": str(prediction),
        "confidence": confidence,
        "recommendation": recommendation
    }