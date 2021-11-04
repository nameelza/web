from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.enums import Choices


class User(AbstractUser):
    pass

class Listings(models.Model):
    CATEGORY_CHOICES = [
        ("PL", "Plants"),
        ("PT", "Pets"),
        ("FD", "Food"),
        ("HM", "Home")
    ]
    title = models.CharField(max_length=40, blank=False)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    image = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Bids(models.Model):
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.listing.title







