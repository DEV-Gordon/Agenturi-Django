from django.urls import path
from apps.customers.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]