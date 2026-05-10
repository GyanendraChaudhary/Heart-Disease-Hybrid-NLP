import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import os

from model import load_or_train_model, predict_risk, compare_models
import config

st.set_page_config(
    page_title="Heart Disease Prediction Using Hybrid NLP",
    page_icon="❤️",
    layout="wide"
)

# ---------------- THEME ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #06111f, #102542, #250d2e);
    color: white;
}
.big-title {
    font-size: 42px;
    font-weight: 900;
    text-align: center;
    color: white;
}
.sub {
    text-align: center;
    color: #c9d6e3;
    font-size: 18px;
}
.card {
    background: rgba(255,255,255,0.09);
    padding: 22px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.16);
    box-shadow: 0 8px 28px rgba(0,0,0,.3);
}
.red-card {
    background: linear-gradient(135deg, #ff416c, #ff4b2b);
    padding: 20px;
    border-radius: 18px;
    text-align:center;
    color:white;
}
.green-card {
    background: linear-gradient(135deg, #11998e, #38ef7d);
    padding: 20px;
    border-radius: 18px;
    text-align:center;
    color:white;
}
.blue-card {
    background: linear-gradient(135deg, #1d2671, #0f9bff);
    padding: 20px;
    border-radius: 18px;
    text-align:center;
    color:white;
}
.stButton>button {
    background: linear-gradient(135deg, #ff416c, #ff4b2b);
    color: white;
    border-radius: 12px;
    font-weight: bold;
    width: 100%;
    padding: 12px;
}
[data-testid="stSidebar"] {
    background: #06111f;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
bundle = load_or_train_model()

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("❤️ Project Navigation")

page = st.sidebar.radio(
    "Go to Page",
    [
        "1. Home Dashboard",
        "2. Patient Prediction",
        "3. Quick Health Check",
        "4. NLP Symptom Analyzer",
        "5. Dataset & EDA",
        "6. Model Performance",
        "7. Patient Report",
        "8. System Architecture",
        "9. Methodology",
        "10. Conclusion & Future Work"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write(f"**Project:** {config.APP_NAME}")
st.sidebar.write(f"**Author:** {config.AUTHOR}")
st.sidebar.write("**Frontend:** Streamlit")
st.sidebar.write("**Backend:** Python")
st.sidebar.write("**ML:** Random Forest")
st.sidebar.write("**NLP:** TF-IDF")

# ---------------- HEADER FUNCTION ----------------
def title(text, sub):
    st.markdown(f"<div class='big-title'>{text}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sub'>{sub}</div>", unsafe_allow_html=True)
    st.write("")

# ---------------- PAGE 1 ----------------
if page == "1. Home Dashboard":
    title("❤️ HEART DISEASE PREDICTION USING HYBRID NLP", "Professional B.Tech Final Year AI Healthcare Project")

    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("<div class='red-card'><h3>Frontend</h3><h2>Streamlit</h2></div>", unsafe_allow_html=True)
    c2.markdown("<div class='blue-card'><h3>Backend</h3><h2>Python</h2></div>", unsafe_allow_html=True)
    c3.markdown("<div class='red-card'><h3>ML Model</h3><h2>Random Forest</h2></div>", unsafe_allow_html=True)
    c4.markdown("<div class='blue-card'><h3>NLP</h3><h2>TF-IDF</h2></div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div class="card">
    <h2>📌 Project Overview</h2>
    <p>
    This project predicts heart disease risk using a hybrid AI approach.
    It combines structured medical data such as age, blood pressure, cholesterol, heart rate,
    and chest pain type with patient symptom text processed using Natural Language Processing.
    </p>
    <p>
    The system includes multiple modules such as patient prediction, symptom analyzer,
    dataset analysis, model performance, report generation, architecture, and methodology.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.success("Project dashboard is ready. Use the sidebar to explore all modules.")

# ---------------- COMMON INPUT FUNCTION ----------------
def patient_form():
    st.subheader("👤 Patient Profile")
    p1, p2 = st.columns(2)

    with p1:
        name = st.text_input("Patient Name", "Gyanendra Chaudhary")
        pid = st.text_input("Patient ID", "P001")
        contact = st.text_input("Contact Number", "9876543210")

    with p2:
        city = st.text_input("City", "Greater Noida")
        checkup_date = st.date_input("Checkup Date", date.today())
        lifestyle = st.selectbox("Lifestyle", ["Active", "Moderate", "Sedentary"])

    st.subheader("❤️ Medical Details")
    m1, m2 = st.columns(2)

    with m1:
        age = st.slider("Age", 20, 90, 45)
        bp = st.slider("Resting Blood Pressure", 80, 220, 130)
        chol = st.slider("Cholesterol Level", 100, 450, 220)

    with m2:
        heart_rate = st.slider("Maximum Heart Rate", 60, 220, 150)
        gender = st.selectbox("Gender", ["Male", "Female"])
        chest_pain = st.selectbox("Chest Pain Type", ["None", "Mild", "Moderate", "Severe"])

    symptoms = st.text_area("Symptoms / Clinical Notes", "chest pain, shortness of breath, fatigue")

    return name, pid, contact, city, checkup_date, lifestyle, age, bp, chol, heart_rate, gender, chest_pain, symptoms

# ---------------- PAGE 2 ----------------
if page == "2. Patient Prediction":
    title("🧾 Patient Prediction", "Enter complete patient details and predict heart disease risk")

    left, right = st.columns([1.2, 1])

    with left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        data = patient_form()
        btn = st.button("🔍 Predict Heart Disease Risk")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📋 What This Page Does")
        st.write("✅ Takes patient name and personal details")
        st.write("✅ Takes medical values")
        st.write("✅ Takes symptom text")
        st.write("✅ Uses NLP + ML for prediction")
        st.write("✅ Generates downloadable report")
        st.markdown("</div>", unsafe_allow_html=True)

    if btn:
        name, pid, contact, city, checkup_date, lifestyle, age, bp, chol, heart_rate, gender, chest_pain, symptoms = data
        pred, prob = predict_risk(age, gender, chest_pain, bp, chol, heart_rate, symptoms)

        st.markdown("---")
        st.subheader("🧠 Prediction Result")

        r1, r2, r3 = st.columns(3)

        with r1:
            if pred == 1:
                st.markdown("<div class='red-card'><h3>Status</h3><h1>HIGH RISK</h1></div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='green-card'><h3>Status</h3><h1>LOW RISK</h1></div>", unsafe_allow_html=True)

        with r2:
            st.markdown(f"<div class='blue-card'><h3>Risk Probability</h3><h1>{prob:.2f}%</h1></div>", unsafe_allow_html=True)

        with r3:
            confidence = "Strong" if prob > 70 else "Moderate" if prob > 40 else "Low"
            st.markdown(f"<div class='blue-card'><h3>Confidence</h3><h1>{confidence}</h1></div>", unsafe_allow_html=True)

        g1, g2 = st.columns(2)

        with g1:
            fig, ax = plt.subplots()
            ax.barh(["Risk Score"], [prob])
            ax.set_xlim(0, 100)
            ax.set_title("Heart Disease Risk Score")
            st.pyplot(fig)

        with g2:
            vals = [age / 90 * 100, bp / 220 * 100, chol / 450 * 100, heart_rate / 220 * 100, min(len(symptoms) * 2, 100)]
            fig2, ax2 = plt.subplots()
            ax2.bar(["Age", "BP", "Chol", "HR", "Symptoms"], vals)
            ax2.set_title("Feature Impact Analysis")
            st.pyplot(fig2)

        report = {
            "Patient Name": name,
            "Patient ID": pid,
            "Contact": contact,
            "City": city,
            "Date": checkup_date,
            "Lifestyle": lifestyle,
            "Age": age,
            "Gender": gender,
            "Blood Pressure": bp,
            "Cholesterol": chol,
            "Heart Rate": heart_rate,
            "Chest Pain": chest_pain,
            "Symptoms": symptoms,
            "Prediction": "High Risk" if pred == 1 else "Low Risk",
            "Risk Probability": f"{prob:.2f}%"
        }

        st.subheader("📄 Patient Report Summary")
        st.table(pd.DataFrame(report.items(), columns=["Field", "Value"]))

        st.download_button(
            "⬇️ Download Patient Report CSV",
            data=pd.DataFrame([report]).to_csv(index=False).encode("utf-8"),
            file_name=f"{name.replace(' ', '_')}_heart_report.csv",
            mime="text/csv"
        )

# ---------------- PAGE 3 ----------------
if page == "3. Quick Health Check":
    title("⚡ Quick Health Check", "Fast risk screening without full patient profile")

    age = st.slider("Age", 20, 90, 50)
    bp = st.slider("Blood Pressure", 80, 220, 140)
    chol = st.slider("Cholesterol", 100, 450, 240)
    heart_rate = st.slider("Heart Rate", 60, 220, 135)
    gender = st.selectbox("Gender", ["Male", "Female"])
    chest_pain = st.selectbox("Chest Pain", ["None", "Mild", "Moderate", "Severe"])
    symptoms = st.text_area("Symptoms", "chest pain and fatigue")

    if st.button("Run Quick Check"):
        pred, prob = predict_risk(age, gender, chest_pain, bp, chol, heart_rate, symptoms)
        if pred == 1:
            st.error(f"⚠️ High Risk Detected: {prob:.2f}%")
        else:
            st.success(f"✅ Low Risk Detected: {prob:.2f}%")

# ---------------- PAGE 4 ----------------
if page == "4. NLP Symptom Analyzer":
    title("🧠 NLP Symptom Analyzer", "Analyze symptom text using TF-IDF NLP technique")

    text = st.text_area("Enter symptom text", "chest pain shortness of breath dizziness fatigue")
    if st.button("Analyze Text"):
        vectorizer = bundle["vectorizer"]
        vec = vectorizer.transform([text])
        words = vectorizer.get_feature_names_out()
        scores = vec.toarray()[0]

        rows = []
        for word, score in zip(words, scores):
            if score > 0:
                rows.append({"Medical Term": word, "TF-IDF Score": round(score, 4)})

        if rows:
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
        else:
            st.warning("No important medical term found in current vocabulary.")

# ---------------- PAGE 5 ----------------
if page == "5. Dataset & EDA":
    title("📊 Dataset & EDA", "Dataset preview and exploratory data analysis")

    if os.path.exists("data/heart.csv"):
        df = pd.read_csv("data/heart.csv")
        st.dataframe(df.head(30), use_container_width=True)

        c1, c2, c3 = st.columns(3)
        c1.markdown(f"<div class='red-card'><h3>Total Records</h3><h1>{len(df)}</h1></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='blue-card'><h3>Total Columns</h3><h1>{len(df.columns)}</h1></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='red-card'><h3>Target Classes</h3><h1>{df['target'].nunique()}</h1></div>", unsafe_allow_html=True)

        st.subheader("Statistical Summary")
        st.dataframe(df.describe(), use_container_width=True)

        g1, g2 = st.columns(2)
        with g1:
            fig, ax = plt.subplots()
            df["target"].value_counts().plot(kind="bar", ax=ax)
            ax.set_title("Target Distribution")
            st.pyplot(fig)

        with g2:
            fig2, ax2 = plt.subplots()
            ax2.hist(df["age"], bins=20)
            ax2.set_title("Age Distribution")
            st.pyplot(fig2)
    else:
        st.error("data/heart.csv not found. Run python generate_data.py first.")

# ---------------- PAGE 6 ----------------
if page == "6. Model Performance":
    title("📈 Model Performance", "Accuracy, comparison and confusion matrix")

    acc = bundle["accuracy"] * 100
    cm = bundle["confusion_matrix"]

    st.markdown(f"<div class='red-card'><h3>Random Forest Accuracy</h3><h1>{acc:.2f}%</h1></div>", unsafe_allow_html=True)

    st.subheader("Model Comparison")
    results = compare_models()
    st.dataframe(results, use_container_width=True)

    fig, ax = plt.subplots()
    ax.bar(results["Model"], results["Accuracy"])
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Model Accuracy Comparison")
    st.pyplot(fig)

    st.subheader("Confusion Matrix")
    st.table(pd.DataFrame(cm, columns=["Predicted Low", "Predicted High"], index=["Actual Low", "Actual High"]))

# ---------------- PAGE 7 ----------------
if page == "7. Patient Report":
    title("📄 Patient Report Generator", "Create a sample patient report for documentation")

    name = st.text_input("Patient Name", "Gyanendra Chaudhary")
    pid = st.text_input("Patient ID", "P001")
    age = st.number_input("Age", 20, 90, 45)
    bp = st.number_input("Blood Pressure", 80, 220, 130)
    chol = st.number_input("Cholesterol", 100, 450, 220)
    result = st.selectbox("Prediction Result", ["Low Risk", "High Risk"])
    risk = st.slider("Risk Probability", 0, 100, 55)

    if st.button("Generate Report"):
        report = {
            "Patient Name": name,
            "Patient ID": pid,
            "Age": age,
            "Blood Pressure": bp,
            "Cholesterol": chol,
            "Prediction Result": result,
            "Risk Probability": f"{risk}%"
        }
        st.table(pd.DataFrame(report.items(), columns=["Field", "Value"]))
        st.download_button(
            "Download Report CSV",
            data=pd.DataFrame([report]).to_csv(index=False).encode("utf-8"),
            file_name="patient_report.csv",
            mime="text/csv"
        )

# ---------------- PAGE 8 ----------------
if page == "8. System Architecture":
    title("🧩 System Architecture", "Complete architecture of the project")

    st.markdown("""
    <div class="card">
    <h2>Architecture Flow</h2>
    <h3>Patient Input → Data Preprocessing → NLP Processing → Feature Combination → Random Forest Model → Prediction Output → Report Generation</h3>
    </div>
    """, unsafe_allow_html=True)

    st.code("""
User
  ↓
Patient Input Form
  ↓
Structured Data + Symptom Text
  ↓
Data Preprocessing
  ↓
TF-IDF NLP Vectorization
  ↓
Feature Combination
  ↓
Random Forest Classifier
  ↓
Risk Prediction
  ↓
Recommendation + Report
""")

# ---------------- PAGE 9 ----------------
if page == "9. Methodology":
    title("⚙️ Proposed Methodology", "Step-by-step project working")

    st.markdown("""
    <div class="card">
    <h2>1. Dataset Collection</h2>
    <p>Healthcare dataset is collected in CSV format.</p>
    <h2>2. Data Preprocessing</h2>
    <p>Data is cleaned, scaled and prepared for training.</p>
    <h2>3. NLP Processing</h2>
    <p>Patient symptom text is converted into numerical features using TF-IDF.</p>
    <h2>4. Feature Combination</h2>
    <p>Medical values and NLP features are merged.</p>
    <h2>5. Model Training</h2>
    <p>Random Forest classifier is trained for prediction.</p>
    <h2>6. Prediction Output</h2>
    <p>The system shows risk level, probability and recommendation.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- PAGE 10 ----------------
if page == "10. Conclusion & Future Work":
    title("✅ Conclusion & Future Work", "Final summary of the project")

    st.markdown("""
    <div class="card">
    <h2>Conclusion</h2>
    <p>
    This project successfully demonstrates a hybrid healthcare prediction system using
    Machine Learning and Natural Language Processing. It predicts heart disease risk using
    structured patient data and symptom text.
    </p>

    <h2>Future Work</h2>
    <ul>
        <li>Use real hospital datasets</li>
        <li>Add doctor login system</li>
        <li>Add patient history database</li>
        <li>Use BERT-based advanced NLP</li>
        <li>Deploy on cloud</li>
        <li>Create Android app version</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.caption("Disclaimer: This project is for academic and educational purposes only.")