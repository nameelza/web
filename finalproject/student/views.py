from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import *


def index(request):
    return render(request, 'student/index.html')


def list_results(request):
    return render(request, 'student/results.html')


def rental(request):
    return render(request, 'student/rental.html')


def profile(request):
    return render(request, 'student/profile.html')


def create(request):
    if request.method == "POST":
        # Create new property
        user = request.user
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        city = request.POST['city_category']
        address = request.POST['form-address']
        place = request.POST['place_category']
        image1 = request.POST['image1']
        image2 = request.POST['image2']
        image3 = request.POST['image3']
        image4 = request.POST['image4']
        print("user", user)
        print("title", title)
        print("description", description)
        print("price", price)
        print("city", city)
        print("address", address)
        print("place", place)
        print("image1", image1)
        print("image2", image2)
        print("image3", image3)
        print("image4", image4)
        pass
    else:
        city_category = Property.CITY_CHOICES
        place_category = Property.PLACE_CHOICES
        return render(request, 'student/create.html', {
            'city_category': city_category,
            'place_category': place_category
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
            return render(request, "student/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "student/login.html")


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
            return render(request, "student/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "student/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "student/register.html")
