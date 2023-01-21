from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .localfunc import *

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
    initialData = {'cityArrived': '', 'cityDeparture': '', 'minDate': getStringDay() , 'valueDate': ''}
    context = {'title': 'Покупка билетов', 'initialData': initialData, 'tableFlights': ''}
    if request.POST:
        initialData['cityDeparture'] = request.POST['cityDeparture']
        initialData['cityArrived'] = request.POST['cityArrived']
        initialData['valueDate'] = request.POST['dateDeparture']
    
    return render(request, template, context)

def main_page(request):
    template = 'flights/mainPage.html'
    context = {'title': 'Главная страница'}
    return render(request, template, context)