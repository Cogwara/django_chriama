from django.contrib import admin
from chriama.models import *


class SellerAdmin(admin.ModelAdmin):
    search_field = ['seller_name']
    list_display = ('seller_name', 'seller_phone_no', 'sellers_address')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'listed_by', 'photo', 'price', 'date_listed')

    list_filter = ['date_listed']
    search_field = ['name']
    date_hierarchy = 'date_listed'


admin.site.register(Product, ProductAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Category)
