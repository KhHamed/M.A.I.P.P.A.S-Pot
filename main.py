import os
import requests
from dotenv import load_dotenv
from flask import Flask, request

# تحميل القيم من ملف .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        # هنا البوت بيحلل الكلام ويرد
        if "سلام" in text:
            reply = "وعليكم السلام ورحمة الله 🌸"
        elif "ازيك" in text:
            reply = "الحمد لله تمام، وانت عامل ايه؟ 😎"
        else:
            reply = f"إنت قلت: {text}"
        
        send_message(chat_id, reply)
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
