import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factories import *

NUM_USERS = 5
NUM_TODOS = 10
NUM_TASKS = 50
NUM_REMINDERS = 25  # has to be <= NUM_TASKS

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [User, Task, Todo, Reminder]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        users = []
        for _ in range(NUM_USERS):
            user = UserFactory()
            users.append(user)

        for _ in range(NUM_TODOS):
            todo = TodoFactory(todo_users=random.sample(users, random.randint(1, len(users))))

        reminders = []
        for _ in range(NUM_REMINDERS):
            rem = ReminderFactory()
            reminders.append(rem)
        reminders += [0]*(NUM_TASKS-NUM_REMINDERS)
        random.shuffle(reminders)

        for _ in range(NUM_TASKS):
            if reminders != []:
                rand_rem = random.choice(reminders)
                if rand_rem:
                    task = TaskFactory(task_reminder=rand_rem)
                else:
                    task = TaskFactory()
                reminders.remove(rand_rem)
            else:
                task = TaskFactory()

