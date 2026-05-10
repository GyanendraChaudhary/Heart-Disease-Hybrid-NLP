import streamlit as st
import pandas as pd
from datetime import date
from utils import apply_theme, header, sidebar_info

st.set_page_config(page_title="Patient Report", page_icon="📄", layout="wide")
apply_theme()
sidebar_info()

header("📄 Patient Report Generator", "Generate a clean patient summary report for project demonstration.")

name = st.text_input("Patient Name", "Gyanendra Chaudhary")
pid = st.text_input("Patient ID", "P001")
age = st.number_input("Age", 20, 90, 45)
bp = st.number_input("Blood Pressure", 80, 220, 130)
chol = st.number_input("Cholesterol", 100, 450, 220)
result = st.selectbox("Prediction Result", ["Low Risk", "High Risk"])
risk = st.slider("Risk Probability", 0, 100, 55)
report_date = st.date_input("Report Date", date.today())

if st.button("Generate Report"):
    report = {
        "Patient Name": name,
        "Patient ID": pid,
        "Age": age,
        "Blood Pressure": bp,
        "Cholesterol": chol,
        "Prediction Result": result,
        "Risk Probability": f"{risk}%",
        "Report Date": report_date
    }

    st.table(pd.DataFrame(report.items(), columns=["Field", "Value"]))

    st.download_button(
        "⬇️ Download Report CSV",
        data=pd.DataFrame([report]).to_csv(index=False).encode("utf-8"),
        file_name=f"{name.replace(' ', '_')}_report.csv",
        mime="text/csv"
    )