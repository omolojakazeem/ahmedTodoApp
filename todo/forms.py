from django import forms
from .models import TodoList, TodoCategory


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'
