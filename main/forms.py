from django import forms
from django.core.mail import send_mail

from .models import Contacts, Customers

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        exclude = []

    def send_email(self):
				"""
				basic send_mail usage
				"""
				Contacts(
				     subject=self.subject,
						 message=self.message,
						 sender=self.sender).save()
				Customers(email=self.sender).save()
				send_mail(
					self.subject,
					self.message,
					self.sender,
					['kieran.farrar@gmail.com'],
				)
				pass

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        exclude = []
