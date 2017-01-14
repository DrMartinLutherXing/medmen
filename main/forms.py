from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=75)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

    def send_email(self):
				"""
				basic send_mail usage
				"""
				send_mail(
					subject,
					message,
					'admin@example.com',
					[sender],
					fail_silently=False,
				)
				pass

