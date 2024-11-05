from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time


def func():
    print(f"{str(datetime.now())}: OK")


# scheduler = BackgroundScheduler(timezone=ZoneInfo("Asia/Tokyo"))
# scheduler = BackgroundScheduler(timezone=ZoneInfo("UTC"))
scheduler = BackgroundScheduler()
# scheduler.add_job(func, 'cron', hour='23', minute='*/1')
scheduler.add_job(func, CronTrigger.from_crontab(
    '50 22 * * *', timezone='Asia/Tokyo'))
scheduler.start()

time.sleep(10000)
