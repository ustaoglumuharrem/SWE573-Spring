# Generated by Django 5.0.3 on 2024-04-13 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0001_initial'),
        ('User', '0002_rename_nickname_user_nickname_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyModel',
            new_name='Notification',
        ),
    ]
