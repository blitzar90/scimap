# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone

import uuid

class Node(models.Model):
	id = models.TextField(default=uuid.uuid4(), primary_key=True)
	
	author = models.ForeignKey('auth.User', blank=True, null=True)

	slug = models.TextField(blank=True, null=True)
	title = models.TextField()
	description = models.TextField()

	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)
	published = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return self.id