from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from todo.models import Todo
from todo.serializers.todo_serializer import TodoSerializer
from todo.selectors.todo_selector import TodoSelector

from contrib.api.pagination import TodoPagination


class TodoListViewSet(ListAPIView):
    serializer_class = TodoSerializer
    pagination_class = TodoPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_completed',]
    search_fields = ['title', 'description']

    def get_queryset(self):
        return TodoSelector.get_all_todos()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
