from django.db.models import fields
from rest_framework import serializers
from athlete_events import models

class AthletesEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AthletesEvents
        fields = '__all__'
