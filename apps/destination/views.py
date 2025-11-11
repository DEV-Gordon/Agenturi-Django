from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Destination, Accommodation, Transport
from .serializers import DestinationSerializer, AccommodationSerializer, TransportSerializer

# Create your views here.
def home ( request):
    return HttpResponse ("Aplicacion Destination")

#viewsets
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer