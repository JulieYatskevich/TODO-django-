from django.contrib import admin

from .models import Board, TodoItem

admin.site.register(Board)
admin.site.register(TodoItem)
