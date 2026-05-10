import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import apply_theme, header, sidebar_info
from model import load_or_train_model, compare_models

st.set_page_config(page_title="Model Performance", page_icon="📈", layout="wide")
apply_theme()
sidebar_info()

header("📈 Model Performance", "Evaluate machine learning models and prediction accuracy.")

bundle = load_or_train_model()
accuracy = bundle["accuracy"] * 100
cm = bundle["confusion_matrix"]

st.markdown(f'<div class="metric-card">Random Forest Accuracy<br><h1>{accuracy:.2f}%</h1></div>', unsafe_allow_html=True)

st.write("")
st.subheader("Model Comparison")
results = compare_models()
st.dataframe(results, use_container_width=True)

fig, ax = plt.subplots()
ax.bar(results["Model"], results["Accuracy"])
ax.set_ylabel("Accuracy (%)")
ax.set_title("Machine Learning Model Accuracy Comparison")
plt.xticks(rotation=15)
st.pyplot(fig)

st.subheader("Confusion Matrix")
cm_df = pd.DataFrame(cm, columns=["Predicted Low", "Predicted High"], index=["Actual Low", "Actual High"])
st.table(cm_df)

st.info("Random Forest is selected because it gives better stability, handles complex data, and reduces overfitting.")