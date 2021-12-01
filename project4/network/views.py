from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import User, Posts, User_Followers


def index(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            content = request.POST["content"]
            user = request.user
            new_post = Posts.objects.create(user=user, content=content)
            new_post.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            posts = Posts.objects.order_by("-date").all()
            # Update likes count
            for post in posts:
                post.likesCount = post.likers.count()
                post.save()
            return render(request, "network/index.html", {
                "posts": posts
            })
    else:
        return render(request, "network/login.html")
    
def profile(request, username):
    user = User.objects.get(username=username)
    posts = Posts.objects.filter(user=user).order_by("-date")
    followers_count = User_Followers.objects.filter(user=user).count()
    following_count = User_Followers.objects.filter(follower=user).count()
    if request.user == user:
        my_profile = True
    else: 
        my_profile = False
    return render(request, "network/profile.html", {
        "profile_user": user,
        "posts": posts,
        "followers_count": followers_count,
        "following_count": following_count,
        "my_profile": my_profile
    })

def followers(request, username):
    user = User.objects.get(username=username)
    followers = User_Followers.objects.filter(user=user)
    return render(request, "network/followers.html", {
        "followers": followers,
        "profile_user": user
    })

def following(request, username):
    user = User.objects.get(username=username)
    following = User_Followers.objects.filter(follower=user)
    return render(request, "network/following.html", {
        "following": following,
        "profile_user": user
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
