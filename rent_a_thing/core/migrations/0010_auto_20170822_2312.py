# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 02:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='price',
            new_name='value',
        ),
    ]
