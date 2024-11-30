from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('home/', views.home, name='home'),  
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('homeaccount/', views.homeaccount, name='homeaccount'),
    path('list/', views.list, name='list'),
    path('house/', views.house, name='house'),
    path('hotel/', views.hotel, name='hotel'),
    path('booking/<int:house_id>/', views.booking, name='booking'),
    path('bookinghotel/<int:hotel_id>/', views.bookinghotel, name='bookinghotel'),
    path('done/', views.done, name='done'),
]