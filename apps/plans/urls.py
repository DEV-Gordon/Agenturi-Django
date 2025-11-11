from django.urls import path
from apps.plans.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]