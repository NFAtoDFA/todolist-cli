from pydantic import BaseModel
from models import Todo
from typing import List

class ListTodosQuery(BaseModel):

    def execute(self) -> List[Todo]:
        todos = Todo.list()

        return todos

class TodoByIdQuery(BaseModel):
    id: str

    def execute(self) -> Todo:
        todo = Todo.get_by_id(self.id)
        return todo

class TodoByTitleQuery(BaseModel):
    title: str

    def execute(self) -> Todo:
        todo = Todo.get_by_title(self.title)
        return todo
