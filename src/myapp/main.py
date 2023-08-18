import time
import threading
import uvicorn
import schedule
import pandas as pd
from fastapi import FastAPI
from myapp.configs import app_config
from myapp.common.constants import MySettings
from myapp.endpoints import (
  version,
  foo_endpoint,
)
from myapp.controller import (
  foo_controller,
)

app = FastAPI (
  title = 'GKE Service Sample',
  description = 'This is a sample of GKE Service Code.'
)

app.include_router(version.api_router, tags=["Service Information"])
app.include_router(foo_endpoint.api_router, tags=["MyApp Services"])


def exec_foo():
  pass

def startup():
  schedule.every().day.at("01:00").do(exec_foo)
  
  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  threading.Thread(target=startup, daemon=True).start()
  uvicorn.run(
    app = "myapp.main:app",
    host = app_config["app"]["host"],
    port = app_config["app"]["port"],
  )
