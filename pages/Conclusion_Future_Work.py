import streamlit as st
from utils import apply_theme, header, sidebar_info

st.set_page_config(page_title="Conclusion", page_icon="✅", layout="wide")
apply_theme()
sidebar_info()

header("✅ Conclusion & Future Work", "Final summary and future improvements of the project.")

st.markdown("""
<div class="card">
<h2>Conclusion</h2>
<p>
The project Heart Disease Prediction Using Hybrid NLP successfully demonstrates the integration of
Machine Learning and Natural Language Processing for intelligent healthcare prediction. The system
analyzes structured medical data and symptom text to predict heart disease risk.
</p>

<h2>Major Achievements</h2>
<ul>
    <li>Developed a professional multi-page Streamlit dashboard.</li>
    <li>Implemented Random Forest based prediction model.</li>
    <li>Integrated NLP symptom analysis using TF-IDF.</li>
    <li>Added EDA, model performance, patient report, and methodology pages.</li>
    <li>Created a final-year level healthcare AI demonstration project.</li>
</ul>

<h2>Future Work</h2>
<ul>
    <li>Integration with real hospital datasets.</li>
    <li>Advanced NLP models like BERT.</li>
    <li>Cloud deployment.</li>
    <li>Mobile application version.</li>
    <li>Doctor login and patient history management.</li>
    <li>Integration with wearable devices.</li>
</ul>
</div>
""", unsafe_allow_html=True)