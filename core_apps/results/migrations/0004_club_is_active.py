# Generated by Django 4.1.4 on 2023-03-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0003_club_player_adjustment_club_player_rb"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
    ]
