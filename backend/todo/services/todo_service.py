from todo.models import Todo


class TodoService(object):

    @staticmethod
    def create_todo(data: dict) -> Todo:
        return Todo.objects.create(
            title=data['title'],
            description=data['description'],
            is_completed=data['is_completed'],
        )

    @staticmethod
    def update_todo(todo: Todo, data: dict) -> Todo:
        todo.title = data.get('title', todo.title)
        todo.description = data.get('description', todo.description)
        todo.is_completed = data.get('is_completed', todo.is_completed)
        todo.save()
        return todo

    @staticmethod
    def delete_todo(todo: Todo) -> None:
        return todo.delete()
