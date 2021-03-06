# -*- coding: UTF-8 -*-

from .models import *

# rest_framework imports
from rest_framework import serializers as serializers


# supplementary classes

class toNodesField(serializers.RelatedField):
	def to_representation(self, value):
		return value.id

class fromNodesField(serializers.RelatedField):
	def to_representation(self, value):
		return value.id


#general serializers

class nodeSerializer(serializers.ModelSerializer):

	toNodes = toNodesField(many=True, read_only=True)
	fromNodes = fromNodesField(many=True, read_only=True)
	
	class Meta:
		model = Node
		fields = '__all__'
		depth = 1

class nodeFullSerializer(serializers.ModelSerializer):

	toNodes = nodeSerializer(many=True, read_only=True)
	fromNodes = nodeSerializer(many=True, read_only=True)

	class Meta:
		model = Node
		fields = '__all__'
		depth = 1

		
class routeSerializer(serializers.ModelSerializer):

	nodes = nodeSerializer(many=True, read_only=True)

	class Meta:
		model = Route
		fields = '__all__'
		depth = 1


class linkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Link
		fields = '__all__'
		depth = 1

class areaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Area
		fields = '__all__'
		depth = 1

class subareaSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubArea
		fields = '__all__'
		depth = 1


# search serializers with type

class nodeSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Node
		fields = ('id', 'type', 'title','description')
		depth = 0


class routeSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Route
		fields = ('id', 'type', 'title', 'description')
		depth = 0

