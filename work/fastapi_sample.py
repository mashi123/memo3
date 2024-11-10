
from datetime import datetime
from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import uvicorn


def func():
    print(f"{str(datetime.now())}: OK caled")


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("sart")
    scheduler = BackgroundScheduler()
    scheduler.add_job(func, CronTrigger.from_crontab(
        '54 21 * * *', timezone='Asia/Tokyo'))
    scheduler.start()
    yield
    scheduler.shutdown()
    print("end")

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("fastapi_sample:app")
