# -*- coding: utf-8 -*-

from rest_framework import serializers as serializers
from .models import Route, Node

class nodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Node
		fields = '__all__'
		depth = 0

class nodeSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Node
		fields = ('id', 'Type', 'title','description' )
		depth = 0

class routeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Route
		fields = '__all__'
		depth = 0

class routeSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Route
		fields = ('id', 'Type', 'title')
		depth = 0