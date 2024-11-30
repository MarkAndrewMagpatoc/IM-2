# Generated by Django 4.2.7 on 2024-11-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_hotel_image_url_hotel_rating_hotel_reviews_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='amenities',
            field=models.CharField(default='WiFi, Air Conditioning, Kitchen', max_length=500),
        ),
        migrations.AddField(
            model_name='house',
            name='image_url',
            field=models.URLField(default='https://images.unsplash.com/photo-1564013799919-ab600027ffc6', max_length=500),
        ),
        migrations.AddField(
            model_name='house',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=4.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='house',
            name='reviews_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='house',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
