# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='subArea',
            field=models.ManyToManyField(blank=True, null=True, related_name='subAreaField', to='scimap.Area'),
        ),
    ]