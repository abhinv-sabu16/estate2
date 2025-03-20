# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Registration(models.Model):
    first_name=models.CharField(max_length=20)
    phone = models.CharField(max_length=11, unique=True)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=20,null=True)

    

    def __str__(self):
        return self.email

class Property(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField() 
    main_image =models.ImageField(upload_to='properties/main_images/')
    sliding_images = models.FileField(upload_to='properties/sliding_images/', blank=True, null=True)

    def __str__(self):
        return self.title

        