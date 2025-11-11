from rest_framework import serializers
from .models import Destination, Accommodation, Transport


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = '__all__'
        read_only_fields = ('id',)


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'
        read_only_fields = ('id',)


class DestinationSerializer(serializers.ModelSerializer):
    accommodations = AccommodationSerializer(many=True, read_only=True, source='accommodation_set')
    transports = TransportSerializer(many=True, read_only=True, source='transport_set')
    
    class Meta:
        model = Destination
        fields = ['id', 'name', 'country', 'city', 'accommodations', 'transports']
        read_only_fields = ('id',)


class DestinationListSerializer(serializers.ModelSerializer):
    """Serializer ligero para listados"""
    class Meta:
        model = Destination
        fields = ['id', 'name', 'country', 'city']
        read_only_fields = ('id',)