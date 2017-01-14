from django.conf.urls import url

from . import views

app_name="main"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^thanks/$', views.thanks, name="thanks"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^contacts/$', views.ContactsView.as_view(), name="contacts"),
]
