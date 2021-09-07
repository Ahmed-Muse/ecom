from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm#this django form fields tha django creates automatically for us
from django.contrib.auth.models import User
from django.forms import fields#this is the model table for the users which django creates automatically for us
from .models import *


class AddUserDetailsForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = UserDetailsModel
        fields = ["username",'password']

class CreateUserForm(UserCreationForm):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
   
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']#all these fields are from django