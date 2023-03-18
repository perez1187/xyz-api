# Generated by Django 4.1.4 on 2023-03-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0021_result"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="player",
        ),
        migrations.AddField(
            model_name="result",
            name="description",
            field=models.CharField(
                default="", max_length=512, verbose_name="Description"
            ),
        ),
    ]