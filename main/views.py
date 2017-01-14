from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView


from .forms import ContactForm
from .models import Contacts


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def thanks(request):
    return render(request, "main/thanks.html")

class ContactsView(ListView):
    template_name = "main/contacts.html"
    context_object_name = "contacts"
    model = Contacts

    def get_queryset(self):
        """
        Return all Contacts that have been submitted
        """
        return Contacts.objects.all()


class ContactView(FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # Write code for after form validation
        form.subject = form.cleaned_data['subject']
        form.message = form.cleaned_data['message']
        form.sender = form.cleaned_data['sender']

        form.send_email()
        return super(ContactView, self).form_valid(form)
