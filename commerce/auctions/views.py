from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models.aggregates import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import User, Listings, Bids, Watchlist, Comment

def index(request):
    if request.user.is_authenticated:
        # Show active listing of other users
        listings = Listings.objects.filter(is_open=True).exclude(user=request.user).order_by('-created_at')
    else:
        # if not logged in, show all active listings
        listings = Listings.objects.filter(is_open=True).order_by('-created_at')
    bids = Bids.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings,
        "message": "Active Listings",
        "message2": "No active listings"
    })

def closedListings(request):
    if request.user.is_authenticated:
        # show all closed listings of other users
        listings = Listings.objects.filter(is_open=False).exclude(user=request.user).order_by('-created_at')
    else:
        # if not logged in, show all closed listings
        listings = Listings.objects.filter(is_open=False).order_by('-created_at')
    return render(request, "auctions/index.html", {
        "listings": listings,
        "message": "Closed Listings",
        "message2": "No closed listings"
    })

@login_required
def myListings(request):
    listings = Listings.objects.filter(user=request.user)
    return render(request, "auctions/index.html", {
        "listings": listings,
        "message": "My Listings",
        "message2": "You have no listings"
    })


def listingPage(request, listing_id):
    # if user is logged in, show the listing
    if request.user.is_authenticated:
        user = request.user
        listing = Listings.objects.get(id=listing_id)
        category = listing.get_category_display()
        bid = Bids.objects.filter(listing=listing)
        comments = Comment.objects.filter(listing=listing)
        # check if listing is in watchlist
        if Watchlist.objects.filter(user=request.user, listing=listing).exists():
            inWatchlist = True
        else:
            inWatchlist = False
        
        # check if user is the listing owner
        if listing.user == request.user:
            isOwner = True
        else:
            isOwner = False
        

        return render(request, "auctions/listingpage.html", {
            "listing": listing,
            "category": category,
            "bid": bid.order_by('-bid_amount').first(),
            "count": bid.count(),
            "inWatchlist": inWatchlist,
            "isOwner": isOwner,
            "user": user,
            "comments": comments
        })

    else:
        return render(request, "auctions/login.html", {
            "message": "Log in to view listings and make bids."
        })

def categories(request):
    categories = Listings.CATEGORY_CHOICES
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

def showCategory(request, category):
    listings = Listings.objects.filter(category=category)
    if listings.count() != 0:
        categoryName = listings.first().get_category_display()
    else:
        message2 = "No listings in this category"
        categoryName = "No listings yet"
    return render(request, "auctions/index.html", {
        "listings": listings,
        "message": categoryName
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
def comment(request, listing_id):
    if request.method == "POST":
        comment = request.POST['comment']
        listing = Listings.objects.get(id=listing_id)
        new_comment = Comment(user=request.user, listing=listing, comment=comment)
        new_comment.save()

        return HttpResponseRedirect(reverse("listingPage", args=(listing_id,)))

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
                message = "Bid must be greater than price"
                category = listing.get_category_display()
                if Watchlist.objects.filter(user=request.user, listing=listing).exists():
                    inWatchlist = True
                else:
                    inWatchlist = False
                return render(request, "auctions/listingpage.html", {
                    "listing": listing,
                    "message": message,
                    "category": category,
                    "inWatchlist": inWatchlist
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
                category = listing.get_category_display()
                if Watchlist.objects.filter(user=request.user, listing=listing).exists():
                    inWatchlist = True
                else:
                    inWatchlist = False
                return render(request, "auctions/listingpage.html", {
                    "listing": listing,
                    "bid": currentBids.order_by('-bid_amount')[0],
                    "count": currentBids.count(),
                    "category": category,
                    "inWatchlist": inWatchlist,
                    "message": message
                })

def close(request, listing_id):
    listing = Listings.objects.get(id=listing_id)
    listing.is_open = False
    listing.save()
    return HttpResponseRedirect(reverse("listingPage", args=(listing_id,)))

@login_required
def watchlistAdd(request, listing_id):
    listing = Listings.objects.get(id=listing_id)
    user = request.user
    if Watchlist.objects.filter(listing=listing, user=user).count() == 0:
        new_watchlist = Watchlist(listing=listing, user=user)
        new_watchlist.save()
    else:
        Watchlist.objects.filter(listing=listing, user=user).delete()
    return HttpResponseRedirect(reverse("listingPage", args=(listing_id,)))

@login_required
def watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist
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
