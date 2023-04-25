import pytest

from todo.tests.factories.todo_factory import TodoFactory

@pytest.fixture
def todos():
    todo1 = TodoFactory(title='Test Todo 1')
    todo2 = TodoFactory(title='Test Todo 2')
    return [todo1, todo2]

@pytest.fixture
def todo_data():
    return {
        'title': 'Test Todo',
        'description': 'This is a test todo.',
        'is_completed': False,
    }
