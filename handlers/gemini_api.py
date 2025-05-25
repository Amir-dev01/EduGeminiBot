import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest')

def ask_gemini(prompt: str) -> str:
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Gemini API error: {e}")
