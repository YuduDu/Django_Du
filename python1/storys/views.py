from django.shortcuts import render
#from django.http import HttpResponses
from django.shortcuts import render_to_response
from storys.models import Story
from django.http import Http404
# Create your views here.

def index(request):
    story_list=Story.objects.all()
    return render_to_response('storys/index.html',{'story_list':story_list})

def detail(request, story_id):
    try:
        s=Story.objects.get(pk=story_id)
    except Story.DoesNotExist:
        raise Http404
    return render_to_response('storys/detail.html',{'story':s})