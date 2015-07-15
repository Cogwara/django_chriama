from django.contrib import admin
from chriama.models import Product, Category
from seller.models import Seller

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Category)
