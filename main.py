import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise RuntimeError("Set BOT_TOKEN and CHAT_ID in Railway Variables")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_message(CHAT_ID, "✅ البوت اشتغل على Railway (نسخة تجريبية).")

print("✅ Running minimal bot on Railway…")
bot.polling()
