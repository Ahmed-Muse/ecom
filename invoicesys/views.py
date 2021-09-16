from django.shortcuts import render,redirect
from .forms import *


# Create your views here.
def add_invoicesys(request):
    title="invoice management system"
    form=InvoiceForm(request.POST or None)
    invoice_product=Invoice.objects.all()
    
    if form.is_valid():
        form.save()
      
    
    context={
        "title":title,
        "form":form,
        "invoice_product":invoice_product
    }
    return render(request,'invoicesys.html',context)
def testjs(request):
    context={}
    return render(request,'testjs.html',context)