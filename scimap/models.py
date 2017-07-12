# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone

import uuid

class Node(models.Model):
	id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
	
	author = models.ForeignKey('auth.User', blank=True, null=True)
	title = models.TextField()
	description = models.TextField()


	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)
	published = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return str(self.id)


class Route(models.Model):
	id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

	title = models.TextField(default='')

	nodes = models.ManyToManyField(Node)

	def __str__(self):
		return str(self.id)
