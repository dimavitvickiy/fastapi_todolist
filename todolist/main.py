from fastapi import FastAPI

from todolist.database.models import TodoList
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


@app.put("/todo-list/{todo_id}/update")
async def update(todo_id: str, todo_list: TodoList):
    return await todo_list_service.update(todo_id, todo_list)
