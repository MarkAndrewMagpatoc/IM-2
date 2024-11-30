from django.contrib import admin
from .models import UserProfile, Hotel, House, Booking

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'phone_number')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_night')
    search_fields = ('name', 'location')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_night', 'bedrooms')
    search_fields = ('name', 'location')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_type', 'check_in_date', 'check_out_date', 'total_price', 'status')
    list_filter = ('booking_type', 'status', 'booking_date')
    search_fields = ('user__username', 'hotel__name', 'house__name')
    date_hierarchy = 'booking_date'