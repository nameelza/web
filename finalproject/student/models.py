from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

def __str__(self):
    return self.username

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(blank=False)
    CITY_CHOICES = [
        ('SJ', 'San Jose'),
        ('SF', 'San Francisco'),
        ('OAKLAND', 'Oakland'),
        ('FREMONT', 'Fremont'),
        ('SR', 'Santa Rosa'),
        ('HAYWARD', 'Hayward'),
        ('PALO ALTO', 'Palo Alto'),
        ('SV', 'Sunnyvale'),
        ('SC', 'Santa Clara'),
        ('VALLEJO', 'Vallejo'),
        ('CONCORD', 'Concord'),
        ('BERKELEY', 'Berkeley'),
        ('SM', 'San Mateo'),
        ('MV', 'Mountain View'),
        ('SR', 'San Rafael'),
        ('RICHMOND', 'Richmond')
    ]
    city = models.CharField(max_length=50, choices=CITY_CHOICES, blank=False)
    address = models.CharField(max_length=100, blank=False)
    PLACE_CHOICES = [
        ("SR", "Shared room"),
        ("PR", "Private room"),
        ("EP", "Entire place")
    ]
    place = models.CharField(max_length=10, choices=PLACE_CHOICES, blank=False)
    image1 = models.TextField(blank=False)
    image2 = models.TextField(blank=False)
    image3 = models.TextField(blank=False)
    image4 = models.TextField(blank=False)

class Amenities(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    wifi = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    washer = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    bike = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    gate = models.BooleanField(default=False)
    wifi_bill = models.IntegerField(default=False)
    water_bill = models.IntegerField(default=False)
    electricity_bill = models.IntegerField(default=False)
    gas_bill = models.IntegerField(default=False)
    heating_bill = models.IntegerField(default=False)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Pending")
    phone = models.CharField(max_length=20, blank=False)
    message = models.CharField(max_length=200, blank=False)


