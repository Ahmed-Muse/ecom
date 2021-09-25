from django.urls import path

from . import views

urlpatterns = [
    
	path('invoice_dashboard/', views.invoice_dashboard, name="invoice_dashboard"),
	path('invoices', views.invoices, name="invoices"),
	path('products/', views.products, name="products"),
	path('clients/', views.clients, name="clients"),

	path('creat-invoice', views.createInvoice, name="create-nvoice"),# I have added invoices
	path('create-build-invoice/<slug:slug>', views.createBuildInvoice, name="create-build-invoice"),
	#path('invoices/create-build/<slug:slug>',views.createBuildInvoice, name='create-build-invoice'),


	#Delete an invoice
	path('invoices/delete/<slug:slug>',views.deleteInvoice, name='delete-invoice'),
	path('invoices/view-pdf/<slug:slug>',views.viewPDFInvoice, name='view-pdf-invoice'),
	
	
] 