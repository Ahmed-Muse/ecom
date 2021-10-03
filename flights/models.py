from django.db import models

# Create your models here.
class AirportModel(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.code}: {self.city}:"


class FlightModel(models.Model):
    #the relate_name is way of accessing the relationship in a reverse order
    origin=models.ForeignKey(AirportModel,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(AirportModel,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()
    def __str__(self):
        return f"{self.id}: {self.origin}:{self.destination}"
class PassengersModel(models.Model):
    fname=models.CharField(max_length=60)
    lname=models.CharField(max_length=60)
    flights=models.ManyToManyField(FlightModel,blank=True,related_name="passengers")
    def __str__(self):
        return f"{self.fname}:{self.lname}"