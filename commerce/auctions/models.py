from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.enums import Choices
from django.db.models.expressions import F


class User(AbstractUser):
    pass

class Listings(models.Model):
    CATEGORY_CHOICES = [
        ("PL", "Plants"),
        ("PT", "Pets"),
        ("FD", "Food"),
        ("HM", "Home")
    ]
    title = models.CharField(max_length=60, blank=False)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    image = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    starting_bid = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Bids(models.Model):
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    bid_count = models.IntegerField(default=0, blank=False)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bidder.username} bid {self.bid_amount} on {self.listing.title}'














