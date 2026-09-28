import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing. Create a .env file and add your key.")

client = genai.Client(api_key=API_KEY)

def generate(prompt: str) -> str:
    response = client.models.generate_content(model=MODEL, contents=prompt)
    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")
    return response.text.strip()
