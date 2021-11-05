from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models.aggregates import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required

from .models import User, Listings, Bids


def index(request):
    if request.user.is_authenticated:
        # Show listing of other users
        listings = Listings.objects.exclude(user=request.user).order_by('-created_at')
    else:
        # if not logged in, show all listings
        listings = Listings.objects.all().order_by('-created_at')
    return render(request, "auctions/index.html", {
        "listings": listings
    })

@login_required
def myListings(request):
    listings = Listings.objects.filter(user=request.user)
    return render(request, "auctions/myListings.html", {
        "listings": listings
    })

def listingPage(request, listing_id):
    listing = Listings.objects.get(id=listing_id)
    bid = Bids.objects.filter(listing=listing)
    return render(request, "auctions/listingpage.html", {
        "listing": listing,
        "bid": bid.order_by('-bid_amount').first(),
        "count": bid.count()
    })

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        price = request.POST['price']
        image = request.POST['image']
        user = request.user

        new_listing = Listings(title=title, description=description, category=category, image=image, starting_bid=price, user=user)
        new_listing.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        
        categories = Listings.CATEGORY_CHOICES
        return render(request, "auctions/create.html", {
            "categories": categories
        })

@login_required
def bid(request, listing_id):
    if request.method == "POST":
        listing = Listings.objects.get(id=listing_id)
        bid_amount = float(request.POST['bid'])
        user = request.user
        currentBids = Bids.objects.filter(listing=listing)

        if currentBids.count() == 0:
            if bid_amount > listing.starting_bid:
                new_bid = Bids(bid_amount=bid_amount, bidder=user, listing=listing)
                new_bid.save()
                return HttpResponseRedirect(reverse("listingPage", args=(listing_id,)))
            else:
                message = "Bid must be greater than starting bid"
                return render(request, "auctions/listingpage.html", {
                    "listing": listing,
                    "message": message
                })
        else:
            currentBid = currentBids.order_by('-bid_amount')[0]
            if bid_amount > currentBid.bid_amount:
                print("New bid is higher than current bid")
                new_bid = Bids(bid_amount=bid_amount, bidder=user, listing=listing)
                new_bid.save()
                return HttpResponseRedirect(reverse("listingPage", args=(listing_id,)))
            else:
                message = "Bid must be greater than current bid"
                return render(request, "auctions/listingpage.html", {
                    "listing": listing,
                    "bid": currentBids.order_by('-bid_amount')[0],
                    "count": currentBids.count(),
                    "message": message
                })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
