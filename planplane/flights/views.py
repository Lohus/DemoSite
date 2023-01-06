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
    temp = AirportsData.objects.all()
    context = {'AirportsData': temp}
    template = 'flights/airport_form.html'
    return render(request, template, context)