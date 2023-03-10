# Generated by Django 4.1.4 on 2023-03-12 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Club",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("club", models.CharField(max_length=100, verbose_name="Club")),
            ],
        ),
        migrations.CreateModel(
            name="Nickname",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(max_length=100, verbose_name="Nickname")),
                (
                    "player_rb",
                    models.DecimalField(
                        decimal_places=3,
                        default=0.0,
                        max_digits=10,
                        verbose_name="Player Rakeback",
                    ),
                ),
                (
                    "player_adjustment",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        verbose_name="Player Adjustment",
                    ),
                ),
                (
                    "club",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="club2",
                        to="results.club",
                        verbose_name="Club",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        default=2,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nickname23",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "unique_together": {("nickname", "club")},
            },
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "club",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nickname4",
                        to="results.nickname",
                        verbose_name="Club",
                    ),
                ),
                (
                    "nickname",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nickname44",
                        to="results.nickname",
                        verbose_name="Nickname",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nickname2",
                        to="results.nickname",
                        verbose_name="Player",
                    ),
                ),
            ],
        ),
    ]
