# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('category', models.CharField(max_length=50, choices=[(b'Cars', b'Cars'), (b'Cloths', b'Cloths'), (b'Computer and Electronics', b'Computer and Electronics')])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Describe the product')),
                ('date_listed', models.DateField(verbose_name=b'Date')),
                ('photo', models.FileField(upload_to=b'static/image/product')),
                ('price', models.FloatField(verbose_name=b'Price')),
                ('category', models.ForeignKey(to='chriama.Category')),
                ('listed_by', models.ForeignKey(to='seller.Seller')),
            ],
        ),
    ]
