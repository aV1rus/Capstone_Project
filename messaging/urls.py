from django.conf.urls import url, patterns

urlpatterns = patterns('messaging.views',
   url(r'^$', 'messaging'),
)
