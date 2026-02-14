# Task Management API
FastAPI · Docker · Kubernetes (Minikube)

## Overview
This repository contains a **Task Management REST API** built using **FastAPI**.  
The project focuses on clean backend design, clear separation of responsibilities, external SDK integration, and containerized deployment.

Rather than aiming for maximum features, the emphasis is on **clarity, correctness, and explaining design decisions**.

---

## Tech Stack
- **Backend:** FastAPI (Python 3.10+)
- **Database:** MongoDB (local / Docker)
- **External SDK:** GitHub SDK (PyGithub)
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)

---

## Features
- Create, read, update, and delete tasks
- Clear separation between API routes, business logic, and data access
- Repository pattern for database interactions
- GitHub SDK integration for external task references
- Dockerized application
- Kubernetes deployment using Deployment, Service, and Secrets
- Graceful handling of missing dependencies

---

## Project Structure
task-manager/
├── main.py # FastAPI application entry point
├── models/ # Pydantic models
├── repository/ # Database access layer
├── services/ # External SDK integrations
├── database/ # MongoDB connection setup
│
├── Dockerfile # Docker configuration
├── requirements.txt # Python dependencies
│
├── k8s-deployment.yaml # Kubernetes Deployment
├── k8s-service.yaml # Kubernetes Service
├── k8s-secret.example.yaml # Example Kubernetes Secret
│
└── README.md

---
## API Endpoints

### Tasks
- `POST /tasks` – Create a task  
- `GET /tasks` – List all tasks  
- `GET /tasks/{task_id}` – Get task details  
- `PUT /tasks/{task_id}` – Update a task  
- `DELETE /tasks/{task_id}` – Delete a task  
- `POST /tasks/{task_id}/complete` – Mark a task as completed  

---

## Task Model
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "status": "pending | in_progress | completed",
  "priority": "low | medium | high",
  "created_at": "timestamp",
  "external_reference_id": "string"
}
```
---
## Design Notes
---
## Code Structure
- API routes contain no direct database logic
- All persistence operations are handled through a repository layer
- External integrations are isolated in service classes
- This keeps the codebase modular and easier to maintain
  
---

## Database
-MongoDB is used as a NoSQL datastore
-Accessed via a dedicated data access layer
-Suitable for flexible task-based data

---

### External SDK Integration
-GitHub is integrated using PyGithub
-A GitHub Issue can be created when a task is created
-The issue identifier is stored as external_reference_id
-If GitHub is unavailable, task creation still succeeds

---

### Docker
-The application is containerized using Docker.

---
### Highlights
-Python 3.10 base image
-Dependencies installed via requirements.txt
-Application runs using uvicorn
-No secrets are included in the image

---

### Kubernetes (Minikube)
Resources Used
-Deployment – Runs the FastAPI application
-Service – Exposes the API
-Secret – Injects environment variables securely
MongoDB is not deployed inside the Kubernetes cluster in this setup.
When the database is unavailable, the API responds with a controlled error instead of crashing.

---

### Secrets Management
-Secrets are intentionally not committed to the repository.
-Real credentials are provided via environment variables or Kubernetes Secrets
-A sample file k8s-secret.example.yaml is included to demonstrate the expected structure

---

### Running Locally
Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```
Install dependencies
```bash
pip install -r requirements.txt
```

Start the server
```bash
uvicorn main:app --reload
```

Swagger UI will be available at:
```bash
http://127.0.0.1:8000/docs
```
---
### Walkthrough
-A short video walkthrough accompanies this repository, covering:
-Architecture and code organization
-API behavior
-Docker setup
-Kubernetes deployment and runtime behavior
-Design decisions and trade-offs

---
