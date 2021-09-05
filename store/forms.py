from django import forms
from .models import *

#
class AddOnlineStockForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = Product
        fields = ['name','price','digital','product_image']
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name'}),
            'price':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Price'}),
            
            #form-control here is the css class that we are passing
        } 
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





##########################################################################################################################
#below is for EMS
class AddPhysicalProductForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = PhysicalStockTable
        fields = ["part_number",'description','quantity','price','comments','weight','length',
        'width','color',"expiry_date",'reorder_level',"vendor"]
class IssuePhysicalItemsForm(forms.ModelForm):
    	class Meta:
            model = PhysicalStockTable
            fields = ['issued_quantity', 'issued_to']
class ReceivePhysicalItemsForm(forms.ModelForm):
    	class Meta:
            model = PhysicalStockTable
            fields = ['received_quantity']
class PhysicalItemsReorderLevelForm(forms.ModelForm):
    	class Meta:
            model = PhysicalStockTable
            fields = ['reorder_level']

class AboutPhysicalItemsForm(forms.ModelForm):
    	class Meta:
            model = PhysicalStockTable
            fields = ['weight','length']

class SearchPhysicalItemsForm(forms.ModelForm):
    	class Meta:
            model = PhysicalStockTable
            fields = ['part_number','description']




############################################################################################################################


##################3 below is for testing only############
class AddProductForTestingOnlyForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = ForTestingOnly
        fields = ["product_name",'product_quantity','product_price']



class ContactForm(forms.Form):
    
    name=forms.CharField(max_length=10)
    email=forms.EmailField(label='E-mail')
    #category=forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject=forms.CharField(max_length=20,required=False)
    body=forms.CharField(widget=forms.Textarea, max_length=100)






############################33 dynamic forms#########################













#################3 test
