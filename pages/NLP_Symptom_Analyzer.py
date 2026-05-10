import streamlit as st
import pandas as pd
from utils import apply_theme, header, sidebar_info
from model import load_or_train_model

st.set_page_config(page_title="NLP Symptom Analyzer", page_icon="🧠", layout="wide")
apply_theme()
sidebar_info()

header("🧠 NLP Symptom Analyzer", "Analyze patient symptom text using TF-IDF based NLP processing.")

bundle = load_or_train_model()
vectorizer = bundle["vectorizer"]

text = st.text_area(
    "Enter symptom text",
    "chest pain, shortness of breath, fatigue, sweating, dizziness"
)

if st.button("Analyze Symptoms"):
    vec = vectorizer.transform([text])
    feature_names = vectorizer.get_feature_names_out()
    values = vec.toarray()[0]

    data = []
    for word, score in zip(feature_names, values):
        if score > 0:
            data.append({"Medical Term": word, "TF-IDF Score": round(score, 4)})

    st.subheader("Extracted NLP Features")
    if data:
        st.dataframe(pd.DataFrame(data), use_container_width=True)
    else:
        st.warning("No important medical term detected from current vocabulary.")

st.markdown("""
<div class="card">
<h3>How NLP Works in This Project</h3>
<p>
Natural Language Processing converts patient symptom text into numerical vectors.
The TF-IDF method gives importance score to medical words such as chest, pain, fatigue,
breath, dizziness and other symptom-related terms.
</p>
</div>
""", unsafe_allow_html=True)