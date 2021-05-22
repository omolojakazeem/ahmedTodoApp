from django.urls import path
from .views import index, delete_todo_category, delete_todo, edit_todo, create_todo, category_index, \
    create_todo_category

app_name = 'todo'

urlpatterns = [
    path('', index, name='homepage'),
    path('delete/<int:todo_id>', delete_todo, name='delete_todo'),
    path('delete_category/<int:cat_id>', delete_todo_category, name='delete_todo_category'),
    path('edit/<int:todo_id>', edit_todo, name='edit_todo'),
    path('create/', create_todo, name='create_todo'),
    path('create_category/', create_todo_category, name='create_todo_category'),
    path('category_index/', category_index, name='category_index'),
]
