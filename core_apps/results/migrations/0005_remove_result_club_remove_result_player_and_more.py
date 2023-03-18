# Generated by Django 4.1.4 on 2023-03-13 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0004_club_is_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="club",
        ),
        migrations.RemoveField(
            model_name="result",
            name="player",
        ),
        migrations.AlterField(
            model_name="result",
            name="nickname",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nicknameOne",
                to="results.nickname",
            ),
        ),
    ]