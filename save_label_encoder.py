import joblib
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Use the same categories you used in training
categories = [
    'Shopping', 'Travel', 'Groceries', 'Subscriptions',
    'Dining', 'Healthcare', 'Utilities', 'Entertainment'
]

# Create LabelEncoder
le = LabelEncoder()
le.fit(categories)

# Save it
joblib.dump(le, "cafc_label_encoder.joblib")
print("Label encoder saved ✅")
