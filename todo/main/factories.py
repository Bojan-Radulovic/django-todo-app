## factories.py
import factory
from factory.django import DjangoModelFactory
from main.models import *
import random
from faker import Faker

fake = Faker()

## Defining a factory
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    user_name = factory.Faker("first_name")
    user_surname = factory.Faker("last_name")
    user_email = factory.LazyAttribute(lambda p: '{}'.format(fake.unique.email()))
    user_join_time = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())


class TodoFactory(DjangoModelFactory):
    class Meta:
        model = Todo

    todo_name = factory.LazyAttribute(lambda p: '{}'.format(fake.sentence(nb_words=2)).rstrip('.'))
    todo_created = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    
    @factory.post_generation
    def todo_users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.todo_users.add(user)


class ReminderFactory(DjangoModelFactory):
    class Meta:
        model = Reminder

    reminder_time = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    reminder_sound = factory.Faker("boolean")
    reminder_vibrate = factory.Faker("boolean")


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    task_name = factory.LazyAttribute(lambda p: '{}'.format(fake.sentence(nb_words=4)).rstrip('.'))
    task_completed = factory.Faker("boolean")
    task_todo = factory.Iterator(Todo.objects.all())
    task_time = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())

    @factory.post_generation
    def task_reminder(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.task_reminder=extracted