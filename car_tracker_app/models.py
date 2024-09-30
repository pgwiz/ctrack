from django.db import models

class Vehicle(models.Model):
    # Define fields for your vehicle information
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20)
    # ... other fields ...