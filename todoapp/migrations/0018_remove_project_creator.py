# Generated by Django 4.1.6 on 2023-03-21 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0017_alter_project_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='creator',
        ),
    ]
