import os
import streamlit as st
from google import genai
from google.genai import types

# 1. API கீயை பாதுகாப்பாக எடுப்பது (Streamlit Cloud & Local இரண்டிற்கும் வேலை செய்யும்)
api_key = None
try:
    api_key = st.secrets.get("GEMINI_API_KEY")
except Exception:
    pass

if not api_key:
    api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def read_my_notes() -> str:
    """Reads service pricing, poster details, resume packages, and website info from notes.txt file."""
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def calculate_discount(price: float, discount_percentage: float) -> str:
    """Calculates the final price after applying a percentage discount."""
    final_price = price - (price * (discount_percentage / 100))
    return f"The final price after a {discount_percentage}% discount is ₹{final_price:.2f}"

# சாட் செட்டப்
chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are an official business consultant for Zynvix Studio. Always use tools to check local service notes and perform exact discount calculations in INR.",
        tools=[read_my_notes, calculate_discount],
    )
)

print("=== ZYNVIX AGENT READY ===")
print("(Type 'exit' or 'quit' to end the chat)")
while True:
    user_query = input("You: ")
    
    if user_query.lower().strip() in ["exit", "quit"]:
        print("\nZynvix Agent: Thank you for reaching out to Zynvix Studio! Have a great day!")
        break
        
    if not user_query.strip():
        continue

    response = chat.send_message(user_query)
    
    print(f"\nZynvix Agent: {response.text}\n")
    print("-" * 50)