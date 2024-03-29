# Generated by Django 4.1.4 on 2023-04-21 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0009_alter_club_unique_together_remove_club_affagent"),
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
        migrations.AlterUniqueTogether(
            name="club",
            unique_together={("club", "affAgent")},
        ),
    ]
