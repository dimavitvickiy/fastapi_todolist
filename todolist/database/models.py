from typing import Optional

from pydantic import BaseModel

from todolist.database.processors import create_todo_list, get_todo_lists


class TodoList(BaseModel):
    id: Optional[str] = None
    name: str

    async def create(self):
        todo_list_doc = self.dict()
        new_doc = await create_todo_list(todo_list_doc)
        return str(new_doc.inserted_id)

    @classmethod
    async def get_all(cls):
        return [
            TodoList(name=record["name"], id=str(record["_id"]))
            for record in await get_todo_lists()
        ]
