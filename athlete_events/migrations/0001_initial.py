# Generated by Django 3.2.4 on 2021-06-07 23:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AthletesEvents',
            fields=[
                ('id_athlete_event', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('athlete_name', models.CharField(max_length=255)),
                ('athlete_sex', models.CharField(max_length=1)),
                ('athlete_age', models.IntegerField()),
                ('athlete_height', models.FloatField()),
                ('athlete_weight', models.FloatField()),
                ('athlete_team', models.CharField(max_length=255)),
                ('athlete_noc', models.CharField(max_length=3)),
                ('athlete_games', models.CharField(max_length=255)),
                ('athlete_year', models.IntegerField()),
                ('athlete_season', models.CharField(max_length=10)),
                ('athlete_city', models.CharField(max_length=255)),
                ('athlete_sport', models.CharField(max_length=255)),
                ('athlete_event', models.TextField()),
                ('athlete_medal', models.CharField(max_length=10)),
            ],
        ),
    ]
