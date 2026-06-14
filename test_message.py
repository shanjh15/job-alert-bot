import telebot

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
CHAT_ID = 8619680369

bot = telebot.TeleBot(TOKEN)

bot.send_message(
    CHAT_ID,
    "🚀 First automated message from Python"
)

print("Message sent!")