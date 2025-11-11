from django.urls import path
from apps.destination.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]