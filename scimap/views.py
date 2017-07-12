# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from django.shortcuts import render

from .models import Node, Route

import json


def index(request):
	nodes = Node.objects.order_by('created')

	return render(request, 'scimap/index.html', {
		'nodes' : list(nodes)
	})

def admin(request):
	return render(request, 'scimap/admin.html', {})


def nodes(request):
	nodes = list(Node.objects.order_by('created')[:20].reverse().values())
	return JsonResponse(nodes, safe=False)


def node(request, uuid = None):
	node = model_to_dict(Node.objects.get(id=uuid))
	return render(request, 'scimap/node.html', {
		'node' : node
	})

#def route(request, uuid = None):
#	route = model_to_dict(Route.objects.get(id=uuid))
#	return render(request, 'scimap/route.html', {
#		'node' : node
#	})


def routes(request):
	routes = serializers.serialize('json', Route.objects.all())
	data_unhandled = json.loads(routes)
	data=[]
	for i in xrange(0,len(data_unhandled)):
		data_unhandled[i]['fields']['id']=data_unhandled[i]['pk']
		data.append(data_unhandled[i]['fields'])
	return JsonResponse(data, safe=False)

