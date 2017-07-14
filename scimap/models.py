# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
import uuid


class Node(models.Model):
	id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
	
	author = models.ForeignKey('auth.User', blank=True, null=True)
	title = models.TextField()
	description = models.TextField()

	# incoming and outcoming nodes
	inc = models.ManyToManyField('self', blank=True, null=True, related_name='out')
	out = models.ManyToManyField('self', blank=True, null=True, related_name='inc')

	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)
	published = models.DateTimeField(blank=True, null=True)

	@property
	def Type(self):
		return 'node'

	def publish(self):
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return str(self.id)

# class NodesRelationship(models.Model):
#     _from = models.ForeignKey('Node', related_name='_from')
#     _to = models.ForeignKey('Node', related_name='_to')

#     class Meta:
#         unique_together = ('_from', '_to')

class Route(models.Model):
	id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

	title = models.TextField(default='')
	nodes = models.ManyToManyField(Node)

	@property
	def Type(self):
		return 'route'

	def __str__(self):
		return str(self.id)
