from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    
  url(r'^all/$', 'tweet.views.tweets'),
   
)
