import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from PIL import Image

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("models/gemini-2.5-flash")

st.title("🤖 Multimodal Chatbot")

# Text input
user_input = st.text_input("Type your message")

# File upload
uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

# -------- TEXT CHAT --------
if user_input:
    response = model.generate_content(user_input)
    st.write("🤖 Bot:", response.text)

# -------- PDF CHAT --------
if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":
        pdf_reader = PdfReader(uploaded_file)
        pdf_text = ""

        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

        st.success("PDF uploaded!")

        question = st.text_input("Ask about the PDF")

        if question:
            prompt = f"""
            Document:
            {pdf_text}

            Question:
            {question}
            """

            response = model.generate_content(prompt)
            st.write("🤖 PDF Answer:", response.text)

# -------- IMAGE CHAT --------
    elif uploaded_file.type.startswith("image"):
        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image")

        prompt = st.text_input("Ask about the image")

        if prompt:
            response = model.generate_content([prompt, image])
            st.write("🤖 Image Answer:", response.text)