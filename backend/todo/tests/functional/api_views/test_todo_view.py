import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from todo.tests.factories.todo_factory import TodoFactory


@pytest.mark.django_db
class TodoViewSetTests:
    create_todo_url = reverse('api-todos:v1:create-todo')
    todo_view = 'api-todos:v1:todo-view'

    def test_create_todo(self, todo_data):
        client = APIClient()
        response = client.post(self.create_todo_url, todo_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == todo_data.get('title')
        assert response.data['description'] == todo_data.get('description')

    def test_retrieve_todo(self):
        todo = TodoFactory()
        client = APIClient()
        response = client.get(reverse(self.todo_view, args=[todo.uuid]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == todo.title

    def test_update_todo(self, todo_data):
        todo = TodoFactory()
        client = APIClient()
        response = client.put(reverse(self.todo_view, args=[todo.uuid]), todo_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == todo_data.get('title')
        assert response.data['description'] == todo_data.get('description')

    def test_remove_todo(self):
        todo = TodoFactory()
        client = APIClient()
        response = client.delete(reverse(self.todo_view, args=[todo.uuid]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
