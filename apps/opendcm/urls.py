from django.conf.urls.defaults import *
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

from opendcm.api.system import Disk as DiskResource
from opendcm.api.system import Partition as PartitionResource
from opendcm.api.system import Profile as ProfileResource

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

v1_api.register(DiskResource())
v1_api.register(PartitionResource())
v1_api.register(ProfileResource())

urlpatterns = patterns('opendcm.views',
    url (r'^$', 'index', name='opendcm_index'),
    url(r'^system/(?P<name>[-\w]+)/$', 'system', name='opendcm_system_detail'),
    
    # rest api
    url(r'^api/', include(v1_api.urls)),
)
