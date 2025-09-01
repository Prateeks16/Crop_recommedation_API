from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained RF model
model = joblib.load("rf.pkl")

# Expected features
FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# FastAPI app
app = FastAPI(title="Crop Prediction API", version="2.0")

# Request schema
class CropRequest(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.get("/")
def root():
    return {"message": "🌱 Crop Prediction API is running with Top-5 recommendations!"}

@app.post("/predict")
def predict(request: CropRequest):
    # Convert input into numpy array
    data = np.array([[getattr(request, f) for f in FEATURES]])

    # Predict probabilities for all classes
    probs = model.predict_proba(data)[0]

    # Get class labels
    classes = model.classes_

    # Sort by probability (descending), take top 5
    top_indices = np.argsort(probs)[::-1][:5]
    top_crops = [
        {"crop": classes[i], "probability": round(float(probs[i]), 4)}
        for i in top_indices
    ]

    return {
        "top_5_recommendations": top_crops,
        "best_crop": top_crops[0]["crop"]
    }
