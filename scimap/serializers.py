# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import serializers as rest_serializers
from .models import Route, Node

class nodeSerializer(rest_serializers.ModelSerializer):
	class Meta:
		model = Node
		fields = '__all__'
		depth = 0

class routeSerializer(rest_serializers.ModelSerializer):
	class Meta:
		model = Route
		fields = '__all__'
		depth = 0
