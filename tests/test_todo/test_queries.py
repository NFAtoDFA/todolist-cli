import pytest
from todolist.models import Todo
from todolist.queries import ListTodosQuery, TodoByIdQuery

def test_list_todos():
    Todo(
        title="A New Todo",
        description="A very cool Todo, do ASAP!",
        is_done=False
    ).save()

    Todo(
        title="Another Todo",
        description="Take your sweet time with this one",
        is_done=False
    ).save()

    query = ListTodosQuery()

    assert len(query.execute()) == 2

def test_get_todo_by_id():
    todo = Todo(
        title="A New Todo",
        description="A very cool Todo, do ASAP!",
        is_done=False
    ).save()

    query = TodoByIdQuery(id=todo.id)
    

    result = query.execute()

    assert result.id == todo.id
    assert result.title == todo.title
    assert result.description == todo.description
    assert result.is_done == todo.is_done
    
