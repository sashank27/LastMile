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


def sendMail(passenger):
    sg = sendgrid.SendGridAPIClient(apikey='')

    from_email = Email("iwm2016501@iiita.ac.in")
    to_email = Email(passenger.email)
    subject = "Sending with SendGrid is Fun"
    content = Content("text/html", "<h2>Hey "+passenger.fname+" </h2><br/><h6>Sorry for the inconvenience caused</h6><br/><p>You can claim your tickets </p><br/><a href='https://google.com>here</a>")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def reschedule(request, flightNumber):
    flight    = get_object_or_404(Flight, flightNumber=flightNumber)
    bookings   = Booking.objects.filter(flightID=flight.id)
    print(flight)

    sortedFlights     = Flight.objects.order_by('departure')

    if flight.status == 'Cancelled':
        # passenger = get_object_or_404(Passenger, fname='Shreyansh')
        # sendMail(passenger)
        for booking in bookings:
            passenger = get_object_or_404(Passenger, bookingRef=booking.bookingRef, specialPreference=True)
            for sf in sortedFlights:
                print(sf.flightNumber + ' ' + str(sf.departure) + ' ' + sf.status + ' ' + str(sf.id))
                if (sf.status=='OnTime') and (sf.departure>flight.departure and sf.emptySeats>0):
                    print(str(sf.id) + ' your flight is cancelled')
                    newBooking = Booking.objects.create(bookingRef=id_generator(), passenger=passenger, flightID=sf.id)
                    passenger.bookingRef = newBooking.bookingRef
                    passenger.save()
                    sf.emptySeats -= 1
                    sf.save()
                    sendMail(passenger)

        for booking in bookings:
            passenger = get_object_or_404(Passenger, bookingRef=booking.bookingRef, specialPreference=False)
            for sf in sortedFlights:
                print(sf.flightNumber + ' ' + str(sf.departure) + ' ' + sf.status + ' ' + str(sf.id))
                if (sf.status=='OnTime') and (sf.departure>flight.departure and sf.emptySeats>0):
                    print(str(sf.id) + ' your flight is cancelled')
                    newBooking = Booking.objects.create(bookingRef=id_generator(), passenger=passenger, flightID=sf.id)
                    passenger.bookingRef = newBooking.bookingRef
                    passenger.save()
                    sf.emptySeats -= 1
                    sf.save()
                    sendMail(passenger)
        success_msg = 'All the passengers on cancelled flight - ' + flightNumber + ' have been allotted new flight tickets'
        return render(request, 'lastMileApp/index.html', {'success':success_msg})
    else:
        return HttpResponse('Your flight ' + flightNumber + ', is on time :)')

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
