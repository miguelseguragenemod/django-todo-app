from django.db import models
from contrib.models.mixins import UUIDWithTimestampMixin


class Todo(UUIDWithTimestampMixin):

  title = models.CharField(
    verbose_name='Title',
    max_length=120
  )

  description = models.TextField(
    verbose_name='Description',
    max_length=500,
    blank=True,
    null=True,
  )

  is_completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  class Meta:
      db_table = 'todo'
      verbose_name = 'Todo'
      verbose_name_plural = 'Todos'
      app_label = 'todo'

