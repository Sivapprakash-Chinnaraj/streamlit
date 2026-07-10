import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Sivapprakash's Cloud & Data Hub",
    page_icon="⚡",
    layout="wide"
)

# --- HEADER SECTION ---
st.title("🏴‍☠️ Cloud & Data Science Portfolio Dashboard")
st.subheader("Deployed Live on AWS EC2 via Ubuntu Linux CLI")
st.markdown("---")

# --- SIDEBAR NAV ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to Project Demo:", ["Home & About", "One Piece Bounty Tracker", "Interactive ML Model"])

# --- PAGE 1: HOME ---
if page == "Home & About":
    st.header("👋 Welcome to My Streamlit App!")
    st.write(
        "This application serves as a live proof-of-concept demonstrating "
        "how Python data scripts can be seamlessly containerized and deployed "
        "to a cloud environment using AWS infrastructure, custom Security Groups, and Nginx."
    )
    
    st.info("💡 **DevOps Tip:** This app is currently running on Port 8501 inside an isolated Ubuntu instance!")

# --- PAGE 2: DATA TAB (ONE PIECE) ---
elif page == "One Piece Bounty Tracker":
    st.header("📊 Straw Hat Pirates Bounty Analytics")
    st.write("Filtering and analyzing character data dynamically using Pandas.")

    # Create a mock dataset based on your HTML project
    data = {
        "Character": ["Luffy", "Zoro", "Sanji", "Booby Robin", "Usopp", "Booby Nami", "Chopper"],
        "Role": ["Captain", "Swordsman", "Chef", "Archaeologist", "Sniper", "Navigator", "Doctor"],
        "Bounty (Berries)": [3000000000, 1111000000, 1032000000, 930000000, 500000000, 366000000, 1000]
    }
    df = pd.DataFrame(data)

    # Interactive Filter Sidebar/Widget
    min_bounty = st.slider("Filter by Minimum Bounty (Berries):", 0, 3500000000, 100000000, step=50000000)
    filtered_df = df[df["Bounty (Berries)"] >= min_bounty]

    # Layout Columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Filtered Dataset")
        st.dataframe(filtered_df, use_container_width=True)
        
    with col2:
        st.subheader("Bounty Distribution Chart")
        st.bar_chart(filtered_df.set_index("Character")["Bounty (Berries)"])

# --- PAGE 3: ML PREDICTOR ---
elif page == "Interactive ML Model":
    st.header("🤖 Live Interactive Prediction Simulator")
    st.write("Input custom parameters below to see how a model calculates outputs in real-time.")

    # Simulate inputs for a model (e.g., predicting cloud infrastructure hosting costs)
    st.subheader("Configure Environment Variables")
    
    servers = st.number_input("Number of EC2 Instances:", min_value=1, max_value=100, value=3)
    storage = st.slider("Total S3 Storage Needed (GB):", 10, 5000, 250)
    traffic_load = st.selectbox("Expected Traffic Load:", ["Low", "Medium", "High", "Critical"])

    # Basic simulation logic
    base_cost = servers * 15 + (storage * 0.023)
    multiplier = {"Low": 1.0, "Medium": 1.2, "High": 1.5, "Critical": 2.0}[traffic_load]
    predicted_cost = round(base_cost * multiplier, 2)

    st.markdown("---")
    st.metric(label="Predicted Monthly Cloud Operational Cost", value=f"${predicted_cost}")
    st.success("Mathematical simulation executed successfully. Ready to bind to a live Scikit-Learn or TensorFlow pickle file!")

# --- FOOTER ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Python | Powered by Amazon Web Services")
