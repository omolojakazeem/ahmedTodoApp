from django.shortcuts import render, redirect
from .models import TodoList, TodoCategory
from .forms import TodoCreateForm


def index(request):
    template_name = 'todo/index.html'
    todos = TodoList.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, template_name=template_name, context=context)


def edit_todo(request, todo_id):
    template_name = 'todo/edit.html'
    todo = TodoList.objects.get(id=todo_id)

    todo_form = TodoCreateForm(instance=todo)
    context = {
        'todo': todo,
        'todo_form':todo_form
    }
    return render(request, template_name=template_name, context=context)


def delete_todo(request, todo_id):
    template_name = 'todo/delete.html'
    todo = TodoList.objects.get(id=todo_id)

    if request.method == 'POST':
        todo.delete()
        return redirect('todo:homepage')
    context = {

    }
    return render(request, template_name=template_name, context=context)
