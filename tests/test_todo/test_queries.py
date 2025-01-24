import pytest
from todolist.models import Todo
from todolist.queries import ListTodosQuery

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
