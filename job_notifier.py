import sqlite3
import requests
import telebot

from config import (
    GREENHOUSE_COMPANIES,
    INCLUDE_KEYWORDS,
    EXCLUDE_KEYWORDS
)

from scrapers.greenhouse import fetch_greenhouse_jobs
from filters.role_filter import is_matching_role

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
CHAT_ID = 8619680369

bot = telebot.TeleBot(TOKEN)

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY
)
""")

for company in GREENHOUSE_COMPANIES:

    jobs = fetch_greenhouse_jobs(company)

    for job in jobs:

        title = job["title"]

        if not is_matching_role(
            title,
            INCLUDE_KEYWORDS,
            EXCLUDE_KEYWORDS
        ):
            continue

        job_id = job["id"]

        cursor.execute(
            "SELECT job_id FROM jobs WHERE job_id=?",
            (job_id,)
        )

        exists = cursor.fetchone()

        if exists:
            continue

        message = f"""
🚀 SDE Match Found

Company: {company}

Role:
{title}

Apply:
{job['absolute_url']}
"""

        bot.send_message(CHAT_ID, message)

        cursor.execute(
            "INSERT INTO jobs(job_id) VALUES(?)",
            (job_id,)
        )

        conn.commit()

        print("Sent:", title)

conn.close()

print(f"Checked {company}: {len(jobs)} jobs")