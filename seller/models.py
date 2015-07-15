from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Seller(models.Model):
    seller = models.ForeignKey(User)
    seller_name = models.CharField(max_length=50, verbose_name="Name")
    seller_phone_no = models.CharField(max_length=20, verbose_name="Phone")
    sellers_address = models.TextField(verbose_name="Address")
    sellers_email = models.EmailField(verbose_name="Email")
    slug = models.SlugField()
    date_joined = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('seller', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.seller_name)
