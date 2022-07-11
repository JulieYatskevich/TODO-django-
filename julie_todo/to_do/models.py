from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('TODO', 'Todo'),
    ('IN_PROGRESS', 'In progress'),
    ('DONE', 'Done'),
)


class Board(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='boards')
    items = models.ManyToManyField('TodoItem', related_name='boards')
    created = models.DateTimeField(auto_now_add=True)
    start = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class TodoItem(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks', null=True)
    description = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='TODO')

    def __str__(self):
        return f'{self.title}'
