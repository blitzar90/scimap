# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0012_auto_20170714_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.RemoveField(
            model_name='node',
            name='lvl1',
        ),
        migrations.AddField(
            model_name='node',
            name='lvl1',
            field=models.ManyToManyField(related_name='Area', to='scimap.Area'),
        ),
        migrations.RemoveField(
            model_name='node',
            name='lvl2',
        ),
        migrations.AddField(
            model_name='node',
            name='lvl2',
            field=models.ManyToManyField(related_name='SubArea', to='scimap.SubArea'),
        ),
        migrations.AlterField(
            model_name='route',
            name='title',
            field=models.TextField(default=None),
        ),
    ]
