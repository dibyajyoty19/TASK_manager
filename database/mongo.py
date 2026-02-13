import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

task_collection = None

if MONGO_URI:
    client = MongoClient(MONGO_URI)
    db = client["task_manager"]
    task_collection = db["tasks"]
