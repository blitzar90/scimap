from django.conf.urls import url

# from . import views

from .views import index, admin, nodes, node, routes

urlpatterns = [
	# url(r'^$', views.index, name='index page'),
	# url(r'^admin/', views.admin, name='admin page'),
	url(r'^$', index, name='index page'),
	url(r'^node/(?P<uuid>[^/]+)/$', node, name='node'),
	url(r'^nodes/', nodes, name='nodes'),
	url(r'^routes/', routes, name='routes'),
	url(r'^cabinet/', admin, name='admin page'),
	#url(r'^route/(?P<uuid>[^/]+)/$', route, name='route'),
]