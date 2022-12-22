# Generated by Django 4.1.3 on 2022-12-21 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_todo_todo_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_task',
        ),
        migrations.AddField(
            model_name='task',
            name='task_reminder',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.reminder'),
            preserve_default=False,
        ),
    ]
