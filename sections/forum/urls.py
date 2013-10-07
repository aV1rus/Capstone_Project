from django.conf.urls import url, patterns

urlpatterns = patterns('sections.forum.views',
   url(r'^$', 'forum'),
   url(r'^find/users$', 'findUsers'),
   url(r'^threads$', 'threads'),
   url(r'^threads/new$', 'thread_new'),
)
