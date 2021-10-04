from django.contrib import admin
from django.urls import path
 
#This will import our view that we have already created
from .views import *
from . import views
#rom .views import *
app_name='flights'
 
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="index"),
    path('<int:flight_id>', views.flight, name="flight"),
    path('<int:flight_id>/bookflight', views.bookflight, name="bookflight"),

   
]