# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-03 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mva', '0012_auto_20160703_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='places_off',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
