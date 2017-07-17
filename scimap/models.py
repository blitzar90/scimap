# -*- coding: UTF-8 -*-

import uuid
from jsonfield import JSONField

from .managers import *

# django imports
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.utils import timezone

class Link(models.Model):

	id = models.UUIDField(default = uuid.uuid4, primary_key=True, editable=False)

	title = models.TextField(default = 'Untitled')	
	description = models.TextField(default = 'No description')	
	fromNode = models.ForeignKey('Node', related_name = '+')
	toNode = models.ForeignKey('Node', related_name = '+')

	def __str__(self):
		return self.title.encode('utf8')

	# making link unique 
	class Meta:
		unique_together = ('fromNode', 'toNode')

class Area(models.Model):

	title = models.TextField(default = 'Area')

	#subs = models.

	def __str__(self):
		return self.title.encode('utf8')


class SubArea(models.Model):

	title = models.TextField(default = 'Subarea')

	#areas = models.

	def __str__(self):
		return self.title.encode('utf8')


class Node(models.Model):

	id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
	
	author = models.ForeignKey('auth.User', blank=True, null=True)
	title = models.TextField(default = 'Untitled')
	description = models.TextField(default = 'No description')

	# incoming and outcoming nodes
	fromNodes = models.ManyToManyField('self', blank=True, symmetrical = False, related_name='+')
	toNodes = models.ManyToManyField('self', blank=True, symmetrical = False, related_name='+')

	# sci area
	area = models.ManyToManyField('Area', related_name = 'areaField')
	subArea = models.ManyToManyField('Area', related_name = 'subAreaField')

	# link info
	toNodeLinkInfo=JSONField(default=dict)

	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)
	published = models.DateTimeField(blank=True, null=True)

	# implement custom manager
	#objects = NodeManager()

	@property
	def type(self):
		return 'node'

	def publish(self):
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return self.title.encode('utf8') + ' ' + str(self.id)


class Route(models.Model):

	id = models.UUIDField(default = uuid.uuid4, primary_key=True, editable=False)

	title = models.TextField(default = 'Untitled')
	nodes = models.ManyToManyField('Node')

	@property
	def type(self):
		return 'route'

	def __str__(self):
		return self.title.encode('utf8') + ' ' + str(self.id)


# check and fix one-sided relations before saving

@receiver(m2m_changed, sender = Node.fromNodes.through)
def checkFromNodes(instance, action, **kwargs):
	
	fromNodesArr = instance.fromNodes.all()
	if action == 'post_add':
		
		for curNode in fromNodesArr:
			nodeForUpdating = Node.objects.get(id = curNode.id)
			toNodesArr = nodeForUpdating.toNodes.all()
			
			# prevent loop
			if not instance in toNodesArr:
				nodeForUpdating.toNodes.add(instance)


@receiver(m2m_changed, sender = Node.toNodes.through)
def checkToNodes(instance, action, **kwargs):
	
	toNodesArr = instance.toNodes.all()
	if action == 'post_add':
		
		for curNode in toNodesArr:
			nodeForUpdating = Node.objects.get(id = curNode.id)
			fromNodesArr = nodeForUpdating.fromNodes.all()
			
			# fill links
			Link.objects.create(fromNode = instance, toNode = curNode)

			# prevent loop
			if not instance in fromNodesArr:
				nodeForUpdating.fromNodes.add(instance)

