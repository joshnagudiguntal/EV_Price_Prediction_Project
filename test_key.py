import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the key from .env file
load_dotenv()

# Get your Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check if the key loaded
if not api_key:
    print("❌ API key not found. Please check your .env file.")
else:
    print("✅ API key found successfully!")

# Try connecting to Gemini
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content("Hello Gemini!")
    print("✅ Connection successful! Gemini replied:")
    print(response.text)
except Exception as e:
    print("❌ Something went wrong:", e)