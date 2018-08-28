from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

# Create your views here.


def home(request):
    df = pd.read_csv('media/Events Report of Drivers in Ahmedabad_16-07 to 31-07.csv')
    stopList = list(set(df['Stop Name']))
    eventList = list(set(df['Event Name']))

    if request.method == 'GET':
        context = {'stopList': stopList, 'data': False, 'eventList': eventList}
        return render(request, 'home/temp1.html', context)
    if request.method == 'POST':
        stopName = request.POST['stopName']
        eventName = request.POST['eventName']
        condition = (df['Stop Name'] == stopName) & (df['Event Name'] == eventName)
        d = df[condition]
        names = list(d['Event Name'].values)
        lats = list(d['Latitude'].values)
        longs = list(d['Longitude'].values)
        context = {
            'stopList': stopList,
            'names': names,
            'lats': lats,
            'longs': longs,
            'n': [x for x in range(len(lats))],
            'data': True,
            'eventList': eventList,
        }
        return render(request, 'home/temp1.html', context)