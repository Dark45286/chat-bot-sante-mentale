import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-3.1-8b-instant",  # modèle Groq réel
    "messages": [
        {"role": "user", "content": "Salut, comment vas-tu ?"}
    ],
    "temperature": 0.7,
    "max_tokens": 150
}

try:
    r = requests.post(URL, headers=headers, json=payload, timeout=15)
    print("Status:", r.status_code)
    print("Body:", r.text)
except Exception as e:
    print("Erreur:", e)
