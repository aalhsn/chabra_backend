from django.contrib import admin
from .models import Product, Profile, Order, Basket


admin.site.site_header = 'Chabra Dashboard'

class ProductAdmin (admin.ModelAdmin):
	list_display = ('name', 'price', 'quantity', 'origin', 'date_added', 'active' )
	#list_display_links = ('name', 'price', 'quantity', 'date_added',)
	search_fields = ('name',)
	list_filter = ('active', 'date_added',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Basket)

