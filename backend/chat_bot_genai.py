import os
import google.generativeai as genai
from dotenv import load_dotenv

print("🚀 Démarrage du chatbot...")

# Charger .env
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY manquant dans .env")

print("🔑 API KEY chargée")

# Configuration Gemini
genai.configure(api_key=API_KEY)

# Modèle STABLE
model = genai.GenerativeModel("gemini-pro")

print("🤖 Modèle prêt")

def generate_reply(message: str) -> str:
    response = model.generate_content(
        f"""
Tu es un assistant calme, bienveillant et professionnel.
Réponds de façon claire, empathique et concise.

Utilisateur : {message}
"""
    )
    return response.text.strip()

# Boucle chatbot
print("\n=== Chatbot Gemini ===")
print("Tape un message (exit pour quitter)\n")

while True:
    user_input = input("User > ")
    if user_input.lower() == "exit":
        print("👋 Fin du chatbot")
        break

    try:
        reply = generate_reply(user_input)
        print("Bot >", reply)
    except Exception as e:
        print("❌ Erreur Gemini :", e)
