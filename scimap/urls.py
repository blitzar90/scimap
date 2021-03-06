# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import *

urlpatterns = [
	
	url(r'^$', index, name='index page'),
	
	url(r'^node/(?P<uuid>[^/]+)/$', node, name='node'),
	
	url(r'^nodes/', nodes, name='nodes'),
	
	url(r'^routes/', routes, name='routes'),
	
	url(r'^links/', links, name='links'),
	
	url(r'^cabinet/', admin, name='admin page'),
	
	url(r'^api/nodes/', nodesHandler, name='nodesHandler'),
	
	url(r'^api/route/(?P<uuid>[^/]+)/$', getRouteById, name='getRouteById'),
	
	url(r'^api/search/', getByTitle, name='search')

]