# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Node)
admin.site.register(Route)
admin.site.register(Area)
admin.site.register(SubArea)


# Register your models here.
