from django.http import HttpResponse
from django.shortcuts import redirect

def unaunthenticated_user(view_func):
    #A decorator as the function below, is a function that takes in another function as the parameter and
    #allows us to add extra functionalities before the original function is called.
    #Thus unauthenticated func is not executed untill the decorator below (wrapper_func) is executed.
    """  when you use this function as the decorator, as below

        @aunthenticated_user
        def loginpage(request):

        say in a function in view, like
        the loginpage, the loginpage is passed as a parameter to this function as aunthenticated_user(loginpage. 
        This means that view_func is now same as the loginpage
         """

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:#if the user is not authenticated, then call the original function
            return view_func(request, *args, **kwargs)# in this line, the view_func is same as the loginpage in views.py
    return wrapper_func


def allowed_users(allowed_roles=[]):#a single page can allow multiple types of users
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            #now make the logic to restrict pages
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name#take the first index and grap its name
            if group in allowed_roles:
             
                return view_func(request, *args, **kwargs)#return the original dashboard view
            else:
                #return HttpResponse("Sorry, you are not allowed to view this page !")
                return redirect('website')#if user is not in the allowed_roles, return them to the website page
        
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='customer':
            return redirect('website')
        if group=='admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function


