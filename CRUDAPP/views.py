from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            place = form.cleaned_data['place']
            upload_image = form.cleaned_data['upload_image']
            data = Employeedb(name=name, email=email, place=place, upload_image=upload_image)
            data.save()
            return redirect('index')
        else:
            form = EmployeeForm
        emp = Employeedb.objects.all()
    return render(request,'index.html',{'form':form,'emp':emp})


