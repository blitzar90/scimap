from django.conf.urls import url

# from . import views

from .views import index, admin

urlpatterns = [
	# url(r'^$', views.index, name='index page'),
	# url(r'^admin/', views.admin, name='admin page'),
	url(r'^$', index, name='index page'),
	url(r'^admin/', admin, name='admin page'),
]