from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from storys.models import Story, Comment
from django.http import Http404
from django.core.urlresolvers import reverse
# Create your views here.

'''def index(request):
    story_list=Story.objects.all()
    return render_to_response('storys/index.html',{'story_list':story_list})

def detail(request, story_id):
    try:
        s=Story.objects.get(pk=story_id)
    except Story.DoesNotExist:
        raise Http404
    return render_to_response('storys/detail.html',{'story':s})'''
    
def comm(request, story_id):
    s=get_object_or_404(Story, pk=story_id)
    if request.POST['comment']:
    	s.comment_set.create(Comment_text=request.POST['comment'])
    	return render(request,'storys/detail.html',{
    	'story':s,
    	})
    else:
    	return render(request,'storys/detail.html',{
    	'story':s,
    	'error_message':"Please write somthing and try again.",
    	})
    	
    	
def back(request,story_id):
	return HttpResponseRedirect(reverse('index'))
	
def newstory(request):
	if request.POST['title'] and request.POST['content']:
		p=Story(title=request.POST['title'], content=request.POST['content'])
		p.save()
		return HttpResponseRedirect(reverse('index'))
	else:
		return render(request,'storys/index.html',{
		'story_list': Story.objects.all(),
    	'error_message':"Please write somthing and try again.",})	