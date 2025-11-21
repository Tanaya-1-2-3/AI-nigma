from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Initialize FastAPI
app = FastAPI()

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "cafc_xgb_model.joblib")
VECTORIZER_PATH = os.path.join(BASE_DIR, "semantic_vectorizer.joblib")
LABEL_ENCODER_PATH = os.path.join(BASE_DIR, "cafc_label_encoder.joblib")

# Load artifacts
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
le = joblib.load(LABEL_ENCODER_PATH)

# Request body
class Transaction(BaseModel):
    description: str
    amount: float

@app.post("/predict")
def predict(transaction: Transaction):
    try:
        # Transform input
        X_text = vectorizer.transform([transaction.description]).toarray()
        X_amount = np.array([[transaction.amount / 1000.0]])  # normalize
        X_features = np.hstack([X_text, X_amount])

        # Predict
        y_proba = model.predict_proba(X_features)[0]
        y_pred = model.predict(X_features)[0]
        category = le.inverse_transform([y_pred])[0]

        # Return
        return {
            "predicted_category": category,
            "probabilities": {cls: float(prob) for cls, prob in zip(le.classes_, y_proba)}
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
