# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-03 05:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mva', '0008_auto_20160703_0354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='people_max',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservation',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mva.Session'),
        ),
    ]