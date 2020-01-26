from todolist.database.models import TodoList, TodoItem
from todolist.database.processors import (
    create_todo_list,
    get_todo_lists,
    get_todo_list,
    update_todo_list,
    delete_todo_list,
    add_todo_item,
    delete_todo_item,
    update_todo_item,
)


class TodoListService:
    async def create(self, todo_list):
        new_doc = await create_todo_list(todo_list)
        return str(new_doc.inserted_id)

    async def get(self, todo_id):
        todo_list_doc = await get_todo_list(todo_id)
        todo_list = TodoList(
            id=str(todo_list_doc["_id"]),
            name=todo_list_doc["name"],
            items=[
                TodoItem(
                    id=str(item["id"]),
                    due=item["due"],
                    finished=item["finished"],
                    text=item["text"],
                )
                for item in todo_list_doc["items"]
            ],
        )
        return todo_list

    async def update(self, todo_id, todo_list):
        return await update_todo_list(todo_id, todo_list)

    async def delete(self, todo_id):
        return await delete_todo_list(todo_id)

    async def get_all(self):
        return [
            TodoList(
                name=record["name"],
                id=str(record["_id"])
            )
            for record in await get_todo_lists()
        ]

    async def add_todo_item(self, todo_list_id, todo_item):
        return await add_todo_item(todo_list_id, todo_item)

    async def delete_todo_item(self, todo_list_id, todo_item_id):
        return await delete_todo_item(todo_list_id, todo_item_id)

    async def update_todo_item(self, todo_list_id, todo_item):
        return await update_todo_item(todo_list_id, todo_item)
