from pydantic import BaseModel
from models import Todo, NotFound

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

class FlipIsDoneByIdCommand(BaseModel):
    id: str

    def execute(self) -> bool:
        new_is_done = Todo.flip_is_done_by_id(self.id)
        return new_is_done
