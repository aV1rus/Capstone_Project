from django.conf.urls import url, patterns



urlpatterns = patterns('sections.messaging.views',
   url(r'^$', 'messaging'),
   url(r'^compose/', 'compose'),
   url(r'^view/(?P<message_id>\d+)/', 'view'),
   url(r'^compose/(?P<receiver>\d+)/', 'compose'),

)
