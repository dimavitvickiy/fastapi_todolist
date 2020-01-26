from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class TodoItem(BaseModel):
    id: Optional[str] = None
    text: str
    due: datetime
    finished: bool = False


class TodoList(BaseModel):
    id: Optional[str] = None
    name: str
    items: List[TodoItem] = []
