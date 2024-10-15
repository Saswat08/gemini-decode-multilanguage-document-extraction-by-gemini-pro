import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import time

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up page configurations
st.set_page_config(page_title="Multilanguage Document Extraction", page_icon="🌍", layout="wide")

# Adding custom CSS for background image, animations, and styling
st.markdown("""
    <style>
    /* Apply the background image to the main content */
    .stApp {
        background-image: url('https://stock.adobe.com/in/search?k=website+background&asset_id=282446155');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Arial', sans-serif;
    }
    
    /* Styling for headers */
    .title {
        font-family: 'Arial Black', sans-serif;
        font-size: 3em;
        color: white;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    }
    
    .subtitle {
        font-family: 'Arial', sans-serif;
        color: #e0e0e0;
        text-align: center;
        margin-top: -10px;
        font-size: 1.2em;
        animation: fadeIn 2.5s ease-in-out;
    }
    
    /* Button animation */
    .stButton button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        animation: bounce 2s infinite;
    }
    
    /* Image styling */
    img.uploaded-image {
        border-radius: 10px;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
        width: 100%;
        max-width: 600px;
    }
    
    /* Fade-in animation */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    
    /* Bounce animation for button */
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    </style>
    """, unsafe_allow_html=True)

# Function to get Gemini AI response
def get_gemini_response(input_text, image, prompt):
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content([input_text, image, prompt])
    return response.text

# Header section with animation
st.markdown("<h1 class='title'>Multilanguage Document Extraction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Effortlessly decode documents across different languages</p>", unsafe_allow_html=True)

# File uploader section
uploaded_file = st.file_uploader("Choose an image of the document", type=["jpg", "jpeg", "png"])
image = None

# Display uploaded image with custom CSS using st.markdown
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_path = f"data:image/png;base64,{st.image(image, use_column_width=True)}"
    st.markdown(f'<img src="{img_path}" class="uploaded-image">', unsafe_allow_html=True)

# Submit button with animation
submit = st.button("Tell me about the document")
input_prompt = """You are an expert in understanding invoices.
We will upload an image as an invoice and you will have to answer the question based on the uploaded invoice image.
"""

# Custom description with styled text
text = """Utilizing Gemini pro AI, this project efficiently extracts vital information from diverse multilingual documents, transcending language barriers with precision."""
styled_text = f"<span style='font-family:serif; color: #e0e0e0;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

# Response handling with loading spinner
if submit:
    if image is not None:
        with st.spinner("Analyzing the document... Please wait."):
            time.sleep(2)  # Simulate loading time
            response = get_gemini_response(input_prompt, image, "")
            st.subheader("The response is:")
            st.success(response)
    else:
        st.warning("Please upload an image before submitting.")
