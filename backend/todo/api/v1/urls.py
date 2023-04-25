# -*- coding: utf-8 -*-

from django.urls import path

from todo.api.v1.views.todo_list import TodoListViewSet
from todo.api.v1.views.todo import TodoViewSet


app_name = 'todo'
urlpatterns = [
    #
    # T O D O S
    #
    path(
        'todos/',
        TodoListViewSet.as_view(),
        name='todo-list',
    ),

    path(
        'todo/',
        TodoViewSet.as_view({ 'post': 'create' }),
        name='create-todo',
    ),

    path(
        'todo/<uuid:todo_uuid>/',
        TodoViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'remove'
        }),
        name='todo-view',
    ),

]
