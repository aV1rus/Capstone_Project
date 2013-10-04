from django.conf.urls import patterns, url,include

urlpatterns = patterns('home.views',
   url(r'^$', 'home'),
   url(r'^settings/', include('sections.settings.urls')),
   url(r'^messaging/', include('sections.messaging.urls')),
   url(r'^newsfeed/', include('sections.newsfeed.urls')),
   url(r'^forum/', include('sections.forum.urls')),
   url(r'^projects/', include('sections.projects.urls')),
)