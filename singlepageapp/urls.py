from django.urls import path

from . import views

app_name="singlepageapp"
urlpatterns = [
    
	path('', views.index, name="index"),
	
	#################################################################333

	
] 