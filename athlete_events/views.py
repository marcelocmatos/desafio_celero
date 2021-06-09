import re
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Athlete
from .serializer import AthleteSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def athlete_list(request):
    athletes = Athlete.objects.all()
    serializer = AthleteSerializer(athletes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def athlete_detail(request, pk):
    athletes = Athlete.objects.get(id=pk)
    serializer = AthleteSerializer(athletes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def athlete_create(request):
    serializer = AthleteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def athlete_update(request, pk):
    athlete = Athlete.objects.get(id = pk)
    serializer = AthleteSerializer(instance=athlete, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def athlete_delete(request, pk):
    athlete = Athlete.objects.get(id = pk)
    athlete.delete()
    return Response('DELETED')
