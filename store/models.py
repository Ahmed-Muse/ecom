from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    #onetoone relationship means that a user can only have one customer and customer can have one user
    #on_delete relationship means that delete the item if the user is deleted
    
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    
    def __str__(self):
    		return self.name
  
class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    price=models.FloatField()
    digital = models.BooleanField(default=False,blank=True, null=True)#If the item is digital, we dont need to ship
    #and if digital is false, then it means we need to ship as it is physical item
    product_image=models.ImageField(null=True, blank=True)
       
    def __str__(self):
        return self.name
    @property# this is property decorator that will enable us to access this as an attribute rather as a method
    def imageURL(self):
        try:
            url=self.product_image.url
        except:
            url = ''
        return url
	

	
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)#if customer is deleted, we dont want to delete the order but rather set the customer value to null
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transaction_id=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id) #it was giving errors hence commented out
        #return self.customer
    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping=True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
        
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    #calculate totals for the order items
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total
    
class ShippingAddress(models.Model):
     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)
     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
     address=models.CharField(max_length=200, null=True)
     city=models.CharField(max_length=200, null=True)
     state=models.CharField(max_length=200, null=True)
     zipcode=models.CharField(max_length=200, null=True)
     date_added = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
           return self.address
    

    