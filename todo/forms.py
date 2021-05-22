from django import forms
from .models import TodoList, TodoCategory


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        exclude = ['owner']


class TodoCreateCategoryForm(forms.ModelForm):
    class Meta:
        model = TodoCategory
        fields = '__all__'