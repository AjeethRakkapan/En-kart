# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-04 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0019_auto_20170704_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='myshop/product/featured')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('text', models.CharField(blank=True, max_length=220, null=True)),
                ('text_right', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Product')),
            ],
        ),
    ]
