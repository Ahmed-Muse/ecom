from django.contrib import admin

from flights.models import AirportModel, FlightModel, PassengersModel

# Register your models here.
admin.site.register(FlightModel)
admin.site.register(AirportModel)
admin.site.register(PassengersModel)