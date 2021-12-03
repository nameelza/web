import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Posts, User_Followers

def index(request):
    # Show all posts
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
                "posts": posts,
                "all": True
            })
    else:
        return render(request, "network/login.html")

def following_view(request):
    # Show posts from people user is following
    if request.user.is_authenticated:
        user = request.user
        following = User_Followers.objects.filter(follower=user)
        posts = []
        for follower in following:
            for post in Posts.objects.filter(user=follower.user):
                posts.append(post)
        # Order posts by date
        posts = sorted(posts, key=lambda post: post.date, reverse=True)
        print(following)
        print("posts",  posts)
        return render(request, "network/index.html",  {
            "posts": posts
        })
    else:
        return render(request, "network/login.html")
    
def profile(request, username):
    # Show user profile
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        posts = Posts.objects.filter(user=user).order_by("-date")
        followers_count = User_Followers.objects.filter(user=user).count()
        following_count = User_Followers.objects.filter(follower=user).count()
        # Check if user on own profile
        if request.user == user:
            my_profile = True
            is_following = False
        else:
            my_profile = False
            # check if user is following
            if User_Followers.objects.filter(user=user, follower=request.user).count() > 0:
                is_following = True
            else:
                is_following = False
        
        return render(request, "network/profile.html", {
            "profile_user": user,
            "posts": posts,
            "followers_count": followers_count,
            "following_count": following_count,
            "my_profile": my_profile,
            "is_following": is_following
        })
    else:
        return render(request, "network/login.html")

def followers(request, username):
    # Show followers of user
    user = User.objects.get(username=username)
    followers = User_Followers.objects.filter(user=user)
    return render(request, "network/followers.html", {
        "followers": followers,
        "profile_user": user
    })

def following(request, username):
    # Show following of user
    user = User.objects.get(username=username)
    following = User_Followers.objects.filter(follower=user)
    return render(request, "network/following.html", {
        "following": following,
        "profile_user": user
    })

@csrf_exempt
def follow(request, username):
    # Follow or unfollow user
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    else:
        user = User.objects.get(username=username)
        if request.user == user:
            return JsonResponse({"error": "Cannot follow self."}, status=400)
        follower = request.user
        if User_Followers.objects.filter(user=user, follower=follower).count() == 0:
            new_follower = User_Followers.objects.create(user=user, follower=follower)
            new_follower.save()
            print(new_follower)
        else:
            User_Followers.objects.filter(user=user, follower=follower).delete()
        return HttpResponse(status=204)
        

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
