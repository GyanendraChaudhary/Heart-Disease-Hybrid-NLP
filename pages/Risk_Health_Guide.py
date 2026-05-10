import streamlit as st
from utils import apply_theme, header, sidebar_info

st.set_page_config(page_title="Risk Health Guide", page_icon="🏥", layout="wide")
apply_theme()
sidebar_info()

header("🏥 Risk Health Guide", "Educational health guidance for heart disease awareness.")

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="card">
    <h2>⚠️ High Risk Indicators</h2>
    <ul>
        <li>High blood pressure</li>
        <li>High cholesterol</li>
        <li>Severe chest pain</li>
        <li>Shortness of breath</li>
        <li>Irregular heartbeat</li>
        <li>Diabetes and obesity</li>
        <li>Smoking and stress</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h2>✅ Healthy Habits</h2>
    <ul>
        <li>Daily walking or exercise</li>
        <li>Balanced diet</li>
        <li>Low salt and low fat food</li>
        <li>Regular health checkups</li>
        <li>Avoid smoking and alcohol</li>
        <li>Control stress and sleep properly</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.warning("Disclaimer: This guide is for educational purposes only. Always consult a doctor for medical diagnosis.")