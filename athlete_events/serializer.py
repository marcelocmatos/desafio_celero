from django.db.models import fields
from rest_framework import serializers
from .models import Athlete

class AthleteSerializer(serializers.ModelSerializer):
    model = Athlete
    fields = '__all__'