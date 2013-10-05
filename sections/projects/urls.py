from django.conf.urls import url, patterns

urlpatterns = patterns('sections.projects.views',
   url(r'^$', 'projects'),
   url(r'^add_new', 'addNew'),
)
