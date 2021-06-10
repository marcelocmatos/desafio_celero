from .models import Athlete
from django.contrib import messages
from django.shortcuts import render
import pandas as pd


def upload_data(request):
    template = 'data_upload.html'
    prompt = {
        'order': 'Order of the CSV must be: "Name", "Sex", "Age", "Height", "Weight",\
            "Team", "NOC", "Games", "Year", "Season", "City", "Sport", "Event", "Medal".',
        'warning': 'ONLY ACCPETS CSV FILES!!!'
        }
    if request.method == 'GET':
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    
    df = pd.read_csv(csv_file)
    for item in df.values:
        Athlete.objects.update_or_create(
            name = item[1],
            sex = item[2],
            age = item[3],
            height = item[4],
            weight = item[5],
            team = item[6],
            noc = item[7],
            games = item[8],
            year = item[9],
            season = item[10],
            city = item[11],
            sport = item[12],
            event = item[13],
            medal = item[14]    
        )
    message = messages.info(request, "File Uploaded Successfuly")
    return render(request, template, message)