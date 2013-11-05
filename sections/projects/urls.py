from django.conf.urls import url, patterns

urlpatterns = patterns('sections.projects.views',
   url(r'^$', 'projects'),
   url(r'^all', 'allProjects'),
   url(r'^add_new', 'addNew'),
   url(r'^project_info', 'projectInfo'),
   url(r'^addFile', 'addFile'),
   url(r'^file_update', 'fileUpdate'),
   url(r'^file_info', 'fileInfo'),
   url(r'^invite', 'invite'),
)
