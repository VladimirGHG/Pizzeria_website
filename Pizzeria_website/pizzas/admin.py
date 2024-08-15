from django.contrib import admin

from .models import Pizza, DoughType, Burger, MeatRoast, Restaurants

admin.site.register(Pizza)
admin.site.register(DoughType)
admin.site.register(Burger)
admin.site.register(MeatRoast)
admin.site.register(Restaurants)
