from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.

#if any changes, run makemigrations and migrate
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=20, null= True, blank=True)
    last_name = models.CharField(max_length=20, null= True, blank=True)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)
    home_number = models.CharField(max_length=10, null=True, blank=True)
    work_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100, null=True, blank=True)

    
    def __str__(self):
        return self.first_name #+ ' ' + str.lname
    
    
    
