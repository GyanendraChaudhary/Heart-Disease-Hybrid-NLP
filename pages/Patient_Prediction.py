import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

from utils import apply_theme, header, sidebar_info, recommendation
from model import predict_risk

st.set_page_config(page_title="Patient Prediction", page_icon="🧾", layout="wide")
apply_theme()
sidebar_info()

header("🧾 Patient Heart Risk Prediction", "Enter patient details and get real-time AI-based heart disease risk prediction.")

left, right = st.columns([1.3, 1])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👤 Patient Profile")

    a, b = st.columns(2)
    with a:
        patient_name = st.text_input("Patient Name", "Gyanendra Chaudhary")
        patient_id = st.text_input("Patient ID", "P001")
        contact = st.text_input("Contact Number", "9876543210")
    with b:
        city = st.text_input("City", "Greater Noida")
        checkup_date = st.date_input("Checkup Date", date.today())
        lifestyle = st.selectbox("Lifestyle", ["Active", "Moderate", "Sedentary"])

    st.subheader("❤️ Medical Details")
    c1, c2 = st.columns(2)
    with c1:
        age = st.slider("Age", 20, 90, 45)
        bp = st.slider("Resting Blood Pressure", 80, 220, 130)
        chol = st.slider("Cholesterol Level", 100, 450, 220)
    with c2:
        heart_rate = st.slider("Maximum Heart Rate", 60, 220, 150)
        gender = st.selectbox("Gender", ["Male", "Female"])
        chest_pain = st.selectbox("Chest Pain Type", ["None", "Mild", "Moderate", "Severe"])

    symptoms = st.text_area("Symptoms / Clinical Notes", "chest pain, fatigue, shortness of breath")
    btn = st.button("🔍 Predict Risk")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Input Summary")
    st.table(pd.DataFrame({
        "Field": ["Name", "Age", "Gender", "BP", "Cholesterol", "Heart Rate", "Chest Pain", "Lifestyle"],
        "Value": [patient_name, age, gender, bp, chol, heart_rate, chest_pain, lifestyle]
    }))
    st.markdown('</div>', unsafe_allow_html=True)

if btn:
    pred, prob = predict_risk(age, gender, chest_pain, bp, chol, heart_rate, symptoms)

    st.markdown("---")
    st.subheader("🧠 AI Prediction Result")

    r1, r2, r3 = st.columns(3)

    with r1:
        if pred == 1:
            st.markdown('<div class="metric-card"><h3>Risk Status</h3><h1>HIGH RISK</h1></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="success-card"><h3>Risk Status</h3><h1>LOW RISK</h1></div>', unsafe_allow_html=True)

    with r2:
        st.markdown(f'<div class="blue-card"><h3>Risk Probability</h3><h1>{prob:.2f}%</h1></div>', unsafe_allow_html=True)

    with r3:
        confidence = "Strong" if prob > 70 else "Moderate" if prob > 40 else "Low"
        st.markdown(f'<div class="blue-card"><h3>Confidence</h3><h1>{confidence}</h1></div>', unsafe_allow_html=True)

    g1, g2 = st.columns(2)

    with g1:
        fig, ax = plt.subplots()
        ax.barh(["Risk Score"], [prob])
        ax.set_xlim(0, 100)
        ax.set_title("Heart Disease Risk Score")
        st.pyplot(fig)

    with g2:
        vals = [age/90*100, bp/220*100, chol/450*100, heart_rate/220*100, min(len(symptoms)*2, 100)]
        fig2, ax2 = plt.subplots()
        ax2.bar(["Age", "BP", "Chol", "HR", "Text"], vals)
        ax2.set_title("Feature Impact Overview")
        st.pyplot(fig2)

    st.subheader("📄 Patient Report")
    report = {
        "Patient Name": patient_name,
        "Patient ID": patient_id,
        "Contact": contact,
        "City": city,
        "Date": checkup_date,
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

    st.table(pd.DataFrame(report.items(), columns=["Field", "Value"]))

    st.download_button(
        "⬇️ Download Patient Report CSV",
        data=pd.DataFrame([report]).to_csv(index=False).encode("utf-8"),
        file_name=f"{patient_name.replace(' ', '_')}_heart_report.csv",
        mime="text/csv"
    )

    st.subheader("✅ Recommendations")
    for item in recommendation(pred):
        st.write("•", item)