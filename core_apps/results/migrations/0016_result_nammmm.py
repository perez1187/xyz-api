# Generated by Django 4.1.4 on 2023-03-14 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0015_remove_result_reportid"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="nammmm",
            field=models.CharField(default="", max_length=10),
        ),
    ]