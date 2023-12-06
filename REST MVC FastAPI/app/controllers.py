# app/controllers.py
from fastapi import HTTPException
from app.models.task import TaskCreate, TaskUpdate
from app.models import tasks  # Import tasks directly from models module

def add_task(task: TaskCreate, tasks: list):
    tasks.append(task.task)
    return {"message": "Task added successfully"}

def get_task(task_id: int, tasks: list):
    if 0 <= task_id < len(tasks):
        return {"task": tasks[task_id]}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

def update_task(task_id: int, updated_task: TaskUpdate, tasks: list):
    if 0 <= task_id < len(tasks):
        tasks[task_id] = updated_task.updated_task
        return {"message": "Task updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

def delete_task(task_id: int, tasks: list):
    if 0 <= task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        return {"message": "Task deleted successfully", "deleted_task": deleted_task}
    else:
        raise HTTPException(status_code=404, detail="Task not found")
