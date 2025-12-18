import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
if not api_key:
    st.error("❌ API key not found. Please check your .env file.")
else:
    genai.configure(api_key=api_key)

# App title
st.set_page_config(page_title="EV Chatbot & Range Predictor", page_icon="⚡")
st.title("⚡ EV Chatbot & Range Predictor powered by Gemini AI")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["🔋 EV Range Predictor", "💬 Chatbot"])

# --- EV RANGE PREDICTOR PAGE ---
if page == "🔋 EV Range Predictor":
    st.header("🔋 Electric Vehicle Range Prediction")

    battery_capacity = st.number_input("Enter battery capacity (kWh):", min_value=1.0)
    motor_efficiency = st.slider("Motor efficiency (%):", 60, 100, 90)
    avg_speed = st.number_input("Enter average speed (km/h):", min_value=10.0)
    energy_consumption = st.number_input("Enter energy consumption (Wh/km):", min_value=50.0, value=150.0)

    if st.button("Predict Range"):
        # Range prediction logic
        usable_energy = battery_capacity * (motor_efficiency / 100)
        predicted_range = (usable_energy * 1000) / energy_consumption
        st.success(f"🚗 Estimated Range: *{predicted_range:.2f} km*")

# --- GEMINI CHATBOT PAGE ---
elif page == "💬 Chatbot":
    st.header("💬 Ask anything about Electric Vehicles or Python code")

    user_input = st.text_input("Ask your question:")
    if st.button("Ask Gemini"):
        if not user_input.strip():
            st.warning("Please enter a question.")
        else:
            try:
                model = genai.GenerativeModel("models/gemini-2.0-flash")
                response = model.generate_content(user_input)
                st.write("🤖 *Gemini replied:*")
                st.write(response.text)

            except Exception as e:
                if "429" in str(e):
                    st.error("⚠️ API limit reached. Please wait or try with a new API key.")
                else:
                    st.error(f"❌ Something went wrong: {e}")