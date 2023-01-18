from django.urls import path

from . import views

app_name = 'flights'
urlpatterns = [
    path('', views.index, name='index'),
    path('code<code_model>/', views.model_aircrafts, name='code'),
    path('airport/', views.airports_of_city, name='airports'),
    path('search/', views.ticket_search, name='ticket'),
]