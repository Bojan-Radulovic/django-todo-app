from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from main.models import *

# Create your views here.
class UserList(ListView):
    model = User


class TaskList(ListView):
    model = Task
    

class TodoList(ListView):
    model = Todo


class TodoUserList(ListView):
    template_name = 'todo_list.html'

    def get_queryset(self):
        self.user = get_object_or_404(User, user_email=self.kwargs['email'])
        return Todo.objects.filter(todo_users__in=[self.user])


class SpecificUser(ListView):
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.filter(user_email=self.kwargs['email'])


def home(request):
    return render(request, 'base_generic.html')