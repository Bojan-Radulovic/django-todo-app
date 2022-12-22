from django.urls import path
from main.views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<email>/', SpecificUser.as_view()),
    path('todos/', TodoList.as_view()),
    path('todos/<email>/', TodoUserList.as_view(), name='user_todos'),
    path('tasks/', TaskList.as_view()),
    path('', home, name='home'),
]