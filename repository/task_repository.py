from uuid import uuid4
from datetime import datetime
from typing import List, Optional

from fastapi import HTTPException
from models.task import Task, TaskCreate, TaskStatus
from database.mongo import task_collection


class TaskRepository:

    def create_task(self, task_data: TaskCreate) -> Task:
        if task_collection is None:
            raise HTTPException(
                status_code=503,
                detail="Database not configured in this environment"
            )

        task_dict = {
            "_id": str(uuid4()),
            "title": task_data.title,
            "description": task_data.description,
            "status": TaskStatus.pending,
            "priority": task_data.priority,
            "created_at": datetime.utcnow(),
            "external_reference_id": None
        }

        task_collection.insert_one(task_dict)

        return Task(
            id=task_dict["_id"],
            title=task_dict["title"],
            description=task_dict["description"],
            status=task_dict["status"],
            priority=task_dict["priority"],
            created_at=task_dict["created_at"],
            external_reference_id=task_dict["external_reference_id"]
        )

    def get_all_tasks(self) -> List[Task]:
        if task_collection is None:
            return []

        tasks = []
        for doc in task_collection.find():
            tasks.append(
                Task(
                    id=doc["_id"],
                    title=doc["title"],
                    description=doc["description"],
                    status=doc["status"],
                    priority=doc["priority"],
                    created_at=doc["created_at"],
                    external_reference_id=doc.get("external_reference_id")
                )
            )
        return tasks

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        if task_collection is None:
            return None

        doc = task_collection.find_one({"_id": task_id})
        if not doc:
            return None

        return Task(
            id=doc["_id"],
            title=doc["title"],
            description=doc["description"],
            status=doc["status"],
            priority=doc["priority"],
            created_at=doc["created_at"],
            external_reference_id=doc.get("external_reference_id")
        )

    def update_task(self, task_id: str, task_data: TaskCreate) -> Optional[Task]:
        if task_collection is None:
            return None

        updated = task_collection.find_one_and_update(
            {"_id": task_id},
            {
                "$set": {
                    "title": task_data.title,
                    "description": task_data.description,
                    "priority": task_data.priority
                }
            },
            return_document=True
        )

        if not updated:
            return None

        return Task(
            id=updated["_id"],
            title=updated["title"],
            description=updated["description"],
            status=updated["status"],
            priority=updated["priority"],
            created_at=updated["created_at"],
            external_reference_id=updated.get("external_reference_id")
        )

    def delete_task(self, task_id: str) -> bool:
        if task_collection is None:
            return False

        result = task_collection.delete_one({"_id": task_id})
        return result.deleted_count == 1

    def complete_task(self, task_id: str) -> Optional[Task]:
        if task_collection is None:
            return None

        updated = task_collection.find_one_and_update(
            {"_id": task_id},
            {"$set": {"status": TaskStatus.completed}},
            return_document=True
        )

        if not updated:
            return None

        return Task(
            id=updated["_id"],
            title=updated["title"],
            description=updated["description"],
            status=updated["status"],
            priority=updated["priority"],
            created_at=updated["created_at"],
            external_reference_id=updated.get("external_reference_id")
        )
