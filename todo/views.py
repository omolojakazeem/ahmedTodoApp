from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import TodoList, TodoCategory
from .forms import TodoCreateForm, TodoCreateCategoryForm


@login_required
def index(request):
    template_name = 'todo/index.html'
    #todos = TodoList.objects.all()
    todos = TodoList.objects.filter(owner=request.user)
    context = {
        'todos': todos,
    }
    return render(request, template_name=template_name, context=context)


@login_required
def create_todo(request):
    template_name = 'todo/create.html'
    todo_form = TodoCreateForm()
    if request.method == 'POST':
        todo_form = TodoCreateForm(request.POST)
        if todo_form.is_valid():
            todo_item = todo_form.save(commit=False)
            todo_item.owner = request.user
            todo_item.save()
            return redirect('todo:homepage')
    context = {
        'todo_form': todo_form,
    }
    return render(request, template_name=template_name, context=context)


@login_required
def edit_todo(request, todo_id):
    template_name = 'todo/edit.html'
    todo = TodoList.objects.get(id=todo_id)

    todo_form = TodoCreateForm(instance=todo)

    if request.method == 'POST':
        todo_form = TodoCreateForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('todo:homepage')
    context = {
        'todo': todo,
        'todo_form': todo_form
    }
    return render(request, template_name=template_name, context=context)


@login_required
def delete_todo(request, todo_id):
    template_name = 'todo/delete.html'
    todo = TodoList.objects.get(id=todo_id)

    if request.method == 'POST':
        todo.delete()
        return redirect('todo:homepage')
    context = {

    }
    return render(request, template_name=template_name, context=context)


@login_required
def create_todo_category(request):
    template_name = 'todo/create_category.html'
    todo_category_form = TodoCreateCategoryForm()
    if request.method == 'POST':
        todo_category_form = TodoCreateCategoryForm(request.POST)
        if todo_category_form.is_valid():
            todo_category_item = todo_category_form.save()
            return redirect('todo:category_index')
    context = {
        'todo_category_form': todo_category_form,
    }
    return render(request, template_name=template_name, context=context)


@login_required
def category_index(request):
    template_name = 'todo/category_index.html'
    categories = TodoCategory.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, template_name=template_name, context=context)


@login_required
def delete_todo_category(request, cat_id):
    template_name = 'todo/delete_category.html'
    category = TodoCategory.objects.get(id=cat_id)
    if request.method == 'POST':
        category.delete()
        return redirect('todo:category_index')
    context = {

    }
    return render(request, template_name=template_name, context=context)