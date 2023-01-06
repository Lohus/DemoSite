from django.urls import path

from . import views

app_name = 'flights'
urlpatterns = [
    path('flights/', views.index, name='index'),
    path('flights/code<code_model>/', views.model_aircrafts, name='code'),
    path('flights/airport/', views.airports_of_city, name='airports'),
]