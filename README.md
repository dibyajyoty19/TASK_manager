Task Management API (FastAPI · Docker · Kubernetes)
Overview

This project is a Task Management REST API built using FastAPI.
It demonstrates my understanding of backend development, clean code structure, containerization using Docker, and basic Kubernetes deployment using Minikube.

The focus of this assignment is on learning, system design, and explanation, not on building a fully production-ready system.

Features

CRUD APIs for managing tasks

Clean object-oriented Python design

Repository pattern for data access

MongoDB integration (local / Docker environment)

External SDK integration using GitHub (PyGithub)

Dockerized application

Kubernetes deployment using Minikube

Secrets management using environment variables and Kubernetes Secrets

Graceful handling of missing dependencies

Tech Stack

Language: Python 3.10

Framework: FastAPI

Database: MongoDB (local / Docker)

External SDK: GitHub SDK (PyGithub)

Containerization: Docker

Orchestration: Kubernetes (Minikube)

API Endpoints
Method	Endpoint	Description
POST	/tasks	Create a new task
GET	/tasks	Get all tasks
GET	/tasks/{id}	Get task by ID
PUT	/tasks/{id}	Update a task
DELETE	/tasks/{id}	Delete a task
POST	/tasks/{id}/complete	Mark task as completed
Task Model
{
  "id": "string",
  "title": "string",
  "description": "string",
  "status": "pending | in_progress | completed",
  "priority": "low | medium | high",
  "created_at": "timestamp",
  "external_reference_id": "string | null"
}

Project Structure
task-manager/
│
├── main.py                  # FastAPI routes
├── models/                  # Pydantic models
├── repository/              # Database access layer
├── services/                # External SDK services
├── database/                # MongoDB connection logic
├── Dockerfile
├── requirements.txt
├── k8s-deployment.yaml
├── k8s-service.yaml
├── k8s-secret.yaml
└── README.md

Design Principles Used

No database logic inside API routes

Clear separation of responsibilities

External services isolated from core logic

Environment-based configuration

Defensive programming to avoid crashes

External SDK Integration (GitHub)

Integrated PyGithub SDK

When a task is created, the API attempts to create a GitHub Issue

The GitHub Issue ID is stored as external_reference_id

If the GitHub API fails, task creation still succeeds

This demonstrates:

SDK usage

Token-based authentication

Graceful failure handling

Docker Usage
Build Image
docker build -t task-manager-api .

Run Container
docker run -p 8000:8000 --env-file .env task-manager-api


Swagger UI:

http://127.0.0.1:8000/docs

Kubernetes Deployment (Minikube)
Kubernetes Resources Used

Deployment

Service (NodePort)

Secret

Important Note About Database in Kubernetes

For Kubernetes deployment, the focus was on deploying the API service itself.

MongoDB was intentionally not deployed inside Kubernetes to keep the setup within an intern-level scope.

When running in Kubernetes without MongoDB:

GET /tasks returns an empty list

POST /tasks returns 503 Database not configured

The API does not crash and handles missing dependencies gracefully

In a production environment, MongoDB would typically be:

A managed cloud database, or

A StatefulSet with persistent storage

Running on Kubernetes
minikube start
minikube image load task-manager-api
kubectl apply -f k8s-secret.yaml
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
minikube service task-manager-service

What I Learned

Designing clean REST APIs using FastAPI

Structuring backend projects using OOP principles

Using real external SDKs

Containerizing applications using Docker

Deploying services using Kubernetes

Managing secrets securely

Handling system dependencies gracefully

Understanding real-world tradeoffs in system design

Conclusion

This project demonstrates my ability to quickly learn new tools, read documentation, and build cloud-ready backend services while keeping the solution clean, understandable, and within scope.