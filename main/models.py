from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contacts(models.Model):
    subject = models.CharField(max_length=75)
    message = models.CharField(max_length=200)
    sender = models.EmailField()

class Customers(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
