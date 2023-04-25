from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from todo.selectors.todo_selector import TodoSelector
from todo.services.todo_service import TodoService
from todo.serializers.todo_serializer import TodoSerializer, CreateTodoSerializer


class TodoViewSet(ViewSet):

    def create(self, request, **kwargs):
        serializer = CreateTodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = TodoService.create_todo(data=serializer.validated_data)

        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, todo_uuid, **kwargs):
        todo = TodoSelector.get_todo_by_uuid(uuid=todo_uuid, raise_exception=True)
        return Response(TodoSerializer(todo).data)

    def update(self, request, todo_uuid, **kwargs):
        todo = TodoSelector.get_todo_by_uuid(uuid=todo_uuid, raise_exception=True)
        serializer = CreateTodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = TodoService.update_todo(todo=todo, data=serializer.validated_data)
        return Response(TodoSerializer(todo).data)

    def remove(self, request, todo_uuid, **kwargs):
        todo = TodoSelector.get_todo_by_uuid(uuid=todo_uuid, raise_exception=True)
        TodoService.delete_todo(todo)
        return Response(status=status.HTTP_204_NO_CONTENT)
