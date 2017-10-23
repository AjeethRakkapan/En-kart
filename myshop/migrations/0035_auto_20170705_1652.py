# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0034_auto_20170705_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(decimal_places=2, default=0.085, max_digits=50),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
    ]
