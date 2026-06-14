import telebot

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    print("Chat ID:", message.chat.id)
    bot.reply_to(message, f"Chat ID: {message.chat.id}")

bot.infinity_polling()