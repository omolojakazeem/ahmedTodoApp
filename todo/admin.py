from django.contrib import admin
from .models import TodoCategory, TodoList

admin.site.register(TodoCategory)
admin.site.register(TodoList)
