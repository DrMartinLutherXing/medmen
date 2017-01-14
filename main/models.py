from __future__ import unicode_literals

from django.db import models

class Contacts(models.Model):
    subject = models.CharField(max_length=75)
    message = models.CharField(max_length=200)
    sender = models.EmailField()

# Create your models here.
