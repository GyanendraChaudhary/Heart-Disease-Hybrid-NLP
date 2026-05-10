import streamlit as st
from utils import apply_theme, header, sidebar_info

st.set_page_config(page_title="System Architecture", page_icon="🧩", layout="wide")
apply_theme()
sidebar_info()

header("🧩 System Architecture", "Complete architecture of the hybrid AI heart disease prediction system.")

st.markdown("""
<div class="card">
<h2>Architecture Flow</h2>
<h3>
Patient Input → Data Preprocessing → NLP Processing → Feature Combination → Random Forest Model → Prediction Output → Report Generation
</h3>
</div>
""", unsafe_allow_html=True)

st.write("")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="metric-card"><h3>Frontend Layer</h3><p>Streamlit UI, patient forms, charts, reports</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="blue-card"><h3>Backend Layer</h3><p>Python processing, model loading, prediction logic</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric-card"><h3>AI Layer</h3><p>TF-IDF NLP + Random Forest ML classifier</p></div>', unsafe_allow_html=True)

st.subheader("Data Flow Diagram")

st.code("""
User
  ↓
Patient Input Form
  ↓
Structured Data + Symptom Text
  ↓
Preprocessing Module
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