from django.contrib import admin
from .models import User, Listings, Bids, Watchlist, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Bids)
admin.site.register(Watchlist)
admin.site.register(Comment)

