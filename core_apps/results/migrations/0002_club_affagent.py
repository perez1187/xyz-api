# Generated by Django 4.1.4 on 2023-04-20 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="affAgent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="results.affagent",
                verbose_name="aff agent",
            ),
        ),
    ]
