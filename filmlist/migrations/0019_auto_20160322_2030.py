# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmlist', '0018_btdrink_btshop_shoprating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='film_name',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user_name',
        ),
        migrations.AddField(
            model_name='shoprating',
            name='drink_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='drink', to='filmlist.BTDrink'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoprating',
            name='shop_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='franchise', to='filmlist.BTShop'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Film',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
