from fastapi import FastAPI

from todolist.database.models import TodoList

app = FastAPI()


@app.get("/")
async def read_root():
    todo_list = TodoList(name="First todo list")
    todo_list.save()
    return {"Hello": todo_list.name}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
