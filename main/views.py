from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView


from .forms import ContactForm, CustomerForm
from .models import Contacts, Customers


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

class CustomersView(ListView):
    template_name = "main/customers.html"
    context_object_name = "customers"
    model = Customers

    def get_queryset(self):
        """
        Return all Customers that have been submitted
        """
        return Customers.objects.all()


def viewCustomer(request, customer_id):
		customer = get_object_or_404(Customers, pk=customer_id)
		return render(request, 'main/customer.html', {
			      'customer': customer,
						'error_message': "woopsy",
		    })

def editCustomer(request, customer_id):
    customer = Customers.objects.get(pk=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        form.save()
    return HttpResponseRedirect(reverse('main:customers'))

def deleteCustomer(request, customer_id):
    customer = Customers.objects.get(pk=customer_id).delete()
    return HttpResponseRedirect(reverse('main:customers'))
