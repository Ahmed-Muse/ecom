from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import fields#just for testing only

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
    price=models.DecimalField(max_digits=7,decimal_places=2)
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
    def get_cart_total(self):# sin
        orderitems = self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property # since now this is a property, we can access it in the template
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
        
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    #calculate totals for the order items by creating the method below
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


###############################################################################################################################
#below is for the EMS 
class PhysicalStockTable(models.Model):
    part_number = models.CharField('part number',max_length=255, blank=True, null=True,unique=True)# unique prevents data duplication
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=False,null=True)
    price = models.IntegerField(blank=False, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)#if adding now, pick currrent data and if updating stick to the original date
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    received_quantity = models.IntegerField(default='0',blank=True,null=True)
    received_by = models.CharField(max_length=50,blank=True,null=True)
    issued_quantity = models.IntegerField(default='0',blank=True,null=True)
    issued_by = models.CharField(max_length=50,blank=True,null=True)
    issued_to = models.CharField(max_length=50,blank=True,null=True)
    created_by = models.CharField(max_length=50,blank=True,null=True)
    reorder_level = models.IntegerField(default='0',blank=True,null=True)

    #item physical attributes
    weight = models.CharField(max_length=50,blank=True,null=True)
    length = models.CharField(max_length=50,blank=True,null=True)
    width = models.CharField(max_length=50,blank=True,null=True)
    color = models.CharField(max_length=50,blank=True,null=True)
    expiry_date = models.CharField(max_length=50,blank=True,null=True)
    
    vendor = models.CharField(max_length=50,blank=True,null=True)


    
    
    def __str__(self):
    		return self.part_number + ' ' + self.description # this will show up in the admin area
  

################################################################################################################################


##################### below is for just testing
class ForTestingOnly(models.Model):
    product_name=models.CharField(max_length=200, null=True)
    product_quantity= models.IntegerField(default=0,null=True,blank=True)
    product_price = models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
           return self.product_name
    @property
    def get_quantity_times_price(self):
        quantity_multiplied_price=self.product_quantity * self.product_price
        return quantity_multiplied_price
class ForTey(models.Model):
    product_name=models.CharField(max_length=200, null=True)
    product_quantity= models.IntegerField(default=0,null=True,blank=True)
    product_price = models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
           return self.product_name



    ###########################

   #test
class Language(models.Model):
    name = models.CharField(max_length=20)
  
    def __str__(self):
        return f"{self.name}"


   #test
class JSHtmlTest(models.Model):
    
    description = models.CharField(max_length=20)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)

  
    def __str__(self):
        return f"{self.description}"

class JsTest(models.Model):
    
    description = models.CharField(max_length=20)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)

  
    def __str__(self):
        return f"{self.description}"

class FormModel(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    
    subject=models.CharField(max_length=20)
    body=models.CharField(max_length=100)



#####################3 dynamic forms#############################3



class ModelAndFormTogether(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    interest_0 = models.CharField(max_length=20,null=True)
    interest_1 = models.CharField(max_length=20,null=True)
    interest_2 = models.CharField(max_length=20,null=True)

class  ModelAndFormTogetherForm(forms.ModelForm):
    class Meta:
        model =  ModelAndFormTogether
        fields = ["first_name",'last_name','interest_0','interest_1','interest_2']


    """ first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    interest = forms.CharField(required=True) """
    
""" class ProfileInterest(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    interest = models.CharField(max_length=250)
     """


######################### dynamic forms two ##################3333

class Profile(models.Model):
    #in the reference, this is forms.CharField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    interest_0 = models.CharField(max_length=20,null=True,blank=True)
    interest_1 = models.CharField(max_length=20,null=True,blank=True)
    interest_2 = models.CharField(max_length=20,null=True,blank=True)

class ProfileInterest(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    interest = models.CharField(max_length=20,null=True)

class ProfileForm(forms.Form):
    first_name = forms.CharField(required=True,max_length=20)
    last_name = forms.CharField(required=True,max_length=20)
    
    interest_0 = forms.CharField(required=True,max_length=20)
    interest_1 = forms.CharField(required=True,max_length=20)
    interest_2 = forms.CharField(required=True,max_length=20)
   
    for i in range(3):
        field_name = 'interest_%s' % (i,)
        
        for names in field_name:
            field_name=forms.CharField(required=False)
            names = forms.CharField(required=True,max_length=20)
        #'interest_%s' % (i,)=forms.CharField(required=True,max_length=20)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        interests = ProfileInterest.objects.filter(
            #profile=self.instance
        )
        for i in range(len(interests) + 1):
            field_name = 'interest_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = interests[i].interest
            except IndexError:
                self.initial[field_name] = ''
        # create an extra blank field
        field_name = 'interest_%s' % (i + 1,)
        self.fields[field_name] = forms.CharField(required=False)

        def clean(self):
            interests = set()
            i = 0
            field_name = 'interest_%s' % (i,)
            while self.cleaned_data.get(field_name):
                interest = self.cleaned_data[field_name]
            if interest in interests:
                self.add_error(field_name, 'Duplicate')
            else:
               interests.add(interest)
            i += 1
            field_name = 'interest_%s' % (i,)
            self.cleaned_data['interests'] = interests

        def save(self):
            profile = self.instance
            profile.first_name = self.cleaned_data['first_name']
            profile.last_name = self.cleaned_data['last_name']

            profile.interest_set.all().delete()
            for interest in self.cleaned_data['interests']:
                ProfileInterest.objects.create(
                profile=profile,
                interest=interest,
                )

    
            
            
  
