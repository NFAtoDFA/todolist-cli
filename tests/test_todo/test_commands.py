import pytest

from todolist.models import Todo
from todolist.commands import CreateTodoCommand, AlreadyExists, FlipIsDoneByIdCommand

def test_create_todo():
    cmd = CreateTodoCommand(
        title="New Todo",
        description="The first Todo ever created",
        is_done=False
    )

    todo = cmd.execute()

    db_todo = Todo.get_by_id(todo.id)
    
    assert db_todo.id == todo.id
    assert db_todo.title == todo.title
    assert db_todo.description == todo.description
    assert db_todo.is_done == todo.is_done

def test_create_already_exists():
    Todo(
        title="New Todo",
        description="The First Todo ever created",
        is_done=False
    ).save()

    cmd = CreateTodoCommand(
        title="New Todo",
        description="The Second Todo ever created",
        is_done=False)

    with pytest.raises(AlreadyExists):
            cmd.execute()

def test_is_done_flip():
    todo = Todo(
        title="New Todo",
        description="The First Todo ever created",
        is_done=False
    ).save()

    cmd = FlipIsDoneByIdCommand(id=todo.id)

    assert cmd.execute() == True
    assert cmd.execute() == False
