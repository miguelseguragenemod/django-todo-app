from rest_framework.exceptions import NotFound

from todo.models.todo import Todo
from todo.response_codes import TODO_NOT_FOUND


class TodoSelector(object):

    @staticmethod
    def get_all_todos():
        return Todo.objects.all()

    @staticmethod
    def get_todo_by_uuid(uuid: str, raise_exception: bool = False) -> Todo or None:
        try:
            return Todo.objects.get(uuid=uuid)
        except Todo.DoesNotExist:
            if raise_exception:
                raise NotFound(**TODO_NOT_FOUND)
            return None
