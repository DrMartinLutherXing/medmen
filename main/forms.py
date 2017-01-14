from django import forms
from django.core.mail import send_mail

from .models import Contacts

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=75)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

    def send_email(self):
				"""
				basic send_mail usage
				"""
				Contacts(
				     subject=self.subject,
						 message=self.message,
						 sender=self.sender).save()
				send_mail(
					self.subject,
					self.message,
					'kieran.farrar@gmail.com',
					[self.sender],
				)
				pass

