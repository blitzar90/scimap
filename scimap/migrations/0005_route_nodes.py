# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0004_remove_route_nodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='nodes',
            field=models.ManyToManyField(to='scimap.Node'),
        ),
    ]
