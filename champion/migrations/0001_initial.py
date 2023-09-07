# Generated by Django 3.2.9 on 2023-09-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name_team', models.CharField(max_length=30)),
                ('count_round', models.IntegerField()),
                ('count_win', models.IntegerField()),
                ('count_draw', models.IntegerField()),
                ('count_lose', models.IntegerField()),
                ('goal', models.IntegerField()),
                ('goal_conceded', models.IntegerField()),
                ('h_s', models.IntegerField()),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InfoMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noti', models.CharField(max_length=255)),
            ],
        ),
    ]
