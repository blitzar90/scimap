# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0008_auto_20170712_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='inc',
            field=models.ManyToManyField(related_name='_node_inc_+', to='scimap.Node', blank=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='out',
            field=models.ManyToManyField(related_name='_node_out_+', to='scimap.Node', blank=True),
        ),
    ]
