import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from todo.tests.factories.todo_factory import TodoFactory


@pytest.mark.django_db
class TodoListViewSetTests:
    todo_list_url = reverse('api-todos:v1:todo-list')

    def test_list_todos(self):
        TodoFactory.create_batch(3)
        client = APIClient()
        response = client.get(self.todo_list_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 3

    def test_filter_todos(self):
        TodoFactory(is_completed=True)
        TodoFactory(is_completed=False)
        client = APIClient()
        response = client.get(self.todo_list_url, {'is_completed': 'true'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    def test_search_todos(self):
        TodoFactory(title='Buy milk')
        TodoFactory(title='Buy eggs')
        TodoFactory(title='Buy bread')
        client = APIClient()
        response = client.get(self.todo_list_url, {'search': 'milk'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    def test_pagination_todos(self):
        TodoFactory.create_batch(20)
        client = APIClient()
        response = client.get(self.todo_list_url, {'page': 2, 'page_size': 10})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 10