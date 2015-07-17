from django.shortcuts import render, get_object_or_404
from seller.models import Seller


def seller_detail(request, product_id):
    seller = get_object_or_404(Seller, pk=product_id)
    return render(request, 'seller/seller_detail.html', dict(seller=seller))
