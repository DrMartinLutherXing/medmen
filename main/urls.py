from django.conf.urls import url

from . import views

app_name="main"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^thanks/$', views.thanks, name="thanks"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^contacts/$', views.ContactsView.as_view(), name="contacts"),
    url(r'^customer/(?P<customer_id>[0-9]+)/$', views.viewCustomer, name='customer'),
    url(r'^customer/edit/(?P<customer_id>[0-9]+)/$', views.editCustomer, name='edit_customer'),
    url(r'^customer/delete/(?P<customer_id>[0-9]+)/$', views.deleteCustomer, name='delete_customer'),
    url(r'^customers/$', views.CustomersView.as_view(), name="customers"),
]
