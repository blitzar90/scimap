from django.conf.urls import url

# from . import views

from .views import index, admin, nodes, node

urlpatterns = [
	# url(r'^$', views.index, name='index page'),
	# url(r'^admin/', views.admin, name='admin page'),
	url(r'^$', index, name='index page'),
	url(r'^node/(?P<uuid>[^/]+)/$', node, name='node'),
	url(r'^nodes/', nodes, name='nodes'),
	url(r'^cabinet/', admin, name='admin page'),
]