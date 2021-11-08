from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("closedListings", views.closedListings, name="closedListings"),
    path("myListings", views.myListings, name="myListings"),
    path("listing/<str:listing_id>",  views.listingPage, name="listingPage"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.showCategory, name="showCategory"),
    path("listing/<str:listing_id>/bid", views.bid, name="bid"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/<str:listing_id>", views.watchlistAdd, name="watchlistAdd"),
    path("listing/<str:listing_id>/close", views.close, name="close"),
    path("listing/<str:listing_id>/comment", views.comment, name="comment")
]
