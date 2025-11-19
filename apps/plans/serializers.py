from rest_framework import serializers
from .models import Plan, Guide, Itinerary, Activity, Destination
from apps.destination.serializers import DestinationSerializer


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ItinerarySerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True, source='activity_set')

    class Meta:
        model = Itinerary
        fields = ['id', 'day', 'description', 'plan', 'activities']

class PlanSerializer(serializers.ModelSerializer):
    # Para lectura
    destination = DestinationSerializer(read_only=True)

    # Para escritura
    destination_id = serializers.IntegerField(write_only=True)

    # Relaciones secundarias (solo lectura)
    itineraries = ItinerarySerializer(many=True, read_only=True, source='itinerary_set')
    guides = GuideSerializer(many=True, read_only=True, source='guide_set')

    class Meta:
        model = Plan
        fields = [
            'id', 'name', 'description', 'base_price',
            'destination', 'destination_id',
            'itineraries', 'guides'
        ]

    def create(self, validated_data):
        destination_id = validated_data.pop('destination_id')
        destination = Destination.objects.get(id=destination_id)
        plan = Plan.objects.create(destination=destination, **validated_data)
        return plan

"""class PlanSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer(read_only=True)
    itineraries = ItinerarySerializer(many=True, read_only=True, source='itinerary_set')
    guides = GuideSerializer(many=True, read_only=True, source='guide_set')

    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'base_price', 'destination', 'itineraries', 'guides']"""