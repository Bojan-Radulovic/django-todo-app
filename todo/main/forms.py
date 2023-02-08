from django import forms
from .models import User, Todo, Reminder, Task

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_surname', 'user_email']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_name', 'todo_users']

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['reminder_time', 'reminder_sound', 'reminder_vibrate']
    
    reminder_task = forms.Field(required=False, disabled=True)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_completed', 'task_todo', 'task_time', 'task_reminder']


class TaskReminderForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_completed', 'task_todo', 'task_time']

    reminder_time = forms.DateTimeField(required=False)
    reminder_sound = forms.BooleanField(required=False)
    reminder_vibrate = forms.BooleanField(required=False)