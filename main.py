from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from enum import Enum
from typin import List, Optional, Dict
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
class Taskupdate(Basemodel): # Model for task update
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

