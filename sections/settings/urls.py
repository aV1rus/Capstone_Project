from django.conf.urls import url, patterns

urlpatterns = patterns('sections.settings.views',
   url(r'^$', 'settings'),
)
