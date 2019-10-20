from django.contrib import admin
from .models import Product, Profile, Order, Basket


admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Basket)

