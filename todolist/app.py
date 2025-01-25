
from models import Todo
from commands import CreateTodoCommand, FlipIsDoneByIdCommand
from queries import ListTodosQuery, TodoByTitleQuery

class TodoApp:
    def __init__(self) -> None:
        Todo.create_table()

    def add_task(self, title:str, description:str="",is_done: bool=False):
        CreateTodoCommand(title=title, description=description, is_done=is_done).execute()

    def list_tasks(self):
       return ListTodosQuery().execute() 

    def list_tasks_not_done(self):
        todo_list = ListTodosQuery().execute()
        todo_list_not_done = list()
        for todo in todo_list:
            if not todo.is_done:
                todo_list_not_done.append(todo)
        return todo_list_not_done

    def flip_is_done(self, title:str):
        todo = TodoByTitleQuery(title=title).execute()
        FlipIsDoneByIdCommand(id=todo.id).execute()
