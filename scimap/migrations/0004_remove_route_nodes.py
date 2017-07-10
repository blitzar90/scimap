# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0003_route_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='nodes',
        ),
    ]
