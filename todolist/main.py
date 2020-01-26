from fastapi import FastAPI

from todolist.database.models import TodoList, TodoItem
from todolist.services import TodoListService

app = FastAPI()
todo_list_service = TodoListService()


@app.get("/todo-list/all")
async def read_all():
    return await todo_list_service.get_all()


@app.get("/todo-list/{todo_id}")
async def read_one(todo_id: str):
    return await todo_list_service.get(todo_id)


@app.delete("/todo-list/{todo_id}")
async def delete(todo_id: str):
    return await todo_list_service.delete(todo_id)


@app.post("/todo-list")
async def create(todo_list: TodoList):
    return await todo_list_service.create(todo_list)


@app.put("/todo-list/{todo_id}")
async def update(todo_id: str, todo_list: TodoList):
    return await todo_list_service.update(todo_id, todo_list)

@app.post("/todo-list/{todo_id}/items")
async def add_item(todo_id: str, todo_item: TodoItem):
    return await todo_list_service.add_todo_item(todo_id, todo_item)

@app.delete("/todo-list/{todo_id}/items/{item_id}")
async def delete_item(todo_id: str, item_id: str):
    return await todo_list_service.delete_todo_item(todo_id, item_id)


@app.put("/todo-list/{todo_id}/items")
async def update_item(todo_id: str, todo_item: TodoItem):
    return await todo_list_service.update_todo_item(todo_id, todo_item)
