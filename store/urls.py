from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.website, name="website"),#this is the home page
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
 	path('update_item/', views.updateItem, name="update_item"),
  	path('process_order/', views.processOrder, name="process_order"),
    path('main/', views.main, name="main"),
	path('dashboard/', views.dashboard, name="dashboard"),
	path('base_dashboard/', views.base_dashboard, name="base_dashboard"),
	
    
 
 

]