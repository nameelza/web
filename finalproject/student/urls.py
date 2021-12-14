from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list_results", views.list_results, name="list_results"),
    path("map_results",  views.map_results, name="map_results"),
    path("rental", views.rental, name="rental"),
    path("profile", views.profile, name="profile"),
    path("create", views.create, name="create")
]