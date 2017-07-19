# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0003_auto_20170718_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='subarea',
            name='AreasField',
            field=models.ManyToManyField(blank=True, to='scimap.Area'),
        ),
        migrations.AlterField(
            model_name='area',
            name='title',
            field=models.TextField(default=b'Area Title'),
        ),
        migrations.AlterField(
            model_name='node',
            name='subArea',
            field=models.ManyToManyField(blank=True, related_name='subAreaField', to='scimap.SubArea'),
        ),
        migrations.AlterField(
            model_name='subarea',
            name='title',
            field=models.TextField(default=b'Subarea Title'),
        ),
    ]
