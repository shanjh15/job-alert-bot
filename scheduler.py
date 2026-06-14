from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
from datetime import datetime

scheduler = BlockingScheduler()

def run_notifier():
    print(f"Running notifier at {datetime.now()}")

    subprocess.run(
        ["python", "job_notifier.py"]
    )

scheduler.add_job(
    run_notifier,
    "interval",
    minutes=10
)

print("Scheduler started...")

scheduler.start()