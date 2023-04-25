import pytest

from todo.models import Todo
from todo.services.todo_service import TodoService
from todo.tests.factories.todo_factory import TodoFactory


@pytest.mark.django_db
class TodoServiceTests:

    def test_create_todo(self, todo_data):
        todo = TodoService.create_todo(todo_data)
        assert todo.uuid is not None
        assert todo.title == todo_data['title']
        assert todo.description == todo_data['description']
        assert todo.is_completed == todo_data['is_completed']

    def test_update_todo(self, todo_data):
        todo = TodoFactory(
            title='Old Title',
            description='Old description.',
            is_completed=True,
        )
        updated_todo = TodoService.update_todo(todo, todo_data)
        assert updated_todo.uuid == todo.uuid
        assert updated_todo.title == todo_data['title']
        assert updated_todo.description == todo_data['description']
        assert updated_todo.is_completed == todo_data['is_completed']

    def test_delete_todo(self, todo_data):
        todo = TodoFactory()
        TodoService.delete_todo(todo)
        with pytest.raises(Todo.DoesNotExist):
            Todo.objects.get(uuid=todo.uuid)