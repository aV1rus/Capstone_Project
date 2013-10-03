from django.conf.urls import patterns, url,include

urlpatterns = patterns('home.views',
   url(r'^$', 'home'),
   url(r'^settings/', include('settings.urls')),
   url(r'^messaging/', include('messaging.urls')),
)