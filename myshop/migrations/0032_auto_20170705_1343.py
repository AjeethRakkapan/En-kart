# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0031_auto_20170705_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
    ]
