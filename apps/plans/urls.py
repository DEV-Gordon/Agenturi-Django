from django.urls import path, include
from apps.plans.views import home
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, GuideViewSet, ItineraryViewSet, ActivityViewSet

router = DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'guides', GuideViewSet)
router.register(r'itineraries', ItineraryViewSet)
router.register(r'activities', ActivityViewSet)


urlpatterns = [
    path('inicio/', home, name= 'home'),
    path('', include(router.urls)),
]