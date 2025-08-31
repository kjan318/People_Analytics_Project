import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Kieso Jan's Portfolio",
    page_icon="🧊",
    layout="wide",
)

# --- FUNCTION TO LOAD EXTERNAL CSS ---
def load_css(file_name):
    """Loads an external CSS file into the Streamlit app."""
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the "Glossy-touch" style
load_css("style.css")


# --- SIDEBAR ---
with st.sidebar:
    st.title("🧊 Contact & Links")
    st.write("Connect with me for collaborations or just a friendly chat about data!")
    st.divider()
    st.markdown(
        """
        - **Email:** [kieso.jan@gmail.com](mailto:kieso.jan@gmail.com)
        - **LinkedIn:** [linkedin.com/in/kieso-jan](https://www.linkedin.com/in/kieso-jan-688a594)
        - **GitHub:** [github.com/kjan318](https://github.com/kjan318/Data-INSIGHTS-Lab/)
        """
    )

# --- HERO SECTION ---
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.title("Kieso Jan: People Analytics & Data Science")
st.write(
    """
    Welcome to my portfolio! I specialize in transforming complex HR data into actionable, strategic insights. 
    This page showcases my flagship project: a comprehensive People Analytics dashboard built from the ground up.
    """
)
st.markdown('</div>', unsafe_allow_html=True)


# --- PROJECT SHOWCASE in a single glass container ---
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.header("Featured Project: The People Analytics Dashboard")
st.divider()

# --- Use columns for a cleaner layout ---
col1, col2 = st.columns((2, 1))

with col1:
    st.image("dashboard_screenshot_03.png", caption="A glimpse of the main dashboard interface.")

with col2:
    st.subheader("Project Goal")
    st.write(
        "To build an end-to-end, portfolio-ready dashboard that tracks the entire employee lifecycle, "
        "from recruitment to retention, using a 100% free and open-source tech stack."
    )
    st.markdown(
        """
        - **Live Demo:** [Link to your deployed dashboard]
        - **Source Code:** [Link to your GitHub repo]
        """
    )

# --- KEY FEATURES ---
st.subheader("Key Features & Capabilities")

with st.expander("📊 Interactive KPI Dashboard"):
    st.write(
        "The dashboard visualizes both lagging and leading indicators, allowing stakeholders to "
        "understand past performance and anticipate future trends. Filters allow for deep dives into specific departments or locations."
    )

with st.expander("🤖 Predictive Turnover Model"):
    st.write(
        "Using a machine learning model (Random Forest Classifier) built with Scikit-learn, the dashboard "
        "scores each active employee on their risk of turnover. This shifts the HR function from reactive to proactive."
    )
    st.code(
        """
# A simplified look at the prediction logic
import joblib

model = joblib.load('turnover_model.pkl')
features = current_employees[['Tenure', 'Performance_Rating', 'eNPS_Score']]
risk_scores = model.predict_proba(features)[:, 1]
        """,
        language="python"
    )

with st.expander("💡 Prescriptive Action Recommendations"):
    st.write(
        "The application doesn't just predict risk; it recommends actions. Based on the key drivers of an employee's "
        "risk score, it provides managers with data-driven suggestions to improve engagement and retention."
    )

# --- TECH STACK ---
st.subheader("Technology Stack")
st.write(
    "This project was built using a modern, cost-effective stack perfect for agile data science projects:"
)
st.markdown(
    """
    - **Python:** The core language for all data processing and modeling.
    - **Streamlit:** For building the interactive web application.
    - **Pandas:** For data manipulation and ETL.
    - **Scikit-learn:** For training the predictive turnover model.
    - **Plotly:** For creating interactive data visualizations.
    - **Google Sheets:** Used as a free, serverless database via its API.
    """
)
st.divider()
# --- CHALLENGES & LESSONS ---
st.subheader("Challenges & Lessons Learned")
st.write(
    "A key part of this project was overcoming common real-world challenges. The most significant was solving the infamous "
    "Google API `PermissionError`. This taught me a valuable lesson in cloud security: **authentication is not authorization**. "
    "The fix involved treating the Service Account as a 'user' and explicitly sharing the Google Sheet with its unique client email, a crucial step for any developer working with Google's ecosystem."
)

st.markdown('</div>', unsafe_allow_html=True)
