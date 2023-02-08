from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_surname = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_join_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_name} {self.user_surname}"


class Todo(models.Model):
    todo_name = models.CharField(max_length=30)
    todo_users = models.ManyToManyField(User)
    todo_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.todo_name


class Reminder(models.Model):
    reminder_time = models.DateTimeField(default=timezone.now)
    reminder_sound = models.BooleanField(default=True)
    reminder_vibrate = models.BooleanField(default=True)

    def __str__(self):
        return f"Redminder at {self.reminder_time}"


class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_completed = models.BooleanField(default=False)
    task_todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    task_time = models.DateTimeField(default=timezone.now)
    task_reminder = models.OneToOneField(Reminder, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.task_name
