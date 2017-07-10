# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from django.shortcuts import render

from .models import Node

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


def node(request, uuid = 1):
	node = model_to_dict(Node.objects.get(id=uuid))
	return JsonResponse(node, safe=False)
