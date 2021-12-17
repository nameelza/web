from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list_results", views.list_results, name="list_results"),
    path("rental", views.rental, name="rental"),
    path("profile", views.profile, name="profile"),
    path("create", views.create, name="create"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]