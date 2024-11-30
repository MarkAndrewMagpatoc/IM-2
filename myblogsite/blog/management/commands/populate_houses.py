from django.core.management.base import BaseCommand
from blog.models import House

class Command(BaseCommand):
    help = 'Populates the database with initial house data'

    def handle(self, *args, **kwargs):
        houses_data = [
            {
                'name': 'Modern Beachfront Villa',
                'location': 'Mactan Island, Cebu',
                'price_per_night': 450,
                'description': 'Luxurious beachfront villa with stunning ocean views, private pool, and direct beach access.',
                'bedrooms': 4,
                'image_url': 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/295090917.jpg?k=d17621b71b0eaa0c7a37d8d8d02d33896cef75145f61e7d96d296d88375a7d39&o=&hp=1',
                'rating': 4.8,
                'reviews_count': 45,
                'amenities': 'Private Pool, Beach Access, WiFi, Air Conditioning, Full Kitchen, BBQ Area'
            },
            {
                'name': 'Mountain View Cottage',
                'location': 'Busay, Cebu City',
                'price_per_night': 280,
                'description': 'Cozy mountain cottage with panoramic city views, perfect for a peaceful retreat.',
                'bedrooms': 2,
                'image_url': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/24/d9/4e/mountain-view-cottage.jpg?w=1200&h=-1&s=1',
                'rating': 4.5,
                'reviews_count': 32,
                'amenities': 'Mountain View, Garden, WiFi, Kitchen, Parking, Outdoor Seating'
            },
            {
                'name': 'City Center Penthouse',
                'location': 'Cebu Business Park',
                'price_per_night': 350,
                'description': 'Luxury penthouse in the heart of the city with modern amenities and skyline views.',
                'bedrooms': 3,
                'image_url': 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/275782754.jpg?k=38c8b6b96aef8924a7de45a31124c7b71b5c8caa602c5d2697686f7b76720644&o=&hp=1',
                'rating': 4.7,
                'reviews_count': 28,
                'amenities': 'City View, Gym Access, Pool, WiFi, Smart TV, Modern Kitchen'
            },
            {
                'name': 'Traditional Filipino House',
                'location': 'Liloan, Cebu',
                'price_per_night': 200,
                'description': 'Experience authentic Filipino living in this traditional house with modern comforts.',
                'bedrooms': 3,
                'image_url': 'https://i.pinimg.com/originals/e9/0b/b5/e90bb5b5c4a1a1d0d5a4ee6589e389c8.jpg',
                'rating': 4.4,
                'reviews_count': 25,
                'amenities': 'Garden, Traditional Architecture, WiFi, Local Experience, Full Kitchen'
            }
        ]

        for house_data in houses_data:
            House.objects.get_or_create(
                name=house_data['name'],
                defaults=house_data
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created house "{house_data["name"]}"'))
