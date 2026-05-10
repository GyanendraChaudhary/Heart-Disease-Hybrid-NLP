import streamlit as st
import pandas as pd

def apply_theme():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #06111f, #102542, #230b2e);
        color: white;
    }
    .hero {
        padding: 28px;
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(255,65,108,.22), rgba(29,38,113,.30));
        border: 1px solid rgba(255,255,255,.18);
        box-shadow: 0 12px 35px rgba(0,0,0,.35);
        text-align: center;
    }
    .hero h1 {
        font-size: 46px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 5px;
    }
    .hero p {
        font-size: 18px;
        color: #d6e2f0;
    }
    .card {
        background: rgba(255,255,255,.08);
        padding: 22px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,.16);
        box-shadow: 0 10px 30px rgba(0,0,0,.28);
    }
    .metric-card {
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        background: linear-gradient(135deg, #ff416c, #ff4b2b);
        color: white;
        font-weight: bold;
    }
    .success-card {
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        background: linear-gradient(135deg, #11998e, #38ef7d);
        color: white;
        font-weight: bold;
    }
    .blue-card {
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        background: linear-gradient(135deg, #1d2671, #0f9bff);
        color: white;
        font-weight: bold;
    }
    .stButton>button {
        background: linear-gradient(135deg, #ff416c, #ff4b2b);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 17px;
        font-weight: 800;
        width: 100%;
    }
    [data-testid="stSidebar"] {
        background: #06111f;
    }
    </style>
    """, unsafe_allow_html=True)

def header(title, subtitle):
    st.markdown(f"""
    <div class="hero">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

def sidebar_info():
    import config
    st.sidebar.title("❤️ Project Menu")
    st.sidebar.write(f"**Project:** {config.APP_NAME}")
    st.sidebar.write(f"**Author:** {config.AUTHOR}")
    st.sidebar.write(f"**Version:** {config.VERSION}")
    st.sidebar.write("**Frontend:** Streamlit")
    st.sidebar.write("**Backend:** Python")
    st.sidebar.write("**ML:** Random Forest")
    st.sidebar.write("**NLP:** TF-IDF")

def load_dataset():
    return pd.read_csv("data/heart.csv")

def recommendation(pred):
    if pred == 1:
        return [
            "Consult a cardiologist as soon as possible.",
            "Monitor blood pressure and cholesterol regularly.",
            "Avoid smoking, junk food, and excessive stress.",
            "Follow a balanced diet and daily physical activity.",
            "This tool is for educational use, not final medical diagnosis."
        ]
    return [
        "Current input shows lower heart disease risk.",
        "Continue regular exercise and balanced diet.",
        "Go for routine health checkups.",
        "Maintain healthy cholesterol and blood pressure levels.",
        "This tool is for educational use, not final medical diagnosis."
    ]