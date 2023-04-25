from rest_framework import serializers

from todo.models.todo import Todo


class CreateTodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_completed',)


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('uuid', 'title', 'description', 'is_completed', 'created_at',)

