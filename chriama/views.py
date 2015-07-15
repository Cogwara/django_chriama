from django.shortcuts import render, get_object_or_404
from .models import Product
from seller.models import Seller


def all_product(request):
    product = Product.objects.all()
    return render(request, 'products/product-list.html', dict(products=product))


def product_detail(request, product_id):
    detail = get_object_or_404(Product, pk=product_id)
    sellers = Seller.objects.all()
    return render(request, 'products/product-detail.html', dict(product_details=detail))