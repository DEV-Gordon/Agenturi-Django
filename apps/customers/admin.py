from django.contrib import admin

from .models import Customer, Booking, Payment, BookingActivity

class BookingActivityInline(admin.TabularInline):
    model = BookingActivity
    extra = 1

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_date', 'status', 'customer', 'plan')
    list_filter = ('status', 'booking_date')
    search_fields = ('customer__first_name', 'customer__last_name')
    inlines = [BookingActivityInline, PaymentInline]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'payment_date', 'method', 'booking')
    search_fields = ('method',)
    list_filter = ('payment_date',)

@admin.register(BookingActivity)
class BookingActivityAdmin(admin.ModelAdmin):
    list_display = ('booking', 'activity')
