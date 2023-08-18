import schedule
from pathlib import Path
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from myapp.configs import app_config

api_router = APIRouter()

@api_router.get("/version")
async def version():
    try:
        fpath = Path(__file__).parent.parent / "version.txt"
        with fpath.open("r", encoding="utf-8") as f:
            return {"version": f.read()}
    except OSError as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Failed to open version file"
        ) from e

@api_router.get("/app_config")
async def _app_config():
    return app_config
  
@api_router.get("/background_tasks")
async def _background_tasks():
    return [str(job) for job in schedule.get_jobs()]
  
@api_router.get("/")
async def root():
    return RedirectResponse("/docs")
  
