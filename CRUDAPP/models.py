from django.db import models

# Create your models here.

class Employeedb(models.Model):
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True)
    place = models.CharField(max_length=100,blank=True)
    upload_image = models.ImageField(upload_to='emp_image',blank=True)