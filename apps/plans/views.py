from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Plan, Itinerary, Activity, Guide
from .serializers import PlanSerializer, ItinerarySerializer, ActivitySerializer, GuideSerializer

# Create your views here.
def home ( request):
    return HttpResponse ("Aplicacion Plans")

#viewsets
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.select_related('destination').all()
    serializer_class = PlanSerializer

class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer