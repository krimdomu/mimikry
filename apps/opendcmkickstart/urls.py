from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'(?P<system_id>\d+)/$', 'opendcmkickstart.views.index')
)
