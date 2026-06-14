import requests
import telebot

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
CHAT_ID = 8619680369

bot = telebot.TeleBot(TOKEN)

url = "https://boards-api.greenhouse.io/v1/boards/datadog/jobs"

data = requests.get(url).json()

job = data["jobs"][0]

message = f"""
🚀 New Job Found

Title: {job['title']}

Apply:
{job['absolute_url']}
"""

bot.send_message(CHAT_ID, message)

print("Job sent!")