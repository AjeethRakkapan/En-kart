# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0048_order_invoice_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='order_id',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
