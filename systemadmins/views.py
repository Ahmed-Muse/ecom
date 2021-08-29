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

#class view 
class HomeView(ListView):
    #model=PhysicalStockTable
    template_name='class_view_test.html'

# Create your views here.
""" def systemadminlogin(request):
    titile="Login page for the system admins "
    if request.method=="POST":#if the user posts something, do below, else just show them sysadminlogin.html page
        #if the user fills the forms and posts, then grab the username and password
        username = request.POST['username']# "username" is from the html form
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)#this line does the authentication by comparing what was posted
        #that was assigned to username and password above with what exists in the database.
   
        if user is not None:
            login(request, user)
            #return to login success page
            return redirect("dashboard")
        else:
            messages.success(request,"There was an error, Try again")
           # return redirect("errorpage")
            return redirect('systemadminlogin')#this is the view function and not the template
        
   
    else:
        return render(request,"authenticate/sysadminlogin.html",{"title":titile})
def systemadminlogout(request):
    logout(request)#logs user out
    messages.success(request,"Successfully logged out ")
    return redirect('website')
    
    return render(request,"authenticate/sysadminlogin.html",{})

def registeration(request):
    userdetailsform=AddUserDetailsForm(request.POST or None)
    systemadmins=UserDetailsModel.objects.all()
    form_class=UserCreationForm()
    if form_class.is_valid():
        form_class.save()
    
    context={
        "userdetailsform":userdetailsform,
        "form_class":form_class,
        "systemadmins":systemadmins,
       
    }
    
    return render(request,"authenticate/register.html",context)
 """

#start of register and and login pages from Dennis 
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        register_form=CreateUserForm()
        if request.method=='POST':
            register_form=CreateUserForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                user=register_form.cleaned_data.get('username')#get the username from the form
                messages.success(request,'Account was created for '+ user)
                return redirect('loginpage')
    
   
    
    context={
        "register_form":register_form,
       
       
    }
    
    return render(request,"authenticate/registerpage.html",context)
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
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



def userpage(request):
    return render(request,"authenticate/userpage.html")
    


#end of register and login pages from Dennis

#below is another way of doing the view ---class based model
""" class UserRegisterView(generic.CreateView):
    form_class=UserCreationForm
    template_name='authenticate/register.html'
    success_url=reverse_lazy('sysadminlogin')
 """



def errorpage(request):
    return render(request,"errorpage.html")
    
