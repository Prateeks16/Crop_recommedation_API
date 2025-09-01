
# 🌱 Crop Recommendation API

A **FastAPI-based Machine Learning API** that recommends the top 5 crops suitable for cultivation based on soil and weather parameters.
The model is powered by a **RandomForest Classifier** trained on the final preprocessed dataset (`final_train_balanced`).

---

## 📌 Features

* 🚀 **FastAPI** backend with RESTful endpoints
* 🌾 **RandomForest model** trained on 7 key soil & climate features:

  * Nitrogen (N)
  * Phosphorus (P)
  * Potassium (K)
  * Temperature
  * Humidity
  * pH
  * Rainfall
* 🔮 Returns **Top-5 ranked crop recommendations** with confidence scores
* 📦 Dockerized for easy deployment
* 🔑 JSON API for integration with frontend / Node.js backend

---

## 📂 Project Structure

```
crop-recommendation-api/
│── rf.pkl                # Trained RandomForest model
│── main.py               # FastAPI app with endpoints
│── requirements.txt      # Dependencies
│── Dockerfile            # For containerization
│── README.md             # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/crop-recommendation-api.git
cd crop-recommendation-api
```

### 2️⃣ Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

pip install -r requirements.txt
```

### 3️⃣ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server runs at 👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🛠️ API Endpoints

### **1. Root Endpoint**

```http
GET /
```

**Response:**

```json
{"message": "Crop Recommendation API is running 🚀"}
```

---

### **2. Predict Top-5 Crops**

```http
POST /predict
```

#### 📥 Request Body (JSON):

```json
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 25.5,
  "humidity": 80,
  "ph": 6.5,
  "rainfall": 200
}
```

#### 📤 Response:

```json
{
  "recommendations": [
    {"crop": "rice", "probability": 0.65},
    {"crop": "maize", "probability": 0.20},
    {"crop": "banana", "probability": 0.07},
    {"crop": "mango", "probability": 0.05},
    {"crop": "cotton", "probability": 0.03}
  ]
}
```

---

## 🐳 Run with Docker

### 1️⃣ Build Docker Image

```bash
docker build -t crop-api .
```

### 2️⃣ Run Container

```bash
docker run -d -p 8000:8000 crop-api
```

Now API is available at 👉 **[http://localhost:8000](http://localhost:8000)**

---

## 📊 Model Training

* Model: **RandomForestClassifier (n\_estimators=200, random\_state=42)**
* Dataset: `final_train_balanced` (7 numeric features + label)
* Output: `rf.pkl` saved with feature names

---

## 👨‍💻 Tech Stack

* **FastAPI** – RESTful API framework
* **Scikit-learn** – Machine Learning (RandomForest)
* **Joblib** – Model persistence
* **Uvicorn** – ASGI server
* **Docker** – Containerization

---

## 🚀 Future Enhancements

* 🌍 Add state & district level recommendations
* 📈 Improve ranking with ensemble models
* 🌦️ Integrate real-time weather APIs

---

