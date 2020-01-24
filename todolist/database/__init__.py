from pymongo import MongoClient

DATABASE_URL = "mongodb://admin:password@db:27017/todo-list"
client = MongoClient(DATABASE_URL, authSource="admin")
db = client["todo-list"]
