from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
        data = csv.DictReader(file)
        stations = []
        for line in data:
            station = {'Name': line['Name'],
                       'Street': line['Street'],
                       'District': line['District']}
            stations.append(station)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)
    context = {'bus_stations': page,
               'page': page}

    return render(request, 'stations/index.html', context)
