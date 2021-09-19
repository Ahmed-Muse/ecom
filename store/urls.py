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
	path('test/', views.test, name="test"),
	path('delete_physical_stock/<str:pk>/', views.delete_physical_stock, name="delete_physical_stock"),
	path('update_physical_stock/<str:pk>/', views.update_physical_stock, name="update_physical_stock"),#no template here
	path('issue_physical_items/<str:pk>/', views.issue_physical_items, name="issue_physical_items"),
	path('issue_or_receive_physical_items/<str:pk>/', views.issue_or_receive_physical_items, name="issue_or_receive_physical_items"),
	path('issue_physical_items/<str:pk>/', views.issue_physical_items, name="issue_physical_items"),#Note that this does not have template
    path('receive_physical_items/<str:pk>/', views.receive_physical_items, name="receive_physical_items"),#No template
	path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
	path('product_full_details/<str:pk>/', views.product_full_details, name="product_full_details"),
	path('search_physical_items/', views.search_physical_items, name="search_physical_items"),
	path('product_list_text_file/', views.product_list_text_file, name="product_list_text_file"),
	path('product_list_csv/', views.product_list_csv, name="product_list_csv"),
	path('product_list_pdf/', views.product_list_pdf, name="product_list_pdf"),
	path('quotation/', views.quotation, name="quotation"),
	path('test2/', views.test2, name="test2"),

	#below is for test only
	path('language/', views.language, name="language"),
	path('form/', views.contactformview, name="contactformview"),
	path('dynamicform/', views.dynamicform, name="dynamicform"),
	path('dynamicformtwo/', views.dynamicformtwo, name="dynamicformtwo"),
	path('save/', views.save, name="save"),

	path('issued_stock_history/', views.issue_physical_stock_history, name="issue_physical_stock_history"),
	path('dynamicformpartworking/', views.dynamicformpartworking, name="dynamicformpartworking"),
	path('dynamicformthree/', views.dynamicformthree, name="dynamicformthree"),
	path('savetwodifferentforms/', views.savetwodifferentforms, name="savetwodifferentforms"),
	path('quotationcustomerdetails/', views.quotationcustomerdetails, name="quotationcustomerdetails"),
	

	#path('product_full_details/<int:id>/', views.product_full_details, name="product_full_details"),
	
	
]