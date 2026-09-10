from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TELEGRAM_TOKEN = "8945246268:AAGt1ah2UKvXz__cWJ_BH6QnrAMrCZzqsF8"  
CHAT_ID = 

TELEGRAM_TOKEN = os.getenv(TELEGRAM_TOKEN)
CHAT_ID = os.getenv("CHAT_ID")  # رقم المحادثة أو الجروب

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message", {}).get("text", "")
    if message:
        reply = f"إنت كتبت: {message}"
        send_message(reply)
    return {"status": "ok"}
