import sqlite3

conn = sqlite3.connect("jobs.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY,
    company TEXT,
    title TEXT,
    url TEXT
)
""")

conn.commit()
conn.close()

print("Database ready")