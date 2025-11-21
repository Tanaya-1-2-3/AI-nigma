import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

# Categories and example merchants
categories = {
    "Food & Dining": ["McDonald's", "Starbucks", "Subway", "Domino's", "KFC", "Pizza Hut", "Cafe Nero"],
    "Shopping": ["Amazon", "Walmart", "Target", "Etsy", "Best Buy", "Flipkart"],
    "Travel": ["Uber", "Lyft", "Delta Airlines", "Airbnb", "Trainline", "Ola", "Taxi Service"],
    "Entertainment": ["Netflix", "Spotify", "Hulu", "Disney+", "Movie Theater", "Cinema"],
    "Utilities": ["Electric Company", "Water Board", "Gas Co", "Internet Service", "Phone Bill"],
    "Healthcare": ["Walgreens", "CVS Pharmacy", "Rite Aid", "Hospital", "Clinic"],
    "Fitness": ["Gym Membership", "Yoga Studio", "Planet Fitness", "Fitbit Subscription"],
    "Finance": ["Bank Transfer", "Credit Card Payment", "Loan EMI", "Investment Platform"],
    "Others": ["Charity Donation", "Gift Shop", "Miscellaneous"]
}

rows = []
num_rows = 50000

for _ in range(num_rows):
    category = random.choice(list(categories.keys()))
    merchant = random.choice(categories[category])

    # Realistic descriptions
    if category == "Travel":
        description = f"{merchant} ride from {fake.city()}"
    elif category == "Food & Dining":
        description = f"{merchant} order {random.randint(100,999)}"
    else:
        description = f"{merchant} {fake.word().capitalize()}"

    # Realistic amounts
    if category == "Food & Dining":
        amount = round(random.uniform(3, 100), 2)
    elif category == "Shopping":
        amount = round(random.uniform(10, 500), 2)
    elif category == "Travel":
        amount = round(random.uniform(5, 1000), 2)
    elif category == "Entertainment":
        amount = round(random.uniform(5, 50), 2)
    elif category == "Utilities":
        amount = round(random.uniform(20, 300), 2)
    elif category == "Healthcare":
        amount = round(random.uniform(10, 200), 2)
    elif category == "Fitness":
        amount = round(random.uniform(10, 150), 2)
    elif category == "Finance":
        amount = round(random.uniform(50, 2000), 2)
    else:
        amount = round(random.uniform(5, 500), 2)

    date = fake.date_between(start_date="-1y", end_date="today")
    rows.append([description, amount, category, date])

df = pd.DataFrame(rows, columns=["description", "amount", "category", "date"])
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

os.makedirs("../data", exist_ok=True)
df.to_csv("../data/transactions_large.csv", index=False)
print(f"✅ Dataset created with {len(df)} rows at ../data/transactions_large.csv")
