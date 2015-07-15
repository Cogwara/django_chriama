from django import forms
from chriama.models import Product, Category, Seller


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'photo', 'price', 'slug')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('slug', 'category')

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('seller_name', 'seller_phone_no', 'sellers_address', 'sellers_email')
