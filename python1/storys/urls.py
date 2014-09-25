from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from storys import views
from storys.models import Story

urlpatterns =patterns('',
	url(r'^$', 
		ListView.as_view(
			model=Story,
			template_name='storys/index.html'),
		name='index'),
	
	url(r'^(?P<pk>\d+)/$',
		DetailView.as_view(
			model=Story,
			template_name='storys/detail.html'),
		name='detail'),
		
	url(r'^(?P<story_id>\d+)/comm/$', views.comm, name='comm'),
	url(r'^(?P<story_id>\d+)/back/$', views.back, name='back'),
	url(r'^newstory/$', views.newstory, name='newstory'),
)