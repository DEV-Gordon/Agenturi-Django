from django.contrib import admin
from .models import Plan, Itinerary, Activity, Guide

class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 1

class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 1

class GuideInline(admin.TabularInline):
    model = Guide
    extra = 1

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'base_price')
    search_fields = ('name',)
    list_filter = ('destination',)
    inlines = [ItineraryInline, GuideInline]

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('day', 'plan')
    search_fields = ('description',)
    list_filter = ('plan',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'itinerary', 'extra_cost')
    search_fields = ('name',)
    list_filter = ('itinerary',)

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'plan')
    search_fields = ('name',)
    list_filter = ('language',)
