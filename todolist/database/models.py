from pydantic import BaseModel

from todolist.database import db


class TodoList(BaseModel):
    name: str

    async def save(self):
        todolist_doc = self.dict()
        return db["todo-list"]["todo-list"].insert_one(todolist_doc)

    @classmethod
    async def get_all(cls):
        todo_lists = TodoList(name=db["todo-list"]["todo-list"].find_one()["name"])
        return todo_lists
