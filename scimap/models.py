# -*- coding: UTF-8 -*-

import uuid

from .managers import *

# django imports
from django.db import models
#from django import forms
from django.utils import timezone

class Area(models.Model):

	title = models.TextField(default =None)

	def __str__(self):
		return self.title


class SubArea(models.Model):

	title = models.TextField(default=None)

	def __str__(self):
		return self.title


class Node(models.Model):

	id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
	
	author = models.ForeignKey('auth.User', blank=True, null=True)
	title = models.TextField()
	description = models.TextField(default=None)

	# incoming and outcoming nodes
	inc = models.ManyToManyField('self', blank=True, symmetrical = False, related_name='+')
	out = models.ManyToManyField('self', blank=True, symmetrical = False, related_name='+')

	# sci area
	lvl1 = models.ManyToManyField(Area, related_name = 'Area')
	lvl2 = models.ManyToManyField(SubArea, related_name = 'SubArea')

	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)
	published = models.DateTimeField(blank=True, null=True)

	objects = NodeManager()

	@property
	def Type(self):
		return 'node'

	def publish(self):
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return str(self.id)


class Route(models.Model):

	id = models.UUIDField(default = uuid.uuid4, primary_key=True, editable=False)

	title = models.TextField(default = None)
	nodes = models.ManyToManyField(Node)

	@property
	def Type(self):
		return 'route'

	def __str__(self):
		return str(self.id)
