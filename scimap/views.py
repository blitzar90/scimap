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

@api_view(['POST'])
@parser_classes((JSONParser,))
def saveNode(request):
	data = request.data

	node = Node(title = data['title'])
	node.save()
		
	areaQS = Area.objects.filter(title__icontains = data['area'])

	if not len(areaQS):
		node.delete()
		return JsonResponse({'succes': False, 'reason': 'Area not found'})
	else:
		node.area.add(areaQS[0])

	if 'subarea' in data:
		
		subareaQS = SubArea.objects.filter(title__icontains = data['subarea'])		
 		print(subareaQS)
		
		if not len(subareaQS):
			node.delete()
			return JsonResponse({'succes': False, 'reason': 'subarea not found'})
		else:
			node.subArea.add(subareaQS[0])

	if 'fromNodes' in data:
		pass

	if 'toNodes' in data:
		pass


		
	return JsonResponse({'succes': True})

@api_view(['GET'])
def getByTitle(request):
    
	data = request.query_params

	if not 'type' in data:

		nodes_base_resp = Node.objects.filter(title__icontains = data['q'])
		routes_base_resp = Route.objects.filter(title__icontains = data['q'])
	  
		nodes = nodeSearchSerializer(nodes_base_resp, many = True)
		routes = routeSearchSerializer(routes_base_resp, many = True)
	
		data = nodes.data + routes.data
	
	elif data['type'] == 'node':
	
		nodes_base_resp = Node.objects.filter(title__icontains = data['q'])
	
		nodes = nodeSearchSerializer(nodes_base_resp, many = True)

		data = nodes.data

	elif data['type'] == 'route':

		routes_base_resp = Route.objects.filter(title__icontains = data['q'])
		
		routes = routeSearchSerializer(routes_base_resp, many = True)

		data = routes.data

	return JsonResponse(data, safe = False)


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
		
		if 'full' in request.data:
			
			curNode = nodeFullSerializer(curNode_base_resp)
			data.append(curNode.data)
		
		else:
			
			curNode = nodeSerializer(curNode_base_resp)
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
				if getattr(nodes.data[i],'toNodeLinkInfo', True):
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