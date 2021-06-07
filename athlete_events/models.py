from django.db import models
from django.db.models.fields import UUIDField
from uuid import uuid4


# Create your models here.
class AthletesEvents(models.Model):
    id_athlete_event = UUIDField(primary_key=True, default=uuid4, editable=False)
    athlete_name = models.CharField(max_length=255)
    athlete_sex = models.CharField(max_length=1)
    athlete_age = models.IntegerField()
    athlete_height = models.FloatField()
    athlete_weight = models.FloatField()
    athlete_team = models.CharField(max_length=255)
    athlete_noc = models.CharField(max_length=3)
    athlete_games = models.CharField(max_length=255)
    athlete_year = models.IntegerField()
    athlete_season = models.CharField(max_length=10)
    athlete_city = models.CharField(max_length=255)
    athlete_sport = models.CharField(max_length=255)
    athlete_event = models.TextField()
    athlete_medal = models.CharField(max_length=10)