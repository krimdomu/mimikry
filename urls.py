from django.conf.urls.defaults import patterns, include, url



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mimikry_project.views.home', name='home'),
    # url(r'^mimikry_project/', include('mimikry_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # opendcm includes
    (r'^opendcm/', include('opendcm.urls')),
    
    # user auth includes
    (r'^opendcmauth/', include('opendcmauth.urls')),

    # kickstart writer
    (r'^kickstart/', include('opendcmkickstart.urls')),
    
    # home
    url(r'^$', 'opendcm.views.index')
)
