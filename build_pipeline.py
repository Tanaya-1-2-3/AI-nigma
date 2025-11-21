import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import xgboost as xgb
import joblib

# Load your mock dataset or real training data
mock_transactions = pd.DataFrame({
    'description': [
        'AMAZON MKTPLACE', 'UBER TRIP', 'WHOLE FOODS', 'NETFLIX SUBSCRIPTION',
        'RESTAURANT PIZZA', 'WALGREENS PHARMACY', 'ELECTRIC COMPANY', 'MOVIE THEATER',
    ],
    'amount': [59.99, 22.50, 87.45, 14.99, 45.00, 32.10, 120.00, 15.00],
    'category': [
        'Shopping', 'Travel', 'Groceries', 'Subscriptions',
        'Dining', 'Healthcare', 'Utilities', 'Entertainment'
    ],
})

# TF-IDF for description
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2,3), max_features=50)

# Numeric transformer for amount
def extract_amount(df):
    return df[['amount']] / 1000.0

numeric_transformer = FunctionTransformer(extract_amount)

# Combine TF-IDF + numeric
preprocessor = ColumnTransformer(
    transformers=[
        ('tfidf', vectorizer, 'description'),
        ('num', numeric_transformer, ['amount'])
    ]
)

# Create pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('xgb', xgb.XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        use_label_encoder=False,
        eval_metric='mlogloss',
        random_state=42
    ))
])

# Encode categories
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(mock_transactions['category'])

# Train pipeline
pipeline.fit(mock_transactions[['description','amount']], y)

# Save artifacts
joblib.dump(pipeline, "cafc_pipeline.joblib")
joblib.dump(le, "cafc_label_encoder.joblib")

print("Pipeline and label encoder saved ✅")
