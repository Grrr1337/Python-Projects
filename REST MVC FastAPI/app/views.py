# app/views.py
from fastapi import HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app import app, models, controllers
from fastapi.staticfiles import StaticFiles
from typing import Annotated, Dict, Optional
import uvicorn
from fastapi import Body, Cookie, FastAPI, HTTPException, Query, Request
from fastapi import Request
from app.models.task import TaskCreate, TaskUpdate


# templates = Jinja2Templates(directory=(Path(__file__).parent.parent / "frontend"))
templates = Jinja2Templates(directory="templates")

# app.mount("/static", StaticFiles(directory=(Path(__file__).parent.parent / "frontend/static")), name="static",)
app.mount("/static", StaticFiles(directory="templates/static"), name="static",)


# @app.get("/", tags=["Main"], summary="Root",)
# async def read_root():
#     return {"message": "Navigate to /docs"}

@app.get(
    "/",
    tags=["Root Webpage"],
    summary="This is the root webpage",
    response_class=HTMLResponse,
)
async def read_root_webpage(
    request: Request, token: Annotated[str | None, Cookie()] = None
):
     return templates.TemplateResponse(
        "index.html", {"request": request, "message": "index"}
    )



@app.get("/api/tasks")
def get_tasks():
    return {"tasks": models.tasks}

@app.post("/api/tasks")
def add_task(task: TaskCreate):
    return controllers.add_task(task, models.tasks)

@app.get("/api/tasks/{task_id}")
def get_task(task_id: int):
    return controllers.get_task(task_id, models.tasks)

@app.put("/api/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    return controllers.update_task(task_id, updated_task, models.tasks)

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    return controllers.delete_task(task_id, models.tasks)
