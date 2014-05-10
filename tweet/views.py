from django.shortcuts import render_to_response
from tweet.models import tweet
# Create your views here.

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def tweets(request):   
    List_of_tweets = tweet.objects.all()
    return render_to_response('pseudo.html', 
                            { 'List_of_tweets':  List_of_tweets })
    
    
    # index view (just redirect to login page)
def index(request):
  return HttpResponseRedirect('/login')

# this view will run after successfull login
@login_required
def logged_in(request):
    return render_to_response('logged_in.html',
        context_instance=RequestContext(request)
    )