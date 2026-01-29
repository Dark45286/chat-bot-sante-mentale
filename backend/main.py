from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

# ====================
# CONFIG
# ====================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# ====================
# FASTAPI
# ====================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ====================
# SCHEMA
# ====================
class ChatRequest(BaseModel):
    message: str

# ====================
# ROUTES
# ====================
@app.get("/")
def root():
    return {"status": "Backend Groq OK"}

@app.post("/chat")
def chat(data: ChatRequest):

    if not GROQ_API_KEY:
        return {
            "reply": "⚠️ Clé API manquante côté serveur."
        }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "Tu es un assistant empathique spécialisé en santé mentale."},
            {"role": "user", "content": data.message}
        ],
        "temperature": 0.7,
        "max_tokens": 200
    }

    try:
        r = requests.post(GROQ_URL, headers=headers, json=payload, timeout=20)
        r.raise_for_status()
        result = r.json()
        reply = result["choices"][0]["message"]["content"]
        return {"reply": reply}

    except Exception as e:
        print("❌ Erreur Groq :", e)
        return {
            "reply": "⚠️ Erreur technique temporaire. Réessaie dans quelques instants."
        }
