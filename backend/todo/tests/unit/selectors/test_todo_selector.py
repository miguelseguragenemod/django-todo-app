import pytest
from rest_framework.exceptions import NotFound

from todo.selectors.todo_selector import TodoSelector
from todo.response_codes import TODO_NOT_FOUND
from todo.tests.factories.todo_factory import TodoFactory


@pytest.mark.django_db
class TodoSelectorTests:

    def test_get_all_todos(self, todos):
        assert list(TodoSelector.get_all_todos()) == todos

    def test_get_todo_by_uuid_exists(self):
        todo = TodoFactory(title='Test Todo')
        assert TodoSelector.get_todo_by_uuid(todo.uuid) == todo

    def test_get_todo_by_uuid_not_found(self):
        uuid = 'a16609b6-f48d-4f69-9a98-058d459a492e'
        with pytest.raises(NotFound) as exc_info:
            TodoSelector.get_todo_by_uuid(uuid, raise_exception=True)
        assert exc_info.value.detail == TODO_NOT_FOUND['detail']

    def test_get_todo_by_uuid_none(self):
        uuid = 'a16609b6-f48d-4f69-9a98-058d459a492e'
        todo = TodoSelector.get_todo_by_uuid(uuid, raise_exception=False)
        assert todo == None
