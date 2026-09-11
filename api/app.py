from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel


# Create FastAPI app
app = FastAPI(title="Customer Churn Prediction API")


# -------------------------
# Home endpoint
# -------------------------
@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }


# -------------------------
# Health check endpoint
# -------------------------
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# -------------------------
# Load trained model
# -------------------------
model = joblib.load(
    "models/logistic_regression_churn_model.pkl"
)


# -------------------------
# Input data schema
# -------------------------
class CustomerData(BaseModel):
    tenure: float
    MonthlyCharges: float
    TotalCharges: float


# -------------------------
# Prediction endpoint
# -------------------------
@app.post("/predict")
def predict(data: CustomerData):

    # Get the exact feature names used during model training
    feature_names = model.feature_names_in_

    # Create input dataframe with all required features
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=feature_names
    )

    # Add the three values provided by the user
    input_data["tenure"] = data.tenure
    input_data["MonthlyCharges"] = data.MonthlyCharges
    input_data["TotalCharges"] = data.TotalCharges

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get churn probability
    probability = model.predict_proba(input_data)[0][1]

    # Return result
    return {
        "prediction": int(prediction),
        "churn_probability": round(float(probability), 3)
    }