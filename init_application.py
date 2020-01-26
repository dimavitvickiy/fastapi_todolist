from todolist.database import db

dummy_todo_lists = [
    {
        "name": "First todo list",
        "items": [
            {
                "id": "5e2de420b7fa4321988e84e2",
                "text": "Do something 1-1",
                "due": "2020-01-25T00:00:00",
                "finished": True
            },
            {
                "id": "5e2de430b7fa4321988e84e3",
                "text": "Do something 1-2",
                "due": "2020-01-27T00:00:00",
                "finished": False
            }
        ]
    },
    {
        "name": "Second todo list",
        "items": [
            {
                "id": "5e2de420b7fa4321988e84e4",
                "text": "Do something 2-1",
                "due": "2020-01-25T00:00:00",
                "finished": False
            }
        ]
    },
    {
        "name": "Third todo list",
        "items": [
            {
                "id": "5e2de420b7fa4321988e84e5",
                "text": "Do something 3-1",
                "due": "2020-01-25T00:00:00",
                "finished": False
            },
            {
                "id": "5e2de430b7fa4321988e84e6",
                "text": "Do something 3-2",
                "due": "2020-01-27T00:00:00",
                "finished": False
            }
        ]
    }
]


if __name__ == '__main__':
    # remove all data
    db["todo-list"]["todo-list"].drop()
    # insert dummy data
    db["todo-list"]["todo-list"].insert_many(dummy_todo_lists)
