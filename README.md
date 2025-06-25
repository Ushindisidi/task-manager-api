# Task Manager API

A lightweight FastAPI application designed to help freelancers track their to-do items with full CRUD (Create, Read, Update, Delete) capabilities.



## ✨ Features

Create Tasks: Add new tasks with a title, optional description, status, and priority.
Retrieve Tasks: Get a list of all current tasks.
Update Tasks: Modify existing tasks by their unique ID.
Delete Tasks: Remove tasks by their unique ID.
Data Validation: Ensures consistent data using Pydantic models and Enums for status and priority.
Interactive Documentation: Automatically generated Swagger UI for easy testing and API exploration.



## 🛠 Technologies Used

Python: 3.10+
Web Framework: FastAPI
Server: Uvicorn
Data Validation: Pydantic
Version Control: Git & GitHub
Deployment: Vercel



## 🚀 How to Install and Run Locally

Follow these steps to set up and run the Task Manager API on your local machine.

### Prerequisites

* Python 3.10+ installed
* pip (Python package installer)
* git (for cloning the repository)

## Installation Steps

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Ushindisidi/task-manager-api.git]
    cd task-manager-api```
    

2.  Create and activate a virtual environment:
   
   ```bash
    python3 -m venv venv
    source venv/scripts/activate
  ```
    
    

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt```
    

4.  Run the API server using Uvicorn:
    ```bash
    uvicorn main:app --reload```
    
    The --reload flag enables auto-reloading so changes to your code are reflected automatically.

    You should see output indicating that the server is running on http://127.0.0.1:8000 (or http://localhost:8000).



 💡 Usage and API Endpoints

Once the server is running, you can interact with the API using tools like curl, Postman, or through the interactive Swagger UI.

 Swagger UI

Open your web browser and navigate to:
http://127.0.0.1:8000/docs

Here, you'll find a complete, interactive documentation of all available endpoints, allowing you to test them directly from your browser.

 Example API Commands (using curl)

1. Create a Task (POST)

```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Develop Task API",
           "description": "Implement CRUD operations for task management.",
           "status": "in_progress",
           "priority": "high"
         }'
```

 2. Get All Tasks(GET):
```bash
curl -X GET "http://localhost:8000/tasks"
```
3.   Update a task(PUT):

```bash
curl -X PUT "http://localhost:8000/tasks/1" \
     -H "Content-Type: application/json" \
     -d '{
           "status": "completed",
           "description": "API developed and tested."
         }'
```
4.  Delete a task(DELETE):

```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

5.🌐 Deployment
This API is configured for easy deployment on Vercel.
A vercel.json file is included in the project root to define the build and routing configurations.
To deploy:
  Install the Vercel CLI: npm install -g vercel
  Login to Vercel: vercel login
  Deploy from your project directory: vercel

AUTHOR
Ushindi Sidi❤
