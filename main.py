# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# from uuid import uuid4
# from datetime import datetime

# app = FastAPI()

# # Input model (what user sends)
# class TaskCreate(BaseModel):
#     title: str
#     description: str
#     priority: str

# # Output model (what API returns)
# class Task(BaseModel):
#     id: str
#     title: str
#     description: str
#     status: str
#     priority: str
#     created_at: datetime

# # In-memory storage
# tasks: List[Task] = []

# @app.get("/")
# def home():
#     return {"message": "Task Manager API is running"}

# # Create Task
# @app.post("/tasks")
# def create_task(task_data: TaskCreate):
#     task = Task(
#         id=str(uuid4()),
#         title=task_data.title,
#         description=task_data.description,
#         status="pending",
#         priority=task_data.priority,
#         created_at=datetime.utcnow()
#     )
#     tasks.append(task)
#     return task

# # Get All Tasks
# @app.get("/tasks")
# def get_tasks():
#     return tasks

# from fastapi import HTTPException

# @app.get("/tasks/{task_id}")
# def get_task(task_id: str):
#     for task in tasks:
#         if task.id == task_id:
#             return task
#     raise HTTPException(status_code=404, detail="Task not found")

# @app.put("/tasks/{task_id}")
# def update_task(task_id: str, task_data: TaskCreate):
#     for index, task in enumerate(tasks):
#         if task.id == task_id:
#             updated_task = Task(
#                 id=task.id,
#                 title=task_data.title,
#                 description=task_data.description,
#                 status=task.status,
#                 priority=task_data.priority,
#                 created_at=task.created_at
#             )
#             tasks[index] = updated_task
#             return updated_task

#     raise HTTPException(status_code=404, detail="Task not found")

# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: str):
#     for index, task in enumerate(tasks):
#         if task.id == task_id:
#             tasks.pop(index)
#             return {"message": "Task deleted successfully"}

#     raise HTTPException(status_code=404, detail="Task not found")

# @app.post("/tasks/{task_id}/complete")
# def complete_task(task_id: str):
#     for index, task in enumerate(tasks):
#         if task.id == task_id:
#             completed_task = Task(
#                 id=task.id,
#                 title=task.title,
#                 description=task.description,
#                 status="completed",
#                 priority=task.priority,
#                 created_at=task.created_at
#             )
#             tasks[index] = completed_task
#             return completed_task

#     raise HTTPException(status_code=404, detail="Task not found")
from services.github_service import GitHubService
from fastapi import FastAPI, HTTPException
from models.task import TaskCreate, Task
from repository.task_repository import TaskRepository

app = FastAPI()

# Create repository instance
task_repo = TaskRepository()
github_service = GitHubService()

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}


@app.post("/tasks")
def create_task(task_data: TaskCreate):
    return task_repo.create_task(task_data)


@app.get("/tasks")
def get_tasks():
    return task_repo.get_all_tasks()


@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    task = task_repo.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: str, task_data: TaskCreate):
    updated_task = task_repo.update_task(task_id, task_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    deleted = task_repo.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


@app.post("/tasks/{task_id}/complete")
def complete_task(task_id: str):
    completed_task = task_repo.complete_task(task_id)
    if not completed_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return completed_task
