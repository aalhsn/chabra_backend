from django.contrib import admin
from django.db.models import Count, Sum, Min, Max, DateTimeField
from django.db.models.functions import Trunc
from .models import Product, Profile, Order, Basket, Address
from django.utils.translation import ugettext_lazy as _


admin.site.site_header = 'Chabra Dashboard'


class ProductAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'date_added', 'active' )
    #list_display_links = ('name', 'price', 'stock', 'date_added',)
    search_fields = ('name',)
    list_filter = ('active', 'date_added',)
    ordering = ['name']
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(active=True)
        if rows_updated == 1:
            message_bit = "1 product was"
        else:
            message_bit = "%s products were" % rows_updated
        self.message_user(request, "%s successfully activated." % message_bit)
    make_active.short_description = "Activate products"

    def make_inactive(self, request, queryset):
        rows_updated = queryset.update(active=False)
        if rows_updated == 1:
            message_bit = "1 product was"
        else:
            message_bit = "%s products were" % rows_updated
        self.message_user(request, "%s successfully deactived." % message_bit)
    make_inactive.short_description = "Deactivate products"



class OrderAdmin (admin.ModelAdmin):

    list_display = ('order_ref', 'customer', 'date_time', 'total' )
    search_fields = ('order_ref', 'customer',)
    list_filter = ('date_time',)
    date_hierarchy = 'date_time'


class AgeRangeListFilter(admin.SimpleListFilter):
    title = ('age')
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return (
            ('12', _('< 17 years old')),
            ('18', _('18-29 years old')),
            ('30', _('30-39 years old')),
            ('40', _('40-49 years old')),
            ('50', _('50-59 years old')),
            ('60', _('60+ years old')),
        )

    def queryset(self, request, queryset):
        if self.value() == '12':
            return queryset.filter(age__gte=0,
                                    age__lte=17)
        if self.value() == '18':
            return queryset.filter(age__gte=18,
                                    age__lte=29)
        if self.value() == '30':
            return queryset.filter(age__gte=30,
                                    age__lte=39)
        if self.value() == '40':
            return queryset.filter(age__gte=40,
                                    age__lte=49)
        if self.value() == '50':
            return queryset.filter(age__gte=50,
                                    age__lte=59)
        if self.value() == '60':
            return queryset.filter(age__gte=60)
        

class ProfileAdmin (admin.ModelAdmin):
    list_display = ('user', 'phone', 'gender', 'age',)
    search_fields = ('user',)
    list_filter = ('gender', AgeRangeListFilter,)



    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # phone = models.PositiveIntegerField(null=True)
    # gender = models.CharField(choices=GENDER, max_length=2, null=True)
    # age = models.PositiveIntegerField(null=True)
    # image = models.ImageField(null=True)

admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(Order, OrderAdmin)
admin.site.register(Basket)