# AI-nigma
Below is a **complete, polished, production-ready `README.md`** for your GitHub repository.
It includes everything: badges, setup, screenshots placeholders, API docs, ML pipeline, future scope, and more.

---

# 💰 Smart Transaction Categorization System

### *AI-Powered Personal Finance Intelligence*

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-teal.svg)
![Next.js](https://img.shields.io/badge/Frontend-Next.js-black.svg)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

The **Smart Transaction Categorization System** is a full-stack AI-powered web application that automatically classifies financial transactions (e.g., “Starbucks Coffee”, “Uber Ride”, “Amazon Purchase”) into meaningful categories such as:

* **Food**
* **Travel**
* **Shopping**
* **Entertainment**
* **Utilities**
* **Medical**
* **Salary / Income**, etc.

This system combines:

* **Next.js Frontend** → Beautiful UI + charts (Bar & Doughnut)
* **FastAPI Backend** → Handles prediction API
* **XGBoost ML Model** → Trained on synthetic + semantic text embeddings
* **NLP + Vectorizer** → Converts transaction descriptions into embeddings

The result is a **responsive, accurate, and intelligent personal finance AI tool**.

---

## 🎯 Features

### ✅ Core Features

* 🔍 **AI-based automatic transaction classification**
* 📊 **Beautiful interactive bar charts & pie charts**
* 📈 **Visual probability breakdown**
* ⚡ **Ultra-fast predictions (FastAPI + XGBoost)**
* ⛓ **End-to-end ML pipeline: training → model → API → UI**
* 🎨 **Modern, responsive, animated UI**

### 🚀 Additional Enhancements

* Confidence-based color indicators
* Spending summary visualizations
* Real-time results dashboard
* Clean semantic embeddings for text classification

---

## 🧠 Why XGBoost?

XGBoost was selected because:

* ✔ Excellent performance on **tabular + text-vector mixed features**
* ✔ Handles **imbalanced classes** better than many algorithms
* ✔ Fast training + fast inference
* ✔ Highly tunable with boosting
* ✔ Works extremely well with TF-IDF / embedding vectors

This makes it ideal for **real-world financial classification**.

---

## 🧩 System Architecture

```
User → Next.js UI → /api/classify → FastAPI ML Backend → XGBoost Model → Prediction → UI Visualized
```

---

## 📂 Folder Structure

```
.
├── app/                     # Next.js frontend
│   ├── api/classify        # API route
│   ├── page.jsx            # Frontend UI
│
├── api/                     # FastAPI backend
│   ├── app.py              # Main backend server
│
├── scripts/                 # ML training pipeline
│   ├── generate_dataset.py
│   ├── train_large_model.py
│
├── data/                    # Saved models + vectorizers
│   ├── cafc_xgb_model.joblib
│   ├── semantic_vectorizer.joblib
│   ├── cafc_label_encoder.joblib
│
├── package.json
├── README.md
└── requirements.txt
```

---

## 🛠 Tech Stack

### **Frontend**

* 💻 Next.js 14
* 🎨 TailwindCSS
* 📊 Chart.js (Bar + Doughnut)

### **Backend**

* ⚡ FastAPI
* 🚀 Uvicorn server

### **Machine Learning**

* 🧠 XGBoost
* 📚 Scikit-learn
* 🔡 TF-IDF / semantic vectorizer
* 🔧 Joblib (model saving)

---

## 🧪 Local Setup Instructions

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

---

## 🔧 Backend Setup (FastAPI + ML Model)

### **2️⃣ Create a Virtual Environment**

```bash
cd api
python -m venv venv
source venv/Scripts/activate    # Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Run FastAPI Backend**

```bash
uvicorn app:app --reload --port 8000
```

Backend runs at:
👉 [http://localhost:8000/predict](http://localhost:8000/predict)
👉 [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)

---

## 🎨 Frontend Setup (Next.js)

### **5️⃣ Install Dependencies**

```bash
cd app
npm install
```

### **6️⃣ Run the Frontend**

```bash
npm run dev
```

Frontend runs at:
👉 [http://localhost:3000](http://localhost:3000)

---

## 🤖 Training the ML Model (Optional)

### **Generate Dataset**

```bash
python scripts/generate_dataset.py
```

### **Train the Model**

```bash
python scripts/train_large_model.py
```

This produces:

* `cafc_xgb_model.joblib`
* `semantic_vectorizer.joblib`
* `cafc_label_encoder.joblib`

---

## 📡 API Documentation

### **POST /predict**

```json
{
  "description": "Swiggy food order",
  "amount": 450
}
```

### **Response**

```json
{
  "predicted_category": "Food",
  "confidence": 0.92,
  "probabilities": {
    "Food": 0.92,
    "Travel": 0.01,
    "Shopping": 0.03,
    "Medical": 0.02
  }
}
```

---

## 💼 Real-World Applications

This project is valuable for:

### 🧑‍🏫 Students

Track and categorize spending automatically.

### 👨‍💼 Working Professionals

Understand spending patterns instantly.

### 🏪 Small Business Owners

Categorize business expenses automatically.

### 🏦 FinTech Startups

Can integrate into budgeting, payments, or banking apps.

---

## 🌱 Future Scope

* 📱 **Mobile App (React Native / Flutter)**
* 🏦 **Real-time bank API integration** (Plaid / SaltEdge)
* 🤖 **Transformer-based text embeddings** (BERT)
* 🔥 **Auto-learning model via user feedback**
* 📈 **Advanced financial dashboards**
* 🧾 **Receipt scanning (OCR + classification)**

---

