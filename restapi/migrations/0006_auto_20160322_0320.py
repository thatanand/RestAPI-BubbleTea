# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 03:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20160322_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='dateWritten',
            new_name='date_written',
        ),
    ]