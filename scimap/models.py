# -*- coding: UTF-8 -*-

import uuid

from .managers import *

# django imports
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.utils import timezone

class Area(models.Model):

	title = models.TextField(default = 'Area')

	def __str__(self):
		return self.title.encode('utf8')


class SubArea(models.Model):

	title = models.TextField(default = 'Subarea')

	def __str__(self):
		return self.title.encode('utf8')


class Node(models.Model):

	id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
	
	author = models.ForeignKey('auth.User', blank=True, null=True)
	title = models.TextField(default = 'Untitled')
	description = models.TextField(default = 'No description')

	# incoming and outcoming nodes
	inc = models.ManyToManyField('self', blank=True, symmetrical = False, related_name='+')
	out = models.ManyToManyField('self', blank=True, symmetrical = False, related_name='+')

	# sci area
	area = models.ManyToManyField(Area, blank = True, related_name = 'lvl1')
	subArea = models.ManyToManyField(SubArea, blank = True, related_name = 'lvl2')

	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)
	published = models.DateTimeField(blank=True, null=True)

	# implement custom manager
	#objects = NodeManager()

	@property
	def Type(self):
		return 'node'

	def publish(self):
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return self.title.encode('utf8') + ' ' + str(self.id)


class Route(models.Model):

	id = models.UUIDField(default = uuid.uuid4, primary_key=True, editable=False)

	title = models.TextField(default = 'Untitled')
	nodes = models.ManyToManyField(Node)

	@property
	def Type(self):
		return 'route'

	def __str__(self):
		return self.title.encode('utf8') + ' ' + str(self.id)


# check and fix one-sided relations before saving

@receiver(m2m_changed, sender = Node.inc.through)
def checkInc(instance, action, **kwargs):
	
	incArr = instance.inc.all()
	if action == 'post_add':
		
		for curNode in incArr:
			nodeForUpdating = Node.objects.get(id = curNode.id)
			targetOut = nodeForUpdating.out.all()
			
			if not instance in targetOut:
				nodeForUpdating.out.add(instance)


@receiver(m2m_changed, sender = Node.out.through)
def checkOut(instance, action, **kwargs):
	
	outArr = instance.out.all()
	if action == 'post_add':
		
		for curNode in outArr:
			nodeForUpdating = Node.objects.get(id = curNode.id)
			targetInc = nodeForUpdating.inc.all()
			
			if not instance in targetInc:
				nodeForUpdating.inc.add(instance)

