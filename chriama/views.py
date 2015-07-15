from django.shortcuts import render, get_object_or_404
from .models import Product


def all_product(request):
    product = Product.objects.all()
    return render(request, 'products/product-list.html', dict(products=product))


def product_detail(request, product_id):
    detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product-detail.html', dict(product_details=detail))

def seller(request)
