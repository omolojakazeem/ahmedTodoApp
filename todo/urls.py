from django.urls import path
from .views import index, delete_todo, edit_todo

app_name = 'todo'

urlpatterns = [
    path('', index, name='homepage'),
    path('delete/<int:todo_id>', delete_todo, name='delete_todo'),
    path('edit/<int:todo_id>', edit_todo, name='edit_todo'),
]
