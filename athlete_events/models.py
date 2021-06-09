from django.db import models
from django.db.models.fields import UUIDField
from uuid import uuid4


# Create your models here.
class Athlete(models.Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    team = models.CharField(max_length=255)
    noc = models.CharField(max_length=3)
    games = models.CharField(max_length=255)
    year = models.IntegerField()
    season = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    event = models.TextField()
    medal = models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = 'athletes'
    
    def __str__(self):
        return self.name