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
