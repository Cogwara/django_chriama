from django.shortcuts import render, get_object_or_404
from .models import Product
from seller.models import Seller


def create_ad(request):
    pass

def edit_ad(request):
    pass

def delete_add(request):
    pass


def all_product(request):
    product = Product.objects.all().order_by('-date_listed')
    return render(request, 'products/product-list.html', dict(products=product))


def product_detail(request, product_id):
    detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product-detail.html', dict(product_details=detail))
