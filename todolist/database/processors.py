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
    return todo_list_document.insert_one({"name": todo_list.name, "items": []})


async def delete_todo_list(todo_list_id):
    todo_list_document.delete_one({"_id": ObjectId(todo_list_id)})
    return todo_list_id


async def add_todo_item(todo_list_id, todo_item):
    todo_item_doc = {
        "id": ObjectId(),
        "due": todo_item.due,
        "finished": todo_item.finished,
        "text": todo_item.text,
    }
    todo_list_document.update_one(
        {"_id": ObjectId(todo_list_id)},
        {"$push": {"items": todo_item_doc}}
    )
    return todo_list_id


async def update_todo_item(todo_list_id, todo_item):
    todo_list_document.update_one(
        {"_id": ObjectId(todo_list_id)},
        {"$set": {"items.$[item]": {
            "id": ObjectId(todo_item.id),
            "text": todo_item.text,
            "due": todo_item.due,
            "finished": todo_item.finished,
        }}},
        array_filters=[{"item.id": ObjectId(todo_item.id)}],
    )
    return todo_list_id


async def delete_todo_item(todo_list_id, todo_item_id):
    todo_list_document.update_one(
        {"_id": ObjectId(todo_list_id)},
        {"$pull": {"items": {"id": ObjectId(todo_item_id)}}}
    )
    return todo_list_id
