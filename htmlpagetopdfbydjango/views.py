from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect,get_object_or_404
 
#importing get_template from loader
from django.template.loader import get_template
 
######################3 start of imports below imports are for the html page pdf conversion by django
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import *
#########################3 end of starts important for pdf


def postlist(request):
   posts=Postpdf.objects.all()
   customers=Customerpdf.objects.all()
   context={
      "posts":posts,
      "customers":customers,

   }
   return render(request,'homeview.html',context)


def customer_render_pdf_view(request,*args,**kwargs):
    pk=kwargs.get("pk")
    customer=get_object_or_404(Customerpdf,pk=pk)
    template_path = 'pdf2.html'
    context = {'customer': customer}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if you want to auto download run the code below
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display only
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'example.html'
    customers=Customerpdf.objects.all()
    posts=Postpdf.objects.all()
    logos=Logopdf.objects.all()
    context = {'myvar': 'The data below in the two tables is from two differents',
    "customers":customers,
    "posts":posts,
    "logos":logos,
    
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if you want to auto download run the code below
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display only
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
         
    return response
    #return render(request,'example.html',context)#this can be used also


# Create your views here. just example
def htmltopdf(request):
    context={
        
    }
    return render(request,'htmltopdf.html',context)