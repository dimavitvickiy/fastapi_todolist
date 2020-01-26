from fastapi import FastAPI

from todolist.database.models import TodoList

app = FastAPI()


@app.get("/")
async def read_root():
    todo_list = TodoList(name="First todo list")
    todo_list = await todo_list.create()
    return {"Hello": todo_list}


@app.get("/todo-lists")
async def read_all():
    todo_lists = await TodoList.get_all()
    return {"Todo lists": todo_lists}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
