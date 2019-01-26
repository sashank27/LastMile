from django.shortcuts import render, get_object_or_404
from .models import Passenger, Booking, Flight

# Create your views here.
def index(request):
    return render(request, 'lastMileApp/index.html', {})

def reschedule(request, bookingRef):
    passenger = get_object_or_404(Passenger, bookingRef=bookingRef)
    booking   = get_object_or_404(Booking, bookingRef=bookingRef)
    flight    = get_object_or_404(Flight, flight_id=booking.flightID)
    context = {
        'passenger': passenger,
        'booking'  : booking,
        'flight'   : flight,
    }
    return render(request, 'lastMileApp/reschedule.html', context)