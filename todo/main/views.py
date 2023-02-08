from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect
from main.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import *


# Create your views here.
class UserList(ListView):
    model = User


class TaskList(ListView):
    model = Task


class ReminderList(ListView):
    model = Reminder
    

class TodoList(ListView):
    model = Todo


class TodoUserList(ListView):
    template_name = 'todo_list.html'

    def get_queryset(self):
        self.user = User.objects.filter(user_email=self.kwargs['email']).first()
        return Todo.objects.filter(todo_users__in=[self.user])


class SpecificUser(ListView):
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.filter(user_email=self.kwargs['email'])


def home(request):
    return render(request, 'base_generic.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'main/add_user.html'
    success_url = '/users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'main/add_user.html'
    success_url = '/users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class UserDeleteView(DeleteView):
    model = User
    template_name = 'main/delete_user.html'
    success_url = '/users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_object'] = self.get_object()
        return context


class TodoCreateView(CreateView):
    model = Todo
    fields = ['todo_name', 'todo_users']
    template_name = 'main/add_todo.html'
    success_url = '/todos'


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['todo_name', 'todo_users']
    template_name = 'main/add_todo.html'
    success_url = '/todos'


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'main/delete_todo.html'
    success_url = '/todos'


class TaskCreateView(CreateView):
    model = Task
    fields = ['task_name', 'task_completed', 'task_todo', 'task_time', 'task_reminder']
    template_name = 'main/add_task.html'
    success_url = '/todos'

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['task_name', 'task_completed', 'task_todo', 'task_time']
    template_name = 'main/add_task.html'
    success_url = '/todos'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'main/delete_task.html'
    success_url = '/todos'


def add_task_reminder(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'POST':
        form = TaskReminderForm(request.POST)
        if form.is_valid():
            task = form.save()
            reminder_time = form.cleaned_data.get('reminder_time')
            if reminder_time:
                reminder = Reminder.objects.create(
                    reminder_time=reminder_time,
                    reminder_sound=form.cleaned_data['reminder_sound'],
                    reminder_vibrate=form.cleaned_data['reminder_vibrate'],
                )
                task.task_reminder = reminder
                task.save()
            return redirect('todos')
    else:
        form = TaskReminderForm(initial={'task_todo': todo})
    return render(request, 'main/add_task_reminder.html', {'form': form})


def add_reminder(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder_time = form.cleaned_data.get('reminder_time')
            if reminder_time:
                reminder = Reminder.objects.create(
                    reminder_time=reminder_time,
                    reminder_sound=form.cleaned_data['reminder_sound'],
                    reminder_vibrate=form.cleaned_data['reminder_vibrate'],
                )
                task.task_reminder = reminder
                reminder.save()
                task.save()
            return redirect('todos')
    else:
        form = ReminderForm(initial={'reminder_task': task})
    return render(request, 'main/add_task_reminder.html', {'form': form})


class ReminderUpdateView(UpdateView):
    model = Reminder
    fields = ['reminder_time', 'reminder_sound', 'reminder_vibrate']
    template_name = 'main/add_task.html'
    success_url = '/todos'


class ReminderDeleteView(DeleteView):
    model = Reminder
    template_name = 'main/delete_reminder.html'
    success_url = '/todos'


def search_task(request):
    query = request.GET.get('q')
    if query:
        results = Task.objects.filter(task_name__icontains=query)
    else:
        results = Task.objects.all()
    return render(request, 'main/search_task.html', {'results': results})


def search_todo(request):
    query = request.GET.get('q')
    if query:
        results = Todo.objects.filter(todo_name__icontains=query)
    else:
        results = Todo.objects.all()
    return render(request, 'main/search_todo.html', {'results': results})


def search_user(request):
    query = request.GET.get('q')
    if query:
        results = User.objects.filter(user_name__icontains=query) | User.objects.filter(user_surname__icontains=query)
    else:
        results = User.objects.all()
    return render(request, 'main/search_user.html', {'results': results})