from django import forms
from django.forms import ModelForm
from . models import *

class EmployeeForm(ModelForm):
    class Meta:
        model = Employeedb
        fields = ['name','email','place','upload_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','id': 'html5-text-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','id': 'html5-email-input'}),
            'place': forms.TextInput(attrs={'class': 'form-control','id':'html5-url-input'}),
            'upload_image': forms.FileInput(attrs={'class': 'form-control','id':'formFile'}),   
        }
