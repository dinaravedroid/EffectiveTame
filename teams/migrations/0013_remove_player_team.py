# Generated by Django 4.1 on 2024-08-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_player_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
    ]
