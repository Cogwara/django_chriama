# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seller_name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('seller_phone_no', models.CharField(max_length=20, verbose_name=b'Phone')),
                ('sellers_address', models.TextField(verbose_name=b'Address')),
                ('sellers_email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('slug', models.SlugField()),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
