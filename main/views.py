from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import ContactForm


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


class ContactView(FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # Write code for after form validation
        return super(ContactView, self).form_valid(form)
