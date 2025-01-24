from pydantic import BaseModel
from todolist.models import Todo
from typing import List

class ListTodosQuery(BaseModel):

    def execute(self) -> List[Todo]:
        todos = Todo.list()

        return todos

