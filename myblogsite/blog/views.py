from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Hotel, House, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from datetime import datetime

def home(request):
    return render(request, "home.html")

@login_required
def homeaccount(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, "homeaccount.html", {'bookings': user_bookings})

def list(request):
    hotels = Hotel.objects.all()
    houses = House.objects.all()
    return render(request, "list.html", {'hotels': hotels, 'houses': houses})

def house(request):
    houses = House.objects.all()
    return render(request, "house.html", {'houses': houses})

def hotel(request):
    hotels = Hotel.objects.all()
    return render(request, "hotel.html", {'hotels': hotels})

@login_required
def booking(request, house_id):
    house = get_object_or_404(House, id=house_id)
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        
        # Convert string dates to datetime objects
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()

        # Check for booking conflicts
        if Booking.has_conflict('house', house_id, check_in_date, check_out_date):
            messages.error(request, 'This house is not available for the selected dates.')
            return render(request, "booking.html", {
                'property': house,
                'booked_dates': house.get_booked_dates()
            })
        
        # Calculate total price
        nights = (check_out_date - check_in_date).days
        total_price = house.price_per_night * nights
        
        # Create booking
        booking = Booking.objects.create(
            user=request.user,
            booking_type='house',
            house=house,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            total_price=total_price
        )
        
        messages.success(request, f'Successfully booked {house.name} for {nights} nights!')
        return redirect('done')
    
    today = datetime.now().date()
    return render(request, "booking.html", {
        'property': house,
        'booked_dates': house.get_booked_dates(),
        'today': today
    })

@login_required
def bookinghotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        
        if check_in and check_out:
            # Convert string dates to datetime objects
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()

            # Check for booking conflicts
            if Booking.has_conflict('hotel', hotel_id, check_in_date, check_out_date):
                messages.error(request, 'This hotel is not available for the selected dates.')
                return render(request, 'bookinghotel.html', {
                    'property': hotel,
                    'booked_dates': hotel.get_booked_dates()
                })
            
            # Calculate total price
            nights = (check_out_date - check_in_date).days
            total_price = hotel.price_per_night * nights
            
            # Create booking
            booking = Booking.objects.create(
                user=request.user,
                booking_type='hotel',
                hotel=hotel,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                total_price=total_price
            )
            
            messages.success(request, f'Successfully booked {hotel.name} for {nights} nights!')
            return redirect('done')
        else:
            messages.error(request, 'Please select check-in and check-out dates.')
    
    today = datetime.now().date()
    return render(request, 'bookinghotel.html', {
        'property': hotel,
        'booked_dates': hotel.get_booked_dates(),
        'today': today
    })

def done(request):
    return render(request, "done.html")

def signup(request):
    print('SIGNING UP....')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        # Validate password
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('signup')

        # Create the User
        my_user = User.objects.create_user(username=username, email=email, password=pass1)
        my_user.save()

        # Create the UserProfile linked to the User
        UserProfile.objects.create(user=my_user)

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')
    else: 
        return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("homeaccount")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")
    
    return render(request, "login.html")