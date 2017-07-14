# -*- coding: UTF-8 -*-

# django imports
from django.db import models


class NodeManager(models.Manager):
    def get_queryset(self):
        return super(NodeManager, self).get_queryset().exclude(id__in = 'self.inc' )
