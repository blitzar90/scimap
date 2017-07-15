# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0014_auto_20170715_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='inc',
        ),
        migrations.RemoveField(
            model_name='node',
            name='out',
        ),
        migrations.AddField(
            model_name='node',
            name='fromNodes',
            field=models.ManyToManyField(related_name='_node_fromNodes_+', to='scimap.Node', blank=True),
        ),
        migrations.AddField(
            model_name='node',
            name='toNodes',
            field=models.ManyToManyField(related_name='_node_toNodes_+', to='scimap.Node', blank=True),
        ),
    ]
