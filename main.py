from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("rf.pkl")


FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

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
    data = np.array([[getattr(request, f) for f in FEATURES]])
    probs = model.predict_proba(data)[0]
    classes = model.classes_
    top_indices = np.argsort(probs)[::-1][:5]
    top_crops = [
        {"crop": classes[i], "probability": round(float(probs[i]), 4)}
        for i in top_indices
    ]
    return {
        "top_5_recommendations": top_crops,
        "best_crop": top_crops[0]["crop"]
    }
