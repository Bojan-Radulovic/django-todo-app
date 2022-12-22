# Generated by Django 4.1.3 on 2022-12-21 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_surname', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=30)),
                ('todo_users', models.ManyToManyField(to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=30)),
                ('task_completed', models.BooleanField(default=False)),
                ('task_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
                ('task_todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.todo')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.task')),
            ],
        ),
    ]
