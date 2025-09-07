import os, requests, time

# قراءة التوكن والـ chat id من Railway Secrets
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": text})

if name == "__main__":
    if not TOKEN or not CHAT_ID:
        raise RuntimeError("❌ ناقص TELEGRAM_BOT_TOKEN أو CHAT_ID في Railway")
    send("✅ البوت اشتغل على Railway يا عبدالله!")
    # نخلي البوت يفضل شغال
    while True:
        time.sleep(3600)
