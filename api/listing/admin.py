from django.contrib import admin
from .models import Listing, Offer, Comment

# Register your models here.
admin.site.register(Listing)
admin.site.register(Offer)
admin.site.register(Comment)
