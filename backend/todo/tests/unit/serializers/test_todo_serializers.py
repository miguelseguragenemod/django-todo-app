import pytest

from todo.tests.factories.todo_factory import TodoFactory
from todo.serializers.todo_serializer import CreateTodoSerializer, TodoSerializer


@pytest.mark.django_db
class CreateTodoSerializerTests:

    def test_valid_serializer_data(self):
        data = {
            'title': 'Test Todo',
            'description': 'This is a test todo.',
            'is_completed': False,
        }
        serializer = CreateTodoSerializer(data=data)
        assert serializer.is_valid() is True

    def test_invalid_serializer_data(self):
        data = {
            'title': '',
            'description': 'This is a test todo.',
            'is_completed': False,
        }
        serializer = CreateTodoSerializer(data=data)
        assert serializer.is_valid() is False
        assert serializer.errors == {'title': ['This field may not be blank.']}


@pytest.mark.django_db
class TodoSerializerTests:

    def test_serializer_output(self):
        todo = TodoFactory(
            title='Test Todo',
            description='This is a test todo.',
        )
        serializer = TodoSerializer(todo)
        expected_output = {
            'uuid': str(todo.uuid),
            'title': 'Test Todo',
            'description': 'This is a test todo.',
            'is_completed': False,
            'created_at': todo.created_at.isoformat().replace('+00:00', 'Z'),
        }
        assert serializer.data == expected_output
