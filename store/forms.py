from django import forms
from .models import *

#
class AddOnlineStockForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = Product
        fields = ['name','price','digital','product_image']
        
        """ widgets={
            'part_number':forms.TextInput(attrs={'class':'form-control','placeholder':'part number','background-color':'red'}),
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'item description'}),
            'quantity_in_store':forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'price':forms.TextInput(attrs={'class':'form-control','placeholder':'price'}),
            'comments':forms.TextInput(attrs={'class':'form-control','placeholder':'comments'}),
            #form-control here is the css class that we are passing
        } """
class AddOnlineCustomerForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = Customer
        fields = ["user",'name','email']
class AddOnlineOrdersForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = Order
        fields = ["customer",'complete','transaction_id']
class OrderOnlineItemsForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = OrderItem
        fields = ["product",'order','quantity']

class AddShippingAdressOnlineForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = ShippingAddress
        fields = ["customer",'order']




