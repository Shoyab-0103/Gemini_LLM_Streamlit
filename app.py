from dotenv import load_dotenv
load_dotenv()  # Loading environment variables from .env file
import streamlit as st
import os
import google.generativeai as genai
from google.api_core.exceptions import NotFound

# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GENAI_API_KEY"))



# Function to load gemini pro model and get response
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        return model.generate_content(question).text
    except NotFound:
        return f"Model not found. Available models: {', '.join(model.name for model in genai.list_models())}"
    except Exception as e:
        return f"Error: {e}"
    


# Initialize the Streamlit app
st.set_page_config(page_title="Q & A Demo")

st.header("Gemini Application")

input_text = st.text_input("Enter your question here: ", key="input")

# Create one submit button
submit_button = st.button("Ask question")

if submit_button:
    # Get the response from the model
    response = get_gemini_response(input_text)
    st.write(response)

# Print response in terminal
    print("Response:", response)
