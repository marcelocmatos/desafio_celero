from django.db import models
from django.db.models.fields import UUIDField


# Create your models here.
class Athlete(models.Model):
    name = models.CharField(max_length=255, null=True)
    sex = models.CharField(max_length=255, null=True)
    age = models.CharField(max_length=255, null=True)
    height = models.CharField(max_length=255, null=True)
    weight = models.CharField(max_length=255, null=True)
    team = models.CharField(max_length=255, null=True)
    noc = models.CharField(max_length=255, null=True)
    games = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=255, null=True)
    season = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    sport = models.CharField(max_length=255, null=True)
    event = models.TextField(null=True)
    medal = models.CharField(max_length=255, null=True)
    class Meta:
        verbose_name_plural = 'athletes'
    
    def __str__(self):
        return self.name