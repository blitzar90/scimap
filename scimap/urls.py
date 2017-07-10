from django.conf.urls import url

# from . import views

from .views import index, admin, nodes

urlpatterns = [
	# url(r'^$', views.index, name='index page'),
	# url(r'^admin/', views.admin, name='admin page'),
	url(r'^$', index, name='index page'),
	url(r'^nodes/', nodes, name='nodes ajax'),
	url(r'^cabinet/', admin, name='admin page'),
]