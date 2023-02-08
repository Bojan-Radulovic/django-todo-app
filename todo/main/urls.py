from django.urls import path
from django.contrib.auth.views import LogoutView
from main.views import *

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('users/<email>/', SpecificUser.as_view(), name='user'),
    path('todos/', TodoList.as_view(), name='todos'),
    path('todos/<email>/', TodoUserList.as_view(), name='user_todos'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('reminders/', ReminderList.as_view(), name='reminders'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('user/add/', UserCreateView.as_view(), name='add_user'),
    path('user/edit/<int:pk>', UserUpdateView.as_view(), name='edit_user'),
    path('user/delete/<int:pk>', UserDeleteView.as_view(), name='delete_user'),
    
    path('todo/add/', TodoCreateView.as_view(), name='add_todo'),
    path('todo/edit/<int:pk>/', TodoUpdateView.as_view(), name='update_todo'),
    path('todo/delete/<int:pk>/', TodoDeleteView.as_view(), name='delete_todo'),

    path('task/add/', TaskCreateView.as_view(), name='task_create'),
    path('task/add/<int:todo_pk>/', add_task_reminder, name='task_todo_create'),
    path('task/edit/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),

    path('reminder/add/<int:task_pk>/', add_reminder, name='reminder_add'),
    path('reminder/edit/<int:pk>/', ReminderUpdateView.as_view(), name='reminder_update'),
    path('reminder/delete/<int:pk>/', ReminderDeleteView.as_view(), name='reminder_delete'),

    path('search/tasks', search_task, name='search_tasks'),
    path('search/todos', search_todo, name='search_todos'),
    path('search/users', search_user, name='search_users'),

    path('', home, name='home'),
]