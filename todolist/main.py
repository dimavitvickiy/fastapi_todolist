from fastapi import FastAPI

from todolist.services import TodoListService

app = FastAPI()
todo_list_service = TodoListService()


@app.get("/todo-list/all")
async def read_all():
    return await todo_list_service.get_all()


@app.get("/todo-list/{todo_id}")
async def read_one(todo_id: str):
    return await todo_list_service.get(todo_id)


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
