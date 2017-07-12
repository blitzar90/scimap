# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import force_text
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.shortcuts import render
from .models import Node, Route
from .serializers import routeSerializer, nodeSerializer
import json

def index(request):
	nodes = Node.objects.order_by('created')

	return render(request, 'scimap/index.html', {
		'nodes' : list(nodes)
	})

def admin(request):
	return render(request, 'scimap/admin.html', {})

def node(request, uuid = None):
	node = model_to_dict(Node.objects.get(id=uuid))
	return render(request, 'scimap/node.html', {
		'node' : node
	})

def route(request, uuid = None):
	route = routeSerializer(Route.objects.get(id=uuid))
	return JsonResponse(route.data, safe = False)



def nodes(request):
	nodes_base_resp = Node.objects.all()
	nodes = nodeSerializer(nodes_base_resp, many = True)
	return JsonResponse(nodes.data, safe = False)

def routes(request):
	routes_base_resp = Route.objects.all()
	routes = routeSerializer(routes_base_resp, many = True)
	return JsonResponse(routes.data, safe = False)
		