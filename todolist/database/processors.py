from bson import ObjectId

from todolist.database import db


todo_list_document = db["todo-list"]["todo-list"]


async def get_todo_list(todo_id):
    return todo_list_document.find_one({"_id": ObjectId(todo_id)})


async def get_todo_lists():
    return todo_list_document.find()


async def update_todo_list(todo_list_id, todo_list):
    todo_list_document.update_one(
        {"_id": ObjectId(todo_list_id)},
        {"$set": {"name": todo_list.name}}
    )
    return todo_list_id


async def create_todo_list(todo_list):
    return todo_list_document.insert_one({"name": todo_list.name})


async def delete_todo_list(todo_list_id):
    todo_list_document.delete_one({"_id": ObjectId(todo_list_id)})
    return todo_list_id
