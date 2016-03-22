# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 22:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmlist', '0024_remove_review_drink_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shop',
            new_name='Franchise',
        ),
        migrations.RenameField(
            model_name='drink',
            old_name='shop_name',
            new_name='franchise_name',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='shop_name',
            new_name='franchise_name',
        ),
    ]
