# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scimap', '0011_auto_20170714_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='SubArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='lvl1',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='node',
            name='lvl2',
            field=models.TextField(default=None),
        ),
    ]
