from django.urls import path,include
from apps.customers.views import home
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, BookingViewSet, BookingActivityViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'booking-activities', BookingActivityViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('inicio/', home, name= 'home'),
    path('', include(router.urls)),
]