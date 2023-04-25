# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'todo'
urlpatterns = [
    path('v1/', include('todo.api.v1.urls', namespace='v1')),
]
