from django.urls import path

from . import views

app_name="singlepageapp"
urlpatterns = [
    
	path('', views.index, name="index"),
    path('index2', views.index2, name="index2"),
    path('section/<int:num>', views.section, name="section"),
    #path('sections/', views.section, name="section"),
	
	
	#################################################################333

	
] 