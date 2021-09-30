from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json

#Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class DateInputForm(forms.DateInput):
    input_type = 'date'


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),#margin buttom
                            required=True)
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={'id': 'floatingPassword', 'class': 'form-control mb-3'}),
                            required=True)

    class Meta:
        model=User
        fields=['username','password']



class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientsModel
        fields = ['clientName', 'clientPhysicalAddress', 'country', 'postalCode', 'phoneNumber', 'emailAddress']



class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductsModel
        fields = ['description', 'quantity', 'unitPrice', 'totalAmount','currency']


class InvoiceForm(forms.ModelForm):
    paymentTermsOptions = [
    ('Cash', 'Cash'),
    ('Deposit', 'Deposit'),
    ('15 days', '15 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]
    statusOptions = [
    ('Paid', 'Paid'),
    ('Current', 'Current'),
    ('Overdue', 'Overdue'),
    ]
    
    paymentTerms = forms.ChoiceField(
                    choices = paymentTermsOptions,
                    required = True,
                    label='Select Payment Terms',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    status = forms.ChoiceField(
                    choices = statusOptions,
                    required = True,
                    label='Invoice Status',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    comments = forms.CharField(
                    required = True,
                    label='comments',
                    widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

    invoiceDueDate = forms.DateField(
                        required = True,
                        label='Invoice due date',
                        widget=DateInputForm(attrs={'class': 'form-control mb-3'}),)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('invoiceNumber', css_class='form-group col-md-6'),
                Column('invoiceDueDate', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('paymentTerms', css_class='form-group col-md-6'),
                Column('status', css_class='form-group col-md-6'),
                css_class='form-row'),
            'comments',

            Submit('submit', ' EDIT INVOICE '))

    class Meta:
        model = InvoicesModel
        fields = ['invoiceNumber', 'invoiceDueDate', 'paymentTerms', 'status', 'comments']


class SettingsForm(forms.ModelForm):
    class Meta:
        model = SettingsModel
        fields = ['clientName', 'clientPhysicalAddress', 'country', 'postalCode', 'phoneNumber', 'emailAddress']


class ClientSelectForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        self.initial_client = kwargs.pop('initial_client')
        self.CLIENT_LIST = ClientsModel.objects.all()
        self.CLIENT_CHOICES = [('-----', '--Select a Client here--')]


        for client in self.CLIENT_LIST:
            d_t = (client.uniqueId, client.clientName)
            self.CLIENT_CHOICES.append(d_t)


        super(ClientSelectForm,self).__init__(*args,**kwargs)

        self.fields['client'] = forms.ChoiceField(
                                        label='Choose a related client',
                                        choices = self.CLIENT_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    class Meta:
        model = InvoicesModel
        fields = ['client']


    def clean_client(self):# you must call clean_x, where x is what you want to overide 
        c_client = self.cleaned_data['client']
        if c_client == '-----':
            return self.initial_client
        else:
            return ClientsModel.objects.get(uniqueId=c_client)

