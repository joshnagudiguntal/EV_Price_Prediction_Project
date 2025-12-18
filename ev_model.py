import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel("models/gemini-2.0-flash")

def get_gemini_response(prompt):
    """Generate a response from Gemini"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"