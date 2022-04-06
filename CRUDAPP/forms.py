from django import forms
from django.forms import ModelForm
from . models import *

#Create an employee form 

class EmployeeForm(ModelForm):
    class Meta:
        model = Employeedb 
        fields = ['employee_name','employee_email', 'employee_age','employee_image']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control','id': 'html5-text-input'}),
            'employee_email': forms.EmailInput(attrs={'class': 'form-control','id': 'html5-email-input'}),
            'employee_age': forms.TextInput(attrs={'class': 'form-control','id':'html5-url-input'}),
            'employee_image': forms.FileInput(attrs={'class': 'form-control','id':'formFile'}),   
        }
