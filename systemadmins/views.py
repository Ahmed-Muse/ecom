from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout#for login and logout- and authentication
from django.contrib import messages

# Create your views here.
def systemadminlogin(request):
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
def errorpage(request):
    return render(request,"errorpage.html")
