from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Customer, Booking, BookingActivity, Payment
from .serializers import CustomerSerializer, BookingActivitySerializer, BookingSerializer, PaymentSerializer

# Create your views here.
def home ( request):
    return HttpResponse ("Aplicacion Customers")

#viewsets
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingActivityViewSet(viewsets.ModelViewSet):
    queryset = BookingActivity.objects.all()
    serializer_class = BookingActivitySerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer