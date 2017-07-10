# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0002_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='title',
            field=models.TextField(default=b''),
        ),
    ]
