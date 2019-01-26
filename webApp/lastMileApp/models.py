from django.db import models
from datetime import datetime    

class Passenger(models.Model):
    fname             = models.CharField(max_length=255, null=True)
    lname             = models.CharField(max_length=255, null=True)
    age               = models.IntegerField()
    email             = models.CharField(max_length=200)
    phoneNumber       = models.CharField(max_length=200)
    gender            = models.CharField(max_length=20)
    checkedBags       = models.IntegerField()
    classType         = models.CharField(max_length=100)
    specialPreference = models.BooleanField(default=False)
    bookingRef        = models.CharField(max_length=200, null=True)
    image             = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.fname + self.lname

class Booking(models.Model):
    bookingRef = models.CharField(max_length=255, null=True)
    passenger  = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flightID   = models.CharField(max_length=200)

    def __str__(self):
        return self.bookingRef

class Flight(models.Model):
    airline          = models.CharField(max_length=200)
    flightNumber     = models.CharField(max_length=200)
    arrival          = models.DateTimeField(default=datetime.now, blank=True)
    departure        = models.DateTimeField(default=datetime.now, blank=True)
    arrivalAirport   = models.CharField(max_length=200)
    departureAirport = models.CharField(max_length=200)
    status           = models.CharField(max_length=200)
    flightCheck      = models.BooleanField(default=True)
    emptySeats         = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.flightNumber

class FlightCheck(models.Model):
    flightNumber     = models.CharField(max_length=200, null=True)
    hydraulicMachine = models.BooleanField(default=True)
    wheelsCheck      = models.BooleanField(default=True)
    landingMech      = models.BooleanField(default=True)
    navigationSystem = models.BooleanField(default=True)
    
    def __str__(self):
        return self.flightNumber