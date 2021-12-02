
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<username>", views.profile, name="profile"),
    path("<username>/followers", views.followers, name="followers"),
    path("<username>/following", views.following, name="following"),
    path("<username>/follow", views.follow, name="follow")
]