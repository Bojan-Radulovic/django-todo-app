# Generated by Django 4.1.3 on 2023-02-07 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_reminder_reminder_task_task_task_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_reminder',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.reminder'),
        ),
    ]
