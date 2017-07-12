# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0006_auto_20170710_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='inc',
            field=models.ManyToManyField(related_name='_node_inc_+', to='scimap.Node'),
        ),
        migrations.AddField(
            model_name='node',
            name='out',
            field=models.ManyToManyField(related_name='_node_out_+', to='scimap.Node'),
        ),
        migrations.AlterField(
            model_name='route',
            name='nodes',
            field=models.ManyToManyField(to='scimap.Node'),
        ),
    ]
