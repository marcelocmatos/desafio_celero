from rest_framework import viewsets
from athlete_events.api import serializers
from athlete_events import models

class AthletesEventsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AthletesEventsSerializer
    queryset = models.AthletesEvents.objects.all()