# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0043_auto_20170705_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='order',
            name='total_products',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
