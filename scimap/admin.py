# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Node, Route

admin.site.register(Node)
admin.site.register(Route)

# Register your models here.
