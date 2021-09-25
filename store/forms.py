from django import forms
from .models import *
from django.forms import (formset_factory, modelformset_factory)

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
    #def clean(self):
        #data=self.cleaned_data
        #part_number=data.get("part_number")
        #queryset=PhysicalStockTable.objects.filter(part_number_icontains=part_number)
        #queryset=PhysicalStockTable.objects.filter(part_number_icontains="CONTAINS BAD WORDS")
        #if queryset.exists():
            #self.add_error("part_number", f"{part_number} already exists! ") """
        #return part_number

class IssuePhysicalItemsForm(forms.ModelForm):
    	class Meta:
            model = PhysicalStockTable
            fields = ['description','issued_quantity', 'issued_to']
class ReceivePhysicalItemsForm(forms.ModelForm):
    	class Meta:
            model = PhysicalStockTable
            fields = ['description','received_quantity']
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

class SellingPriceCalcForm(forms.ModelForm):
    	class Meta:
            model = SellingPriceCalcModel
            fields = ['product_name','product_cost','markup','comments']

class  QuotationForm(forms.Form):
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Product description'
        })
    )
    quantity = forms.CharField(
        label='Product Quantity',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product quantity here'
        })
    )
    unit_price = forms.CharField(
        label='Unit price',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Unit price'
        })
    )
    total_price = forms.CharField(
        label='Total price',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Total price'
        })
    )
class  CustomerDetailsForm(forms.Form):
    customer = forms.CharField(
        label='customer',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Customer details'
        })
    )




######### test form
class  TwoDifferentFormsForm1(forms.Form):
    first_name = forms.CharField(
        label='first name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'first name'
        })
    )
class  TwoDifferentFormsForm2(forms.Form):
    last_name = forms.CharField(
        label='last name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'last name'
        })
    )






########################################################################################

class  QuotationCustomerForm1(forms.Form):
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Product description'
        })
    )
    quantity = forms.CharField(
        label='Product Quantity',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product quantity here'
        })
    )
    unit_price = forms.CharField(
        label='Unit price',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Unit price'
        })
    )
    total_price = forms.CharField(
        label='Total price',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Total price'
        })
    )
class  QuotationCustomerForm2(forms.Form):
    customer_name = forms.CharField(
        label='Customer name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Customer name'
        })
    )
    customer_mobile = forms.CharField(
        label='Customer Mobile',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Customer mobile'
        })
    )

##############################################################################################################

########## start of dynamic form for HRM ################3
class  HRMForm(forms.Form):
    staff_no = forms.CharField(
        label='staff_no',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Staff number'
        })
    )
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )
    department = forms.CharField(
        label='Department',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Department'
        })
    )
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        })
    )
    comment = forms.CharField(
        label='Comment',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Comment'
        })
    )




####### end of dynamic form for the HRM######################












class  NamesTableForm(forms.ModelForm):
    class Meta:
        model=NamesTable
        fields=['fname','lname']


############################################################################################################################



class ContactForm(forms.Form):
    
    name=forms.CharField(max_length=100)
    email=forms.EmailField(label='E-mail')
    #category=forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject=forms.CharField(max_length=20,required=False)
    body=forms.CharField(widget=forms.Textarea, max_length=100)
    def cleaned_contact_form_data(self):
        cleaned_data=self.cleaned_data
        name=cleaned_data.get("name")
        if name.lower().strip()=="AhmedMuseDiriye":
            raise forms.ValidationError("This name is taken")
        return name






############################33 dynamic form3   #########################
class  DynamicFormThreeForm(forms.Form):
    product_name = forms.CharField(
        label='Product Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product Name here'
        })
    )
    quantity = forms.CharField(
        label='Product Quantity',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product quantity here'
        })
    )


    














#################3 test
