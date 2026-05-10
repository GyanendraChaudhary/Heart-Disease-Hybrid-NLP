import streamlit as st
from utils import apply_theme, header, sidebar_info

st.set_page_config(page_title="Methodology", page_icon="⚙️", layout="wide")
apply_theme()
sidebar_info()

header("⚙️ Proposed Methodology", "Step-by-step working methodology of the final year project.")

st.markdown("""
<div class="card">
<h2>1. Dataset Collection</h2>
<p>Healthcare dataset is collected in CSV format containing patient medical parameters and disease labels.</p>

<h2>2. Data Preprocessing</h2>
<p>Missing values, noisy data and numerical scaling are handled before training the model.</p>

<h2>3. NLP Processing</h2>
<p>Symptoms written in natural language are transformed using TF-IDF vectorization.</p>

<h2>4. Feature Combination</h2>
<p>Structured medical values and NLP features are combined into a hybrid feature set.</p>

<h2>5. Model Training</h2>
<p>Random Forest classifier is trained on hybrid features for heart disease prediction.</p>

<h2>6. Prediction and Recommendation</h2>
<p>The system predicts risk level and provides health recommendations through Streamlit interface.</p>
</div>
""", unsafe_allow_html=True)