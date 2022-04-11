from django.contrib import admin
from . models import *
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'place', 'upload_image')

admin.site.register(Employeedb,EmpAdmin)