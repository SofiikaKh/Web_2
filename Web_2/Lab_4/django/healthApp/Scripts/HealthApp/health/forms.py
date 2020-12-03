from .models import Symp
from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SympForm(ModelForm):
    class Meta:
        model= Symp
        fields=['name'] 
        vidgets = {'name': TextInput(attrs={
            'class': "form-control", 
            'name':'symptom',
            'id':'symptom',
            'placeholder': 'What worries you?'
        })}

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2', ]