# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0009_auto_20170714_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='created',
        ),
        migrations.RemoveField(
            model_name='node',
            name='published',
        ),
        migrations.RemoveField(
            model_name='node',
            name='updated',
        ),
    ]
