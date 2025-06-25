from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Dict
app = FastAPI(
    title="Task Manager API",
    description="A simple API to manage freelancer tasks, supporting task creation, retrieval, and deletion (CRUD).",
    version="1.0.0",
)
# In-memory database simulation
tasks_db: List[Dict] = []
next_id: int = 1
#---Enums for status and priority---
class Status(str, Enum): # Enum for task status
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
class Priority(str, Enum): # Enum for task priority
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
#---Pydantic models for task creation and response---
class TaskCreate(BaseModel): # Model for task creation
    title: str
    description: Optional[str] = None
    status: Status = Status
    priority: Priority = Priority
class Taskupdate(BaseModel): # Model for task update
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Status] = None
    priority: Optional[Priority] = None
class Task(BaseModel): #pydantic model representing a task
    id: int
    title: str
    description: Optional[str] = None
    status: Status 
    priority: Priority 
@app.get("/tasks", response_model=List[Task], status_code=status.HTTP_200_OK)
async def get_all_tasks(): # Retrieve a list of all tasks
    return tasks_db
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate): # Create a new task
    global next_id
    new_task = task.model_dump()
    new_task["id"] = next_id
    tasks_db.append(new_task)
    next_id += 1
    return new_task
@app.put("/tasks/{task_id}", response_model=Task, status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task_update: Taskupdate): #Updates an existing task by ID
    for index, task in enumerate(tasks_db): # Iterate through tasks to find the one to update
        # Check if the task ID matches the one to update
        if task["id"] == task_id:
            updated_data = task_update.model_dump(exclude_unset=True)
            tasks_db[index].update(updated_data)
            return tasks_db[index] # Return the updated task
    # If the task with the given ID is not found, raise a 404 error
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with ID {task_id} not found."
    )
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT) 
async def delete_task(task_id: int): #Delete a task by ID
    global tasks_db
    initial_len = len(tasks_db)
    tasks_db = [task for task in tasks_db if task["id"] != task_id]
    if len(tasks_db) == initial_len:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found."
        )
    return {"message": f"Task with ID {task_id} deleted successfully."}



