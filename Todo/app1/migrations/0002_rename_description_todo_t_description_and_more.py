# Generated by Django 5.0.1 on 2024-01-09 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='description',
            new_name='t_description',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='t_title',
        ),
    ]
