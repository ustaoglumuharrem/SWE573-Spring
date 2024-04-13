# Generated by Django 5.0.3 on 2024-04-13 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Communityy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.JSONField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Communityy.communityy')),
            ],
        ),
    ]