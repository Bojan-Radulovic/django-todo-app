# Generated by Django 4.1.3 on 2022-12-22 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_reminder_reminder_sound_reminder_reminder_vibrate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_creator',
        ),
    ]
