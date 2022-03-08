from django.db import models

# Create your models here.
class UserDetails(models.Model):
    email = models.EmailField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=12)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    region = models.CharField(max_length=20)
    availableResources = models.TextField()

class AdminRequest(models.Model):
    email = models.EmailField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=12)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    region = models.CharField(max_length=20)
    availableResources = models.TextField()

class AdminDetails(models.Model):
    email = models.EmailField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=12)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    region = models.CharField(max_length=20)
    availableResources = models.TextField()

