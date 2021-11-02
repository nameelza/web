from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.


def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.filter(pk=flight_id).first()
    passengers = flight.passengers.all()
    nonPassengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, 'flights/flight.html', {
        'flight': flight,
        'passengers': passengers,
        'nonPassengers': nonPassengers
    })

def book(request, flight_id):
    if request.method == 'POST':
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(id=passenger_id)
        flight = Flight.objects.get(id = flight_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight_id,)))
    
    

    
