# Generated by Django 4.2.1 on 2023-05-14 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_projects_slug_projects_project_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='body',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='created',
        ),
    ]