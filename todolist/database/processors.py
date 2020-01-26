from todolist.database import db


todo_list_document = db["todo-list"]["todo-list"]


async def get_todo_lists():
    return todo_list_document.find()

async def create_todo_list(todo_list_doc):
    return todo_list_document.insert_one(todo_list_doc)
