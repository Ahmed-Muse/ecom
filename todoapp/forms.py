from django import forms
from .models import *


class AddTasksForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = TasksModel
        fields = ["title",'task','status']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Task title'}),
            'task':forms.TextInput(attrs={'class':'form-control','placeholder':'Task description'}),
            
            
            #form-control here is the css class that we are passing
        } 