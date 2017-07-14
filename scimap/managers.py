# -*- coding: UTF-8 -*-

# django imports
from django.db import models


class NodeManager(models.Manager):
    
    def get_queryset(self):
        
        standard =super(NodeManager, self).get_queryset()

        res = standard

        return res
