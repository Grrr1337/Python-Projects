# app/models/task.py
from pydantic import BaseModel

class TaskCreate(BaseModel):
    task: str

class TaskUpdate(BaseModel):
    updated_task: str
