from django.urls import path, include
from apps.destination.views import home
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet, TransportViewSet, AccommodationViewSet

router= DefaultRouter()
router.register(r'destinations', DestinationViewSet)
router.register(r'transports', TransportViewSet)
router.register(r'accommodations', AccommodationViewSet)

urlpatterns = [
    path('inicio/', home, name= 'home'),
    path('', include(router.urls)),
]

