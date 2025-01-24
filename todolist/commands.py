from pydantic import BaseModel
from todolist.models import Todo, NotFound

class AlreadyExists(Exception):
    pass

class CreateTodoCommand(BaseModel):
    title: str
    description: str
    is_done: bool

    def execute(self) -> Todo:
        try:
            Todo.get_by_title(self.title)
            raise AlreadyExists
        except NotFound:
            pass

        todo = Todo(
            title=self.title,
            description=self.description,
            is_done=self.is_done
        ).save()

        return todo
