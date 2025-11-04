from django.contrib import admin

from .models import Destination, Accommodation, Transport

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city')
    search_fields = ('name', 'country', 'city')
    list_filter = ('country',)

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'address', 'destination')
    search_fields = ('name', 'address')
    list_filter = ('type', 'destination')

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('type', 'company', 'destination')
    search_fields = ('company',)
    list_filter = ('type',)
