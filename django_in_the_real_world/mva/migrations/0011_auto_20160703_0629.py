# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-03 06:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mva', '0010_auto_20160703_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_place', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_reserved', to='mva.Session'),
        ),
    ]
