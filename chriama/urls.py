from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', all_product, name="all_product"),
                       url(r'^(?P<product_id>\d+)/$', product_detail, name='product-detail'))
