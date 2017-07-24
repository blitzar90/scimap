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

def getNodesById(searchData):

	id_list = searchData['ids']
	data = list()
	for uuid in id_list:

		try:
			curNode_base_resp = Node.objects.get(id = uuid)
		except Node.DoesNotExist:
			return False
		
		if 'full' in searchData:
			
			curNode = nodeFullSerializer(curNode_base_resp)
			data.append(curNode.data)

			return data
		
		else:
			
			curNode = nodeSerializer(curNode_base_resp)
			data.append(curNode.data)
		
	return data

def saveNode(saveData):
	data = saveData

	node = Node(title = data['title'])
	node.save()
		
	areaQS = Area.objects.filter(title__icontains = data['area'])

	if not len(areaQS):
		node.delete()
		return {'success': False, 'reason': 'Area not found'}
	else:
		node.area.add(areaQS[0])

#	if 'author' in data:
#
#		node.author = data['author']
#		node.save()

	if 'description' in data:

		node.description = data['description']
		node.save()

	if 'subarea' in data:
		
		subareaQS = SubArea.objects.filter(title__icontains = data['subarea'])		
		
		if not len(subareaQS):
			node.delete()
			return {'success': False, 'reason': 'subarea not found'}
		else:
			node.subArea.add(subareaQS[0])

	if 'fromNodes' in data:
		for strId in data['fromNodes']:
			
			try:
				curNode = Node.objects.get(id = strId)
			except Node.DoesNotExist:
				return {'success': False, 'reason': 'node with id %s not found' % strId}
			
			node.fromNodes.add(curNode)

	if 'toNodes' in data:
		print 'hello'
		for strId in data['toNodes']:
			try:
				curNode = Node.objects.get(id = strId)
			except Node.DoesNotExist:
				return {'success': False, 'reason': 'node with id %s not found' % strId}
			
			node.toNodes.add(curNode)
		
	return {'success': True}

@api_view(['POST'])
@parser_classes((JSONParser,))
def nodesHandler(request):

	if 'ids' in request.data:

		data = getNodesById(request.data)

		if not data:
			return HttpResponse(status=404)
		else:
			return JsonResponse(data, safe = False)

	else:

		data = saveNode(request.data)
		return JsonResponse(data, safe = False)

@api_view(['GET'])
def getByTitle(request):
    
	query = request.query_params

	if not 'type' in query:

		nodes_base_resp = Node.objects.filter(title__icontains = query['q'])
		routes_base_resp = Route.objects.filter(title__icontains = query['q'])
	  
		nodes = nodeSearchSerializer(nodes_base_resp, many = True)
		routes = routeSearchSerializer(routes_base_resp, many = True)
	
		data = nodes.data + routes.data
	
	elif query['type'] == 'node':
	
		nodes_base_resp = Node.objects.filter(title__icontains = query['q'])
	
		nodes = nodeSearchSerializer(nodes_base_resp, many = True)

		data = nodes.data

	elif query['type'] == 'route':

		routes_base_resp = Route.objects.filter(title__icontains = query['q'])
		
		routes = routeSearchSerializer(routes_base_resp, many = True)

		data = routes.data

	elif query['type'] == 'area':

		areas_base_resp = Area.objects.filter(title__icontains = query['q'])
		
		areas = areaSerializer(areas_base_resp, many = True)

		data = areas.data

	elif query['type'] == 'subarea':

		subareas_base_resp = SubArea.objects.filter(title__icontains = query['q'])
		
		subareas = subareaSerializer(subareas_base_resp, many = True)

		data = subareas.data


	elif query['type'] == 'link':

		links_base_resp = Link.objects.filter(title__icontains = query['q'])
		
		links = linkSerializer(links_base_resp, many = True)

		data = links.data

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