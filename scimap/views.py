# -*- coding: utf-8 -*-

import sys

# django imports
from django.utils.encoding import force_text
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# rest_framework imports
import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Node, Route
from .serializers import routeSerializer, nodeSerializer

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

def getByTitle(request, title = None):
    nodes_base_resp = Node.objects.filter(title__icontains = title)
    nodes = nodeSerializer(nodes_base_resp, many = True)
    
    return JsonResponse(nodes.data, safe = False)

def route(request, uuid = None):
    try:
		route_base_resp = Route.objects.get(id=uuid)
    except Route.DoesNotExist:
        return HttpResponse(status=404)

    route = routeSerializer(route_base_resp)
	
    return JsonResponse(route.data, safe = False)

def nodes(request):
	nodes_base_resp = Node.objects.all()
	nodes = nodeSerializer(nodes_base_resp, many = True)
	
	return JsonResponse(nodes.data, safe = False)

def routes(request):
	routes_base_resp = Route.objects.all()
	routes = routeSerializer(routes_base_resp, many = True)
	
	return JsonResponse(routes.data, safe = False)
		