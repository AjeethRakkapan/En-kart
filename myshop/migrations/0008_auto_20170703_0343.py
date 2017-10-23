# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0007_product_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
