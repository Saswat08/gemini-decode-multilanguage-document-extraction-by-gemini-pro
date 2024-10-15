from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image, prompt):
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content([input_text, image, prompt])
    return response.text
st.set_page_config(page_title="Multilanguage Document Extraction")
st.header("Language Decode")
uploaded_file = st.file_uploader("Choose an image of the document", type=["jpg","jpeg","png"])
image = None
if uploaded_file is not None:
    Image = Image.open(uploaded_file)
    st.image(image, caption="Uploader Image", use_column_width = True)
submit = st.button("Tell me about the document")
input_prompt = """You are an expert in understanding invoices.
We will upload an image as an invoice and you will have to answer the question based on the uploaded invoice image.
"""
text = """Utilizing Gemini pro ai, this project effortlessly extracts vital information efficiently from diverse multilingual documents, transcending language barrier with precision."""
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)
if submit and image is not None:
    response = get_gemini_response(input_prompt, image, "")
    st.subheader("The response is") 
    st.write(response) 
else:
    if submit: 
     st.write("Please upload an image before submitting.")