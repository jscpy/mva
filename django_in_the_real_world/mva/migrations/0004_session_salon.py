# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-03 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mva', '0003_session_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='salon',
            field=models.CharField(blank=True, choices=[('PK', 'Salón Principal'), ('FK', 'Salón Foraneo'), ('CK', 'Salón Candidato')], max_length=10),
        ),
    ]