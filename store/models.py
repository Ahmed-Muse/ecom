from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerTable(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    #onetoone relationship means that a user can only have one customer and customer can have one user
    #on_delete relationship means that delete the item if the user is deleted
    
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    
    
    def __str__(self):
    		return self.name
  
class ProductTable(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price=models.FloatField()
    digital = models.BooleanField(default=False,blank=True, null=True)#If the item is digital, we dont need to ship
    #and if digital is false, then it means we need to ship as it is physical item
    #image
       
    def __str__(self):
        return self.name
	

	
class OrderTable(models.Model):
    customer = models.ForeignKey(CustomerTable, on_delete=models.SET_NULL, null=True,blank=True)#if customer is deleted, we dont want to delete the order but rather set the customer value to null
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        #return str(self.id) #it was giving errors hence commented out
        return self.customer
    
class OrderItemTable(models.Model):
    product_id = models.ForeignKey(ProductTable, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(OrderTable, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True,blank=True,default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
class ShippingAddressTable(models.Model):
     customer = models.ForeignKey(CustomerTable, on_delete=models.SET_NULL, null=True)
     order = models.ForeignKey(OrderTable, on_delete=models.SET_NULL, null=True)
     address=models.CharField(max_length=200, null=False)
     city=models.CharField(max_length=200, null=False)
     state=models.CharField(max_length=200, null=False)
     zipcode=models.CharField(max_length=200, null=False)
     date_added = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
           return self.address
    
    
    
    
    
    