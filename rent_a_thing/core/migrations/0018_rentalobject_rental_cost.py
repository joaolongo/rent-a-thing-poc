# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_rentalobject_is_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalobject',
            name='rental_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]