from django.urls import path

from . import views

app_name="todoapp"
urlpatterns = [
    
	path('', views.index, name="index"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('update_tasks/<str:pk>/', views.update_tasks, name="update_tasks"),
	
	#################################################################333

	
] 