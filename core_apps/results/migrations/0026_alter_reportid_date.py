# Generated by Django 4.1.4 on 2023-03-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0025_alter_club_player_adjustment_alter_club_player_rb"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reportid",
            name="date",
            field=models.DateField(),
        ),
    ]
