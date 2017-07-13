# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import index, admin, nodes, node, routes, route, getByTitle

urlpatterns = [
	url(r'^$', index, name='index page'),
	url(r'^node/(?P<uuid>[^/]+)/$', node, name='node'),
	url(r'^route/(?P<uuid>[^/]+)/$', route, name='route'),
	url(r'^nodes/', nodes, name='nodes'),
	url(r'^routes/', routes, name='routes'),
	url(r'^api/search/(?P<title>[^/]+)/$', getByTitle, name='search'),
	url(r'^cabinet/', admin, name='admin page')
]