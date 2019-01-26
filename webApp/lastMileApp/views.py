from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Passenger, Booking, Flight
from django.core.mail import EmailMessage
import sendgrid
import os
from sendgrid.helpers.mail import *
from django.views.decorators.csrf import csrf_exempt
import string, random

# Create your views here.
def index(request):
    return render(request, 'lastMileApp/index.html', {})


@csrf_exempt
def reschedule_test(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse(request.POST.get('flightNumber'))
    else:
        return HttpResponse('None')


def sendMail(request):
    sg = sendgrid.SendGridAPIClient(apikey='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')

    data = {
        "from": {
            "email": "shreyanshdwivedi1997@gmail.com",
            "name": "Shreyansh Dwivedi"
        },
        "headers": {},
        "personalizations": [
            {
                "subject": "Hello, World!",
                "to": [
                    {
                        "email": "test22091997@gmail.com",
                        "name": "Test"
                    }
                ]
            }
        ],
        "reply_to": {
            "email": "shreyanshdwivedi1997@gmail.com",
            "name": "Shreyansh Dwivedi"
        },
        "subject": "Hello, World!",
        "template_id": "d-dcd0ed6e703f4d909ebadf9dc849f1f4",
    }
    response = sg.client.mail.send.post(request_body=data)
    return HttpResponse('Done')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def reschedule(request, bookingRef):
    passenger = get_object_or_404(Passenger, bookingRef=bookingRef)
    booking   = get_object_or_404(Booking, bookingRef=bookingRef)
    flight    = get_object_or_404(Flight, id=booking.flightID)
    print(flight)

    sortedFlights     = Flight.objects.order_by('departure')
    specialPassengers = Passenger.objects.filter(specialPreference=True)
    normalPassengers  = Passenger.objects.filter(specialPreference=False)

    print(specialPassengers)
    print(normalPassengers)

    if flight.status == 'Cancelled':
        for sp in specialPassengers:
            for sf in sortedFlights:
                print(sf.flightNumber + ' ' + str(sf.departure) + ' ' + sf.status + ' ' + str(sf.id))
                if (sf.status == 'OnTime') and (sf.departure > flight.departure and sf.emptySeats>0):
                    print(str(sf.id) + ' your flight is cancelled')
                    newBooking = Booking.objects.create(bookingRef=id_generator(), passenger=passenger, flightID=sf.id)
                    passenger.bookingRef = newBooking.bookingRef
                    passenger.save()
                    sf.emptySeats -= 1
                    sf.save()
                    return HttpResponseRedirect('/reschedule/'+passenger.bookingRef)
        
        for np in normalPassengers:
            for sf in sortedFlights:
                print(sf.flightNumber + ' ' + str(sf.departure) + ' ' + sf.status + ' ' + str(sf.id))
                if (sf.status == 'OnTime') and (sf.departure > flight.departure):
                    print(str(sf.id) + ' your flight is cancelled')
                    newBooking = Booking.objects.create(bookingRef=id_generator(), passenger=passenger, flightID=sf.id)
                    passenger.bookingRef = newBooking.bookingRef
                    passenger.save()
                    sf.emptySeats -= 1
                    sf.save()
                    return HttpResponseRedirect('/reschedule/'+passenger.bookingRef)
    else:
        return HttpResponse('Your flight is on time :)')

    context = {
        'passenger': passenger,
        'booking'  : booking,
        'flight'   : flight,
    }
    return render(request, 'lastMileApp/reschedule.html', context)


def claimed(request):
    return render(request, 'lastMileApp/claimed.html', {})


def preference(request, bookingRef):
    passenger = get_object_or_404(Passenger, bookingRef=bookingRef)
    booking   = get_object_or_404(Booking, bookingRef=bookingRef)
    flight    = get_object_or_404(Flight, flight_id=booking.flightID)
    context = {
        'passenger': passenger,
        'booking'  : booking,
        'flight'   : flight,
    }
    return render(request, 'lastMileApp/preference.html', context)


def setPreference(request, bookingRef):
    passenger = get_object_or_404(Passenger, bookingRef=bookingRef)
    booking   = get_object_or_404(Booking, bookingRef=bookingRef)
    flight    = get_object_or_404(Flight, flight_id=booking.flightID)
    context = {
        'passenger': passenger,
        'booking'  : booking,
        'flight'   : flight,
    }
    return render(request, 'lastMileApp/preference.html', context)


def getCabCoupons(request, bookingRef):
    passenger = get_object_or_404(Passenger, bookingRef=bookingRef)
    booking   = get_object_or_404(Booking, bookingRef=bookingRef)
    flight    = get_object_or_404(Flight, flight_id=booking.flightID)
    context = {
        'passenger': passenger,
        'booking'  : booking,
        'flight'   : flight,
    }
    return render(request, 'lastMileApp/index.html', context)


def getHotelCoupons(request, bookingRef):
    passenger = get_object_or_404(Passenger, bookingRef=bookingRef)
    booking   = get_object_or_404(Booking, bookingRef=bookingRef)
    flight    = get_object_or_404(Flight, flight_id=booking.flightID)
    context = {
        'passenger': passenger,
        'booking'  : booking,
        'flight'   : flight,
    }
    return render(request, 'lastMileApp/index.html', context)


def getFoodCoupons(request, bookingRef):
    passenger = get_object_or_404(Passenger, bookingRef=bookingRef)
    booking   = get_object_or_404(Booking, bookingRef=bookingRef)
    flight    = get_object_or_404(Flight, flight_id=booking.flightID)
    context = {
        'passenger': passenger,
        'booking'  : booking,
        'flight'   : flight,
    }
    return render(request, 'lastMileApp/index.html', context)
