from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4 # this is used to create unique ids for the slugs... for instance, if you have two clients with the same name
# they will be differentiated using the unique ids
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class ClientsModel(models.Model):

    Country = [
    ('Somalia', 'Somalia'),
    ('Kenya', 'Kenya'),
    ('Djibouti', 'Djibouti'),
    ]#this is a tuple

    #Basic Fields. these below variables are instances of the above class object
    clientName = models.CharField(null=True, blank=True, max_length=200)
    clientPhysicalAddress = models.CharField(null=True, blank=True, max_length=200)
    country = models.CharField(choices=Country, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    
    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    dateCreated = models.DateTimeField(blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.country, self.uniqueId)
    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.dateCreated is None:
            self.dateCreated = timezone.localtime(timezone.now())#create the date automatically
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]#then create the unique id on the fly and split the fourth one...this will run only when you initiate the model
            self.slug = slugify('{} {} {}'.format(self.clientName, self.country, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.country, self.uniqueId))
        self.lastUpdated = timezone.localtime(timezone.now())#this will run every time there are changes

        super(ClientsModel, self).save(*args, **kwargs)
        
class InvoicesModel(models.Model):
    paymentTerms = [
    ('Cash', 'Cash'),
    ('Deposit', 'Deposit'),
    ('15 days', '15 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]

    invoiceStatus = [
    ('Paid', 'Paid'),
    ('Current', 'Current'),
    ('Overdue', 'Overdue'),
   
    ]

    invoiceNumber = models.CharField(null=True, blank=True, max_length=100)
    
    invoiceDueDate = models.DateField(null=True, blank=True)
    paymentTerms = models.CharField(choices=paymentTerms, default='15 days', max_length=100)
    status = models.CharField(choices=invoiceStatus, default='Current', max_length=100)
    comments=models.CharField(blank=True,null=True,default='invoice',max_length=250)

    #RELATED fields
    client = models.ForeignKey(ClientsModel, blank=True, null=True, on_delete=models.SET_NULL)

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    dateCreated = models.DateTimeField(blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.invoiceNumber, self.uniqueId)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.dateCreated is None:
            self.dateCreated = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.invoiceNumber, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.invoiceNumber, self.uniqueId))
        self.lastUpdated = timezone.localtime(timezone.now())

        super(InvoicesModel, self).save(*args, **kwargs)


class ProductsModel(models.Model):
    Currency = [
    ('$', 'USD'),
    ('Euro', 'Euro'),
    
    ]

    description = models.CharField(null=True, blank=True,max_length=250)
    quantity = models.FloatField(null=True, blank=True)
    unitPrice = models.FloatField(null=True, blank=True)
    totalAmount = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=Currency, default='$', max_length=100)

    #Related Fields
    invoice = models.ForeignKey(InvoicesModel, blank=True, null=True, on_delete=models.CASCADE)

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    dateCreated = models.DateTimeField(blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.description, self.uniqueId)


    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.dateCreated is None:
            self.dateCreated = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.description, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.description, self.uniqueId))
        self.lastUpdated = timezone.localtime(timezone.now())

        super(ProductsModel, self).save(*args, **kwargs)

class SettingsModel(models.Model):

    Country = [
    ('Somalia', 'Somalia'),
    ('Kenya', 'Kenya'),
    ('Djibouti', 'Djibouti'),
    ]#this is a tuple

    #Basic Fields
    #Basic Fields. these below variables are instances of the above class object
    clientName = models.CharField(null=True, blank=True, max_length=200)
    clientPhysicalAddress = models.CharField(null=True, blank=True, max_length=200)
    country = models.CharField(choices=Country, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    
    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    dateCreated = models.DateTimeField(blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.country, self.uniqueId)


    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.dateCreated is None:
            self.dateCreated = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.country, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.country, self.uniqueId))
        self.lastUpdated = timezone.localtime(timezone.now())

        super(SettingsModel, self).save(*args, **kwargs)

