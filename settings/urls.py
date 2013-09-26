from django.conf.urls import url, patterns

urlpatterns = patterns('settings.views',
   url(r'^$', 'settings'),
)
