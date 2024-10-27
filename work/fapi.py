import time
from fastapi import FastAPI
from numpy import record
import uvicorn
from uvicorn.config import LOGGING_CONFIG
import dtstore
import genlist
from datetime import datetime
from fastapi.responses import ORJSONResponse

app = FastAPI()
log_config = LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

dts = dtstore.Dtstore(100000, 100)


@app.get("/get")
async def read_num(num: int = 1):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    # datalist = dts.get2dlist()
    datalist = dts.getDataFrame().to_json(orient="records")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    return datalist
    # return ORJSONResponse(datalist)


uvicorn.run(app, log_config=log_config, host="0.0.0.0", port=8000)
