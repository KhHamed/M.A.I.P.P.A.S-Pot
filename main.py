import os
import requests
from fastapi import FastAPI, Request
from dotenv import load_dotenv

# تحميل القيم من ملف .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = FastAPI()

def send_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=payload)
    return response.json()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message", {}).get("text", "")
    if message:
        reply = f"إنت كتبت: {message}"
        send_message(reply)
    return {"status": "ok"}

@app.get("/")
def home():
    return {"message": "Telegram Bot Webhook شغال ✅"}
