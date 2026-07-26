import joblib
import pandas as pd

model = joblib.load("models/baseline.joblib")


def predict_failure(sensor_data):

    model_input = {
        "Air temperature [K]":
            sensor_data["Air temperature [K]"],

        "Process temperature [K]":
            sensor_data["Process temperature [K]"],

        "Rotational speed [rpm]":
            sensor_data["Rotational speed [rpm]"],

        "Torque [Nm]":
            sensor_data["Torque [Nm]"],

        "Tool wear [min]":
            sensor_data["Tool wear [min]"]
    }

    df = pd.DataFrame([model_input])

    prediction = int(model.predict(df)[0])

    probability = float(
        model.predict_proba(df)[0][1]
    )

    label = (
        "Danger"
        if prediction == 1
        else "Healthy"
    )

    return {
        "prediction": label,
        "prediction_code": prediction,
        "probability": round(probability, 3)
    }