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
    
from django.db import models

class Property(models.Model):
    # Title of the property
    title = models.CharField(max_length=200)

    # Description of the property
    description = models.TextField()

    # Price of the property
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Location of the property
    location = models.CharField(max_length=255)

    # Number of bedrooms
    bedrooms = models.PositiveIntegerField()

    # Number of bathrooms
    bathrooms = models.PositiveIntegerField()

    # Size of the property in square feet
    size = models.PositiveIntegerField(help_text="Size in square feet")

    # Date the property was listed
    created_at = models.DateTimeField(auto_now_add=True)

    # Date the property was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # Optional: Image field for property images
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    # Optional: A field to indicate if the property is available for sale or rent
    is_for_sale = models.BooleanField(default=True)

    def __str__(self):
        return self.title
        