from django.contrib import admin
from .models import Passenger, Booking, Flight, FlightCheck

# Register your models here.
admin.site.register(Passenger)
admin.site.register(Booking)
admin.site.register(Flight)
admin.site.register(FlightCheck)