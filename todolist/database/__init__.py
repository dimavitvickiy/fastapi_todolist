from pymongo import MongoClient

from todolist.config import DATABASE_URL


client = MongoClient(DATABASE_URL, authSource="admin")
db = client["todo-list"]
