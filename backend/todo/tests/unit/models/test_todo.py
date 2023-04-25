import pytest

from django.core.exceptions import ValidationError

from todo.models import Todo
from todo.tests.factories.todo_factory import TodoFactory


@pytest.mark.django_db
class TodoModelTests:

    @staticmethod
    def test_string_representation():
        todo = TodoFactory(title='Test Todo')
        assert str(todo) == 'Test Todo'

    @staticmethod
    def test_verbose_name():
        assert str(Todo._meta.verbose_name) == 'Todo'

    @staticmethod
    def test_verbose_name_plural():
        assert str(Todo._meta.verbose_name_plural) == 'Todos'

    @staticmethod
    def test_todo_is_not_completed_by_default():
        todo = TodoFactory()
        assert todo.is_completed == False

    @classmethod
    def test_todo_validation_with_long_title(self):
        with pytest.raises(ValidationError) as exec_info:
            todo = Todo.objects.create(title='This is a very long title for a todo which should raise an error due to the title being too long because it has more than 120 characters')
            todo.full_clean()
        assert 'Ensure this value has at most 120 characters (it has ' in str(exec_info.value)
