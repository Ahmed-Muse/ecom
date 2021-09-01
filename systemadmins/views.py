#from ecommerce.store.models import PhysicalStockTable
from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import *
#from models import PhysicalStockTable

#start of importing for building views
from django.views.generic import ListView,DetailView
#ListView will do queryset to the database and look all the records in the database and render them back so that we can show in the web
#DetailView just brings the details of one record


#end of important libraries for building views

from django.views import generic#this is for using class method for building the views
from django.urls import reverse_lazy


#start of libraries for registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout#for login and logout- and authentication

#end of libraries for registration
from .decorators import *
from django.contrib.auth.models import Group
#class view 

#start of register and and login pages from Dennis 

def registerpage(request):
    
    register_form=CreateUserForm()
    if request.method=='POST':
        register_form=CreateUserForm(request.POST)
        if register_form.is_valid():
            #register_form.save()
            user=register_form.save()
            #user=register_form.cleaned_data.get('username')#get the username from the form
            username=register_form.cleaned_data.get('username')#get the username from the form
            messages.success(request,'Account was created for '+ username)
            group=Group.objects.get(name='customer')#create user as customer category by default
            user.groups.add(group)
            return redirect('loginpage')
    
   
    
    context={
        "register_form":register_form,
       
       
    }
    
    return render(request,"authenticate/registerpage.html",context)
@unaunthenticated_user
def loginpage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:#if there is an authenticated user
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request,'Dear '+username + ', Your username or password is incorrect ! ')
    
  
    
    context={
        
        }
    
    return render(request,"authenticate/loginpage.html",context)

def logoutpage(request):
    logout(request)#logs user out
    messages.success(request,"Successfully logged out ")
    return redirect('loginpage')

