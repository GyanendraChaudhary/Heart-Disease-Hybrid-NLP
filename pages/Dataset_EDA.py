import streamlit as st
import matplotlib.pyplot as plt
from utils import apply_theme, header, sidebar_info, load_dataset

st.set_page_config(page_title="Dataset EDA", page_icon="📊", layout="wide")
apply_theme()
sidebar_info()

header("📊 Dataset & EDA", "Explore dataset structure, distributions, and basic health data analysis.")

df = load_dataset()

st.subheader("Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="metric-card">Total Records<br><h2>{len(df)}</h2></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="blue-card">Features<br><h2>{len(df.columns)-1}</h2></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="metric-card">Target Classes<br><h2>{df["target"].nunique()}</h2></div>', unsafe_allow_html=True)

st.write("")
st.subheader("Dataset Statistical Summary")
st.dataframe(df.describe(), use_container_width=True)

g1, g2 = st.columns(2)

with g1:
    st.subheader("Target Distribution")
    fig, ax = plt.subplots()
    df["target"].value_counts().plot(kind="bar", ax=ax)
    ax.set_xticklabels(["Low Risk", "High Risk"], rotation=0)
    ax.set_ylabel("Count")
    st.pyplot(fig)

with g2:
    st.subheader("Age Distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(df["age"], bins=20)
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Frequency")
    st.pyplot(fig2)

g3, g4 = st.columns(2)

with g3:
    st.subheader("Cholesterol Distribution")
    fig3, ax3 = plt.subplots()
    ax3.hist(df["chol"], bins=20)
    ax3.set_xlabel("Cholesterol")
    st.pyplot(fig3)

with g4:
    st.subheader("Blood Pressure Distribution")
    fig4, ax4 = plt.subplots()
    ax4.hist(df["trestbps"], bins=20)
    ax4.set_xlabel("Blood Pressure")
    st.pyplot(fig4)