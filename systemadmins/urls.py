
from django.urls import path
from . import views
#from .views import *

urlpatterns = [
    path('registerpage/', views.registerpage, name="registerpage"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logoutpage/', views.logoutpage, name="logoutpage"),
    
    
    
] 