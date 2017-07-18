# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Node)
admin.site.register(Route)
admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Link)

