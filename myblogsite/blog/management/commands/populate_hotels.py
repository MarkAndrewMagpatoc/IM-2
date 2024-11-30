from django.core.management.base import BaseCommand
from blog.models import Hotel

class Command(BaseCommand):
    help = 'Populates the database with initial hotel data'

    def handle(self, *args, **kwargs):
        hotels_data = [
            {
                'name': 'Seda Ayala Center Cebu',
                'location': 'Cebu Business Park, Cebu City',
                'price_per_night': 300,
                'description': 'Set in landscaped gardens overlooking the city, this luxurious hotel offers world-class amenities and service.',
                'image_url': 'https://pix10.agoda.net/hotelImages/5240124/-1/ffe388717201f2f96c5b9c8e1b448f6a.jpg?ca=23&ce=0&s=414x232&ar=16x9',
                'rating': 3.9,
                'reviews_count': 200
            },
            {
                'name': 'Quest Hotel and Conference Center - Cebu',
                'location': 'Archbishop Reyes Avenue, Cebu City',
                'price_per_night': 250,
                'description': 'Modern hotel with conference facilities, perfect for business and leisure travelers.',
                'image_url': 'https://lh4.googleusercontent.com/proxy/fIXt0rS7Hm9FHlQDMXW8KE3cbdJrTBkc522JZlyYgSQ2z3zl6Hzt1v15n2NbYDPNYdUIG412kd497vx-rPjdU2E5cYL73F_CTCF6E7TT3Wokiw',
                'rating': 4.3,
                'reviews_count': 150
            },
            {
                'name': 'Mezzo Hotel',
                'location': 'F. Cabahug Street, Cebu City',
                'price_per_night': 399,
                'description': 'Contemporary hotel offering stylish rooms and modern amenities in the heart of the city.',
                'image_url': 'https://ik.imagekit.io/tvlk/apr-asset/dgXfoyh24ryQLRcGq00cIdKHRmotrWLNlvG-TxlcLxGkiDwaUSggleJNPRgIHCX6/hotel/asset/20003455-517322ad156951a8f1a1f0468f86c103.jpeg?tr=q-80,c-at_max,w-740,h-500&_src=imagekit',
                'rating': 4.5,
                'reviews_count': 20
            },
            {
                'name': 'Holiday Spa Hotel',
                'location': 'F. Ramos Street, Cebu City',
                'price_per_night': 200,
                'description': 'Relaxing spa hotel offering comfortable accommodations and wellness facilities.',
                'image_url': 'https://images.trvl-media.com/lodging/5000000/4950000/4941500/4941437/e1fc7ed7.jpg?impolicy=resizecrop&rw=575&rh=575&ra=fill',
                'rating': 4.5,
                'reviews_count': 20
            }
        ]

        for hotel_data in hotels_data:
            Hotel.objects.get_or_create(
                name=hotel_data['name'],
                defaults=hotel_data
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created hotel "{hotel_data["name"]}"'))
