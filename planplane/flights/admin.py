from django.contrib import admin
from .models import *

@admin.register(AircraftsData)
class AircraftsDataAdmin(admin.ModelAdmin):
    # Отображение колонок таблицы в пнели админа
    list_display = ('aircraft_code', 'name_of_aircrafts', 'range')

    # Вывод модели воздушного судна в зависимости от локализации (стандратное отображение англ)
    @admin.display(description = 'Model')
    def name_of_aircrafts(self, obj, leng = 'en'):
        if leng in obj.model:
            retstr = obj.model.get(leng)
        else:
            retstr = 'Language don`t exist'
        return retstr

admin.site.register(AirportsData)
admin.site.register(BoardingPasses)
admin.site.register(Bookings)
admin.site.register(Flights)
admin.site.register(Seats)
admin.site.register(TicketFlights)
admin.site.register(Tickets)

