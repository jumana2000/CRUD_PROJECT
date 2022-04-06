from django.shortcuts import render
from . models import *
from .forms import EmployeeForm

# Create your views here.

def index(request):
    form = EmployeeForm
    return render(request,'home.html',{form:'form'})
