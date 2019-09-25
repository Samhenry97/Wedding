from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rsvp', views.rsvp, name='rsvp'),
    path('guests', views.guests, name='guests')
]
