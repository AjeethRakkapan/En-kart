# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-01 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_auto_20170701_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
