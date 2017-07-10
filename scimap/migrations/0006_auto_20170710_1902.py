# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0005_route_nodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='nodes',
            field=models.ManyToManyField(to='scimap.Node', null=True, blank=True),
        ),
    ]
