# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='speaker',
            name='twitter',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
