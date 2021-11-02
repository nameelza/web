from django.shortcuts import render

from .models import Flight

# Create your views here.


def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.filter(pk=flight_id).first()
    return render(request, 'flights/flight.html', {
        'flight': flight,
        'passengers': flight.passengers.all()
    })
    
    

    
