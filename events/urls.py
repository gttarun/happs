from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^create/$', views.create_event, name='create_event'),
]