# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0002_auto_20170718_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='subArea',
            field=models.ManyToManyField(blank=True, null=True, related_name='subAreaField', to='scimap.SubArea'),
        ),
    ]
