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

class TransportSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer(read_only=True)

    destination_id = serializers.PrimaryKeyRelatedField(
        queryset=Destination.objects.all(),
        source='destination',
        write_only=True
    )

    class Meta:
        model = Transport
        fields = ['id', 'type', 'company', 'destination', 'destination_id']