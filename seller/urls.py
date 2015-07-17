from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^(?P<product_id>\d+)/$', seller_detail, name='seller-detail'),
                       )
