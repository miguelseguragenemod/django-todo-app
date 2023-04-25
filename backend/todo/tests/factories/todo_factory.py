import factory
from factory.django import DjangoModelFactory

from contrib.utils.testing.faker import instance_faker
from todo.models import Todo

faker = instance_faker()

class TodoFactory(DjangoModelFactory):
    title = factory.LazyFunction(faker.sentence)
    description = factory.LazyFunction(faker.sentence)

    class Meta:
        model = Todo
