from datetime import date
from typing import Set 

from fastapi import APIRouter, BackgroundTasks, status 
from myapp.common.constants import MY_VAR
from myapp.configs import app_config
from myapp.controllers import fooController
from pandas import Timestamp
from pydantic import BaseModel, Field, validator

api_router = APIRouter()

class FooControllerModel(BaseModel):
    name: str
    
    @validator("name")
    @classmethod
    def is_valid_fab(cls, name: str):
        if not name:
            raise ValueError(f"'{name}' is not a valid name value")
        return name 
  
def foo_execute(model: FooControllerModel):
    fooController.exec(
        name = model.name
    )

@api_router.post(
    "/foo_hello",
    status_code = status.HTTP_201_CREATED,
)
async def foo_endpoint(
    model: FooControllerModel,
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(foo_execute, model = model)
    return "job_created"