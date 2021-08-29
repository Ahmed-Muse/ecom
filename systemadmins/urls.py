
from django.urls import path
from . import views
#from .views import *

urlpatterns = [
    #path('systemadminlogin/', views.systemadminlogin, name="systemadminlogin"),
    path('errorpage/', views.errorpage, name="errorpage"),
    #path('systemadminlogout/', views.systemadminlogout, name="logout"),#the name is paassed to the template as the reference url
    #path('register/', views.registeration, name="register"),#the name is paassed to the template as the reference url
    # path('register/', UserRegisterView.as_view(),name='register'),#the name is paassed to the template as the reference url

    path('registerpage/', views.registerpage, name="registerpage"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logoutpage/', views.logoutpage, name="logoutpage"),
    path('userpage/', views.userpage, name="userpage"),

    
    
] 