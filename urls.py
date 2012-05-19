from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from opendcm.api.hardware import System as SystemResource
from opendcm.api.support import NextBoot as NextBootResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(SystemResource())
v1_api.register(NextBootResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mimikry_project.views.home', name='home'),
    # url(r'^mimikry_project/', include('mimikry_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # rest api
    (r'^api/', include(v1_api.urls)),
)
