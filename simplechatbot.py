import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose model
model = genai.GenerativeModel("models/gemini-2.5-flash")

def chat():
    print("🤖 Gemini Chatbot Ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            response = model.generate_content(user_input)
            print("Bot:", response.text)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()
