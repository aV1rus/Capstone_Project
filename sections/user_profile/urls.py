from django.conf.urls import url, patterns

urlpatterns = patterns('sections.user_profile.views',
   url(r'^$', 'userProfile'),
)
