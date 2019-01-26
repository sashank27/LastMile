from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Passenger, Booking, Flight
from django.core.mail import EmailMessage
import sendgrid
import os
from sendgrid.helpers.mail import *

# Create your views here.
def index(request):
    return render(request, 'lastMileApp/index.html', {})

def sendMail(request):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    # from_email = Email("shreyanshdwivedi1997@gmail.com")
    # to_email = Email("test22091997@gmail.com")
    # subject = "Sending with SendGrid is Fun"
    # # content = Content("text/html", "<img src='<p>This is an <strong>important</strong> message.</p>'>")
    # template_id = "d-dcd0ed6e703f4d909ebadf9dc849f1f4"
    # mail = Mail(from_email, subject, to_email, template_id)
    # response = sg.client.mail.send.post(request_body=mail.get())
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)

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