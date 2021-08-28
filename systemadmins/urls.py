
from django.urls import path
from . import views


urlpatterns = [
    path('systemadminlogin/', views.systemadminlogin, name="systemadminlogin"),
    path('errorpage/', views.errorpage, name="errorpage"),
    
]