# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0013_auto_20170714_2355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='lvl1',
            new_name='area',
        ),
        migrations.RemoveField(
            model_name='node',
            name='lvl2',
        ),
        migrations.AddField(
            model_name='node',
            name='subArea',
            field=models.ManyToManyField(related_name='SubArea', to='scimap.SubArea', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='title',
            field=models.TextField(default=b'Area'),
        ),
        migrations.AlterField(
            model_name='node',
            name='description',
            field=models.TextField(default=b'No description'),
        ),
        migrations.AlterField(
            model_name='node',
            name='title',
            field=models.TextField(default=b'Untitled'),
        ),
        migrations.AlterField(
            model_name='route',
            name='title',
            field=models.TextField(default=b'Untitled'),
        ),
        migrations.AlterField(
            model_name='subarea',
            name='title',
            field=models.TextField(default=b'Subarea'),
        ),
    ]
