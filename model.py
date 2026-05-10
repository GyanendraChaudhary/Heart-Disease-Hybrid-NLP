import os
import joblib
import numpy as np
import pandas as pd

from scipy.sparse import hstack
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

MODEL_PATH = "model.pkl"

def load_data():
    if not os.path.exists("data/heart.csv"):
        raise FileNotFoundError("data/heart.csv not found. Run generate_data.py first.")
    return pd.read_csv("data/heart.csv")

def prepare_features(df):
    numeric_cols = ["age", "sex", "cp", "trestbps", "chol", "thalach"]
    text_col = "symptoms"

    X_num = df[numeric_cols]
    y = df["target"]

    scaler = StandardScaler()
    X_num_scaled = scaler.fit_transform(X_num)

    vectorizer = TfidfVectorizer(max_features=150, stop_words="english")
    X_text = vectorizer.fit_transform(df[text_col])

    X_final = hstack([X_num_scaled, X_text])
    return X_final, y, scaler, vectorizer

def train_model():
    df = load_data()
    X, y, scaler, vectorizer = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    rf = RandomForestClassifier(n_estimators=250, max_depth=10, random_state=42)
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    bundle = {
        "model": rf,
        "scaler": scaler,
        "vectorizer": vectorizer,
        "accuracy": accuracy,
        "confusion_matrix": cm,
        "report": report,
        "columns": ["age", "sex", "cp", "trestbps", "chol", "thalach"]
    }

    joblib.dump(bundle, MODEL_PATH)
    return bundle

def load_or_train_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return train_model()

def compare_models():
    df = load_data()
    X, y, scaler, vectorizer = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=250, max_depth=10, random_state=42)
    }

    results = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        acc = accuracy_score(y_test, pred)
        results.append({"Model": name, "Accuracy": round(acc * 100, 2)})

    return pd.DataFrame(results)

def predict_risk(age, gender, chest_pain, bp, chol, heart_rate, symptoms):
    bundle = load_or_train_model()
    model = bundle["model"]
    scaler = bundle["scaler"]
    vectorizer = bundle["vectorizer"]

    sex = 1 if gender == "Male" else 0
    cp = 3 if chest_pain == "Severe" else 2 if chest_pain == "Moderate" else 1 if chest_pain == "Mild" else 0

    num = np.array([[age, sex, cp, bp, chol, heart_rate]])
    num_scaled = scaler.transform(num)

    text_vec = vectorizer.transform([symptoms])
    final_input = hstack([num_scaled, text_vec])

    prediction = model.predict(final_input)[0]
    probability = model.predict_proba(final_input)[0][1] * 100

    return prediction, probability