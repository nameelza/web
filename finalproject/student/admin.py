from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Property)
admin.site.register(Amenities)
admin.site.register(Booking)