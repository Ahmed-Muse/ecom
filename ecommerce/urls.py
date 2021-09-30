"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#start of libraries for images
from django.conf.urls.static import static
from django.conf import settings
# end of libraries for images

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),#this line does all the routing for the views

    #since systemadmins is doing all the authentication, we need the two lines below
    path('systemadmins/', include('django.contrib.auth.urls')),#this ensures and allows that we use the already built in authentication system
    path('systemadmins/', include('systemadmins.urls')),#point to systemadmins
    
    #since systemadmins is doing all the authentication, we need the two lines below
    path('invoicesys/', include('django.contrib.auth.urls')),#this ensures and allows that we use the already built in authentication system
    path('invoicesys/', include('invoicesys.urls')),#point to systemadmins
    path('invoice/', include('django.contrib.auth.urls')),#this ensures and allows that we use the already built in authentication system
    path('invoice/', include('invoice.urls')),#point to systemadmins

    path('htmlpagetopdfbydjango/', include('django.contrib.auth.urls')),#this ensures and allows that we use the already built in authentication system
    path('htmlpagetopdfbydjango/', include('htmlpagetopdfbydjango.urls')),#point to systemadmins


]


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#error
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
