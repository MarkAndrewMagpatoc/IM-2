from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default='')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(default='')
    image_url = models.URLField(max_length=500, default='https://images.unsplash.com/photo-1566073771259-6a8506099945')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)
    reviews_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_booked_dates(self):
        bookings = Booking.objects.filter(hotel=self, check_in_date__isnull=False)
        booked_dates = []
        for booking in bookings:
            current_date = booking.check_in_date
            while current_date <= booking.check_out_date:
                booked_dates.append(current_date.strftime('%Y-%m-%d'))
                current_date += timedelta(days=1)
        return booked_dates

class House(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default='')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(default='')
    bedrooms = models.IntegerField(default=1)
    image_url = models.URLField(max_length=500, default='https://images.unsplash.com/photo-1564013799919-ab600027ffc6')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)
    reviews_count = models.IntegerField(default=0)
    amenities = models.CharField(max_length=500, default='WiFi, Air Conditioning, Kitchen')

    def __str__(self):
        return self.name

    def get_booked_dates(self):
        bookings = Booking.objects.filter(house=self, check_in_date__isnull=False)
        booked_dates = []
        for booking in bookings:
            current_date = booking.check_in_date
            while current_date <= booking.check_out_date:
                booked_dates.append(current_date.strftime('%Y-%m-%d'))
                current_date += timedelta(days=1)
        return booked_dates

class Booking(models.Model):
    BOOKING_TYPES = (
        ('hotel', 'Hotel'),
        ('house', 'House'),
    )
    
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_type = models.CharField(max_length=5, choices=BOOKING_TYPES, default='hotel')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    check_in_date = models.DateField(null=True)
    check_out_date = models.DateField(null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    
    # Payment fields
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='credit_card')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        property_name = self.hotel.name if self.hotel else self.house.name
        return f"{self.user.username}'s booking at {property_name}"

    @staticmethod
    def has_conflict(property_type, property_id, check_in, check_out):
        if property_type == 'hotel':
            bookings = Booking.objects.filter(
                hotel_id=property_id,
                check_in_date__lte=check_out,
                check_out_date__gte=check_in
            )
        else:
            bookings = Booking.objects.filter(
                house_id=property_id,
                check_in_date__lte=check_out,
                check_out_date__gte=check_in
            )
        return bookings.exists()