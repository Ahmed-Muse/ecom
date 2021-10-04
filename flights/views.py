from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.
def index(request):
    flights=FlightModel.objects.all()

    context={
        "flights":flights
    }
    return render(request,'flights/index.html',context)

def flight(request,flight_id):

    
    flight=FlightModel.objects.get(id=flight_id)
    non_pasengers=PassengersModel.objects.exclude(flights=flight).all()#these are the people who are not on the flight
    #exclude passengers who among their flights, have this (flight) as one of their flights
    #this wll give a drop down of all the passengers who are not in a flight
    context={
        "flight":flight,
        "passengers":flight.passengers.all(),#this passengers is the related name
        "non_pasengers":non_pasengers,
    }
    return render(request,"flights/flight.html", context)

def bookflight(request, flight_id):
    if request.method=="POST":
        flight=FlightModel.objects.get(pk=flight_id)
        #if the request method is post (ie. someone submitted this form via the request.Post method)
        #get the flight with that flight id then  get the passenger whose id is equal whatever was submitted in the post form with the name of passenger

        passenger=PassengersModel.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)#this is like adding new row into a table...flights is from the model
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))
        
    