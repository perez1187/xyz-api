# Generated by Django 4.1.4 on 2023-04-21 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0005_club_player_adjustment_club_player_rb"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="club",
            name="is_active",
        ),
    ]