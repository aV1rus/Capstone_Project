from django.conf.urls import url, patterns

urlpatterns = patterns('sections.forum.views',
   url(r'^$', 'forum'),
)