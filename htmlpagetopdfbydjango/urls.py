from django.contrib import admin
from django.urls import path
 
#This will import our view that we have already created
from .views import *
from . import views
#app_name='application'
 
urlpatterns = [
    path('admin/', admin.site.urls),

    path('posts', views.postlist, name="posts"),
    path('pdf_file', render_pdf_view, name="example"),
    path('pdf/<pk>/',customer_render_pdf_view,name='customer-pdf-view'),
    

    
   #path('customer',CustomerListView.as_view(),name='customer-list-view'),
    #path('test/',render_pdf_view,name='test-view'),
    #path('pdf/<pk>/',customer_render_pdf_view,name='customer-pdf-view'),
 
    #path('creat-invoice', views.createInvoice, name="create-nvoice"),# I have added invoices
    #path('',HomeView.as_view(),name='homeview'),
    #path('PostDetailView/<int:pk>',PostDetailView.as_view(),name='PostDetailView'), 
]