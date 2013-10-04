from django.conf.urls import url, patterns

urlpatterns = patterns('sections.messaging.views',
   url(r'^$', 'messaging'),
)
