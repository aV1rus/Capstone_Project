from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'capstone.views.home', name='home'),
    # url(r'^capstone/', include('capstone.foo.urls')),
    url(r'^$', 'login.views.register'),
    url(r'^login/', include('login.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^logout/', "login.views.disconnect"),
    url(r'^register/', "login.views.register"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns() #Used only in debug mode