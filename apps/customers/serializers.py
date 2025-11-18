from rest_framework import serializers
from .models import Customer, Booking, Payment, BookingActivity
from apps.plans.serializers import ActivitySerializer, PlanSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BookingActivitySerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(read_only=True)

    class Meta:
        model = BookingActivity
        fields = ['id', 'activity', 'booking']

'''
class BookingSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    activities = BookingActivitySerializer(many=True, read_only=True, source='bookingactivity_set')

    class Meta:
        model = Booking
        fields = ['id', 'booking_date', 'status', 'plan', 'customer', 'activities'] '''

class BookingSerializer(serializers.ModelSerializer):
    plan_id = serializers.IntegerField(write_only=True)
    customer_id = serializers.IntegerField(write_only=True)

    plan = PlanSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)

    activities = BookingActivitySerializer(
        many=True,
        read_only=True,
        source='bookingactivity_set'
    )

    class Meta:
        model = Booking
        fields = [
            'id',
            'booking_date',
            'status',
            'plan', 'plan_id',
            'customer', 'customer_id',
            'activities'
        ]

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'