from django.db import models

# Create your models here.

class Employeedb(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    employee_age = models.IntegerField()
    employee_image = models.ImageField(upload_to='employee_image')
    
    def __str__(self):
        return self.employee_name