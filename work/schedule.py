from concurrent.futures import thread
from zoneinfo import ZoneInfo
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time


def test():
    print(f"{str(datetime.now())}: OK")


scheduler = BackgroundScheduler(timezone=ZoneInfo("Asia/Tokyo"))
# scheduler = BackgroundScheduler(timezone=ZoneInfo("UTC"))
scheduler.add_job(test, 'cron', hour='23', minute='*/1')
scheduler.start()

time.sleep(10000)
