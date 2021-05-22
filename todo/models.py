from django.contrib.auth.models import User
from django.db import models


class TodoCategory(models.Model):
    category = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class TodoList(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(TodoCategory, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
