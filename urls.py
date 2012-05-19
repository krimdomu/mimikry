from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api

from opendcm.api.datacenter import DataCenter as DataCenterResource
from opendcm.api.datacenter import Floor as FloorResource
from opendcm.api.datacenter import Room as RoomResource
from opendcm.api.datacenter import Row as RowResource
from opendcm.api.datacenter import Rack as RackResource

from opendcm.api.hardware import System as SystemResource
from opendcm.api.hardware import Bios as BiosResource
from opendcm.api.hardware import EthernetCard as EthernetCardResource
from opendcm.api.hardware import HardDrive as HardDriveResource
from opendcm.api.hardware import Mainboard as MainboardResource
from opendcm.api.hardware import MemoryDimm as MemoryDimmResource
from opendcm.api.hardware import Processor as ProcessorResource
from opendcm.api.hardware import SoundCard as SoundCardResource
from opendcm.api.hardware import VideoCard as VideoCardResource

from opendcm.api.support import NextBoot as NextBootResource
from opendcm.api.support import Event as EventResource
from opendcm.api.support import SystemGroup as SystemGroupResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')

v1_api.register(DataCenterResource())
v1_api.register(FloorResource())
v1_api.register(RoomResource())
v1_api.register(RowResource())
v1_api.register(RackResource())

v1_api.register(SystemResource())
v1_api.register(BiosResource())
v1_api.register(EthernetCardResource())
v1_api.register(HardDriveResource())
v1_api.register(MainboardResource())
v1_api.register(MemoryDimmResource())
v1_api.register(ProcessorResource())
v1_api.register(SoundCardResource())
v1_api.register(VideoCardResource())

v1_api.register(NextBootResource())
v1_api.register(EventResource())
v1_api.register(SystemGroupResource())

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
    
    # index
    (r'^$', 'opendcm.views.index'),
    (r'^system/(?P<name>[-\w]+)/$', 'opendcm.views.detail'),
    
    
    # user auth includes
    (r'^auth/', include('userauth.urls')),
)
