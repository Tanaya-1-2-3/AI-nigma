import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/transactions_large.csv")
MODEL_PATH = os.path.join(BASE_DIR, "cafc_xgb_model.joblib")
VECTORIZER_PATH = os.path.join(BASE_DIR, "semantic_vectorizer.joblib")
LABEL_ENCODER_PATH = os.path.join(BASE_DIR, "cafc_label_encoder.joblib")

# Load dataset
df = pd.read_csv(DATA_PATH)

# TF-IDF features on description
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3), max_features=100)
X_text = vectorizer.fit_transform(df["description"]).toarray()

# Numeric features (normalize amount)
X_amount = df["amount"].values.reshape(-1, 1) / 1000.0
X_features = np.hstack([X_text, X_amount])

# Labels
le = LabelEncoder()
y = le.fit_transform(df["category"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_features, y, test_size=0.2, random_state=42
)

# Train XGBoost with verbosity
model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    eval_metric="mlogloss",
    random_state=42,
    verbosity=1  # <-- Show training progress
)
model.fit(X_train, y_train)

# Evaluate
acc = model.score(X_test, y_test)
print(f"Test accuracy: {acc*100:.2f}%")

# Save artifacts
joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)
joblib.dump(le, LABEL_ENCODER_PATH)

print("✅ Model training complete!")
