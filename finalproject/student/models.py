from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

def __str__(self):
    return self.username

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
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
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    address = models.CharField(max_length=100)
    PLACE_CHOICES = [
        ("SR", "Shared room"),
        ("PR", "Private room"),
        ("EP", "Entire place")
    ]
    place = models.CharField(max_length=10, choices=PLACE_CHOICES)
    image1 = models.TextField(blank=False)
    image2 = models.TextField(blank=False)
    image3 = models.TextField(blank=False)
    image4 = models.TextField(blank=False)

class Amenities(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    wifi = models.BooleanField()
    kitchen = models.BooleanField()
    washer = models.BooleanField()
    gym = models.BooleanField()
    bike = models.BooleanField()
    parking = models.BooleanField()
    cctv = models.BooleanField()
    gate = models.BooleanField()
    wifi_bill = models.IntegerField()
    water_bill = models.IntegerField()
    electricity_bill = models.IntegerField()
    gas_bill = models.IntegerField()
    heating_bill = models.IntegerField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=200)


