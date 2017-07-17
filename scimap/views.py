# -*- coding: utf-8 -*-

import sys
import json
from pprint import pprint

# django imports
from django.utils.encoding import force_text
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

# rest_framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes

from .models import *
from .serializers import *


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
    routes_base_resp = Route.objects.filter(title__icontains = title)
  
    nodes = nodeSearchSerializer(nodes_base_resp, many = True)
    routes = routeSearchSerializer(routes_base_resp, many = True)

    data = nodes.data + routes.data

    return JsonResponse(data, safe = False)


# using rest decorators
@api_view(['POST'])
@parser_classes((JSONParser,))
def getNodesById(request, format=None):

	id_list = request.data['ids']
	data = list()

	for uuid in id_list:

		try:
			curNode_base_resp = Node.objects.get(id = uuid)
		except Node.DoesNotExist:
			return HttpResponse(status=404)
		
		curNode = nodePostSerializer(curNode_base_resp)
		data.append(curNode.data)

	return JsonResponse(data, safe = False)


def getRouteById(request, uuid = None):
    
    try:
		route_base_resp = Route.objects.get(id=uuid)
    except Route.DoesNotExist:
        return HttpResponse(status=404)

    route = routeSerializer(route_base_resp)
	
    return JsonResponse(route.data, safe = False)


def nodes(request):
	
	nodes_base_resp = Node.objects.all()
	nodes = nodeSerializer(nodes_base_resp, many = True)
	
	# filling toNodeLinkInfo field
	links_base_resp = Link.objects.all()
	links = linkSerializer(links_base_resp, many = True)
	for i in xrange(0, len(nodes.data)):
		for g in xrange(0, len(links.data)):
			if nodes.data[i]['id'] == str(links.data[g]['fromNode']):
				if len(nodes.data[i]['toNodeLinkInfo']) == 0:
					nodes.data[i]['toNodeLinkInfo']={
					str(links.data[g]['toNode']):{
						'title':links.data[g]['title'],
						'description':links.data[g]['description']
						}
					}
				else:
					nodes.data[i]['toNodeLinkInfo'][str(links.data[g]['toNode'])]={
						'title':links.data[g]['title'],
						'description':links.data[g]['description']
					}


	
	return JsonResponse(nodes.data, safe = False)


def routes(request):
	
	routes_base_resp = Route.objects.all()
	routes = routeSerializer(routes_base_resp, many = True)
	
	return JsonResponse(routes.data, safe = False)
		

def links(request):
	
	links_base_resp = Link.objects.all()
	links = linkSerializer(links_base_resp, many = True)
	
	return JsonResponse(links.data, safe = False)