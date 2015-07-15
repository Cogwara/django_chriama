from django.core.urlresolvers import reverse
from django.db import models
from seller.models import Seller

CATEGORY = ('Cars', 'Cloths', 'Computer and Electronics')


class Category(models.Model):
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=zip(sorted(CATEGORY), sorted(CATEGORY)))

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.category)


class Product(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=50, verbose_name="Name")
    category = models.ForeignKey(Category)
    description = models.TextField(verbose_name="Describe the product")
    date_listed = models.DateField(verbose_name="Date")
    listed_by = models.ForeignKey(Seller)
    photo = models.FileField(upload_to="static/image/product")
    price = models.FloatField(verbose_name='Price')

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.name)
