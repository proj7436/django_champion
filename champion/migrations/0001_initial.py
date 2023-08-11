# Generated by Django 4.2.4 on 2023-08-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Champion",
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
                ("rank", models.IntegerField()),
                ("name_team", models.CharField(max_length=30)),
                ("count_round", models.IntegerField()),
                ("count_win", models.IntegerField()),
                ("count_lose", models.IntegerField()),
                ("count_draw", models.IntegerField()),
                ("goal", models.IntegerField()),
                ("goal_conceded", models.IntegerField()),
                ("h_s", models.IntegerField()),
                ("point", models.IntegerField()),
            ],
        ),
    ]