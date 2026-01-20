import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv(GEMINI_API_KEY="AIzaSyDqPO3A0Aq72eQDVihHl2y2lfmE-kphgLg"))

model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

def chat():
    print("🤖 Gemini Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            response = model.generate_content(user_input)
            print("Gemini:", response.text.strip())
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

def chat():
    print("🤖 Gemini Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            response = model.generate_content(user_input)
            print("Gemini:", response.text.strip())
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

def chat():
    print("🤖 Gemini Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            response = model.generate_content(user_input)
            print("Gemini:", response.text.strip())
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()