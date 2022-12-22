from django.contrib import admin
from .models import *

## Register your models here.
model_list = [User, Task, Todo, Reminder]
admin.site.register(model_list)
