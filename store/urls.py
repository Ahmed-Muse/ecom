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
	path('hrm/', views.hrm, name="hrm"),
	path('customers/', views.customers, name="customers"),
	path('stock/', views.stock, name="stock"),
	path('stock_online/', views.stock_online, name="stock_online"),

	path('customer_online/', views.customer_online, name="customer_online"),
	path('orders_online/', views.orders_online, name="orders_online"),
	path('stock_online/', views.stock_online, name="stock_online"),
	path('order_online_items/', views.order_online_items, name="order_online_items"),
	path('shipping_address_online/', views.shipping_address_online, name="shipping_address_online"),
	
    
 
 

]