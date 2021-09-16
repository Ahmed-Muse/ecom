from django.urls import path

from . import views

urlpatterns = [
    
	path('invoicesys/', views.add_invoicesys, name="invoicesys"),
	path('testjs/', views.testjs, name="testjs"),
	
]