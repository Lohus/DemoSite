from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    temp = AircraftsData.objects.values('aircraft_code', 'model')
    context = { 'temp': temp}
    template = 'flights/index.html'
    return render(request, template, context)
    # return HttpResponse(template.render(context, request))

def model_aircrafts(request, code_model):
    return HttpResponse("Aircrafts code: %s." % code_model)

def airports_of_city(request):
    if request.POST:
        temp = AirportsData.objects.filter(city__en=request.POST['namecity'])
        context = {'AirportsData': temp}
    else:
        context = {}
    template = 'flights/airport_form.html'
    return render(request, template, context)

def ticket_search(request):
    template = 'flights/ticket.html'
    return render(request, template)

def main_page(request):
    template = 'flights/mainPage.html'
    context = {'title': 'Главная страница'}
    return render(request, template, context)