from pyexpat import model
from tkinter import Widget
from . models import userList
from django import forms
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = userList
        fields = ['name','email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }