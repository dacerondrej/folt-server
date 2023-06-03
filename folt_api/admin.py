from django.contrib import admin
from .models import Customer, Courier, Offer, OfferItem, Pickup

# Register your models here.
admin.site.register(Customer)
admin.site.register(Courier)
admin.site.register(Offer)
admin.site.register(OfferItem)
admin.site.register(Pickup)
