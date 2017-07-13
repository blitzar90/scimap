# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import *

urlpatterns = [
	
	url(r'^$', index, name='index page'),
	
	url(r'^node/(?P<uuid>[^/]+)/$', node, name='node'),
	
	url(r'^nodes/', nodes, name='nodes'),
	
	url(r'^routes/', routes, name='routes'),
	
	url(r'^cabinet/', admin, name='admin page'),
	
	url(r'^api/nodes/', getNodesById, name='getNodesById'),
	
	url(r'^api/route/(?P<uuid>[^/]+)/$', getRouteById, name='getRouteById'),
	
	url(r'^api/search/(?P<title>[^/]+)/$', getByTitle, name='search'),
]