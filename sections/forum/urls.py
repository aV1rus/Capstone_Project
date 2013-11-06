from django.conf.urls import url, patterns

urlpatterns = patterns('sections.forum.views',
   url(r'^$', 'forum'),
   url(r'^edit', 'editComment'),
   url(r'^find/users$', 'findUsers'),
   url(r'^threads$', 'threads'),
   url(r'^threads/new$', 'thread_new'),
   url(r'^threads/view', 'thread_view'),
   url(r'^threads/link', 'linkProject'),
)
