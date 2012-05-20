from django.contrib import admin
from tastypie.models import ApiKey

from opendcm.models.support import SystemGroup
from opendcm.models.support import Event
from opendcm.models.support import NextBoot

from opendcm.models.datacenter import DataCenter
from opendcm.models.datacenter import Floor
from opendcm.models.datacenter import Room
from opendcm.models.datacenter import Row
from opendcm.models.datacenter import Rack

from opendcm.models.hardware import Bios
from opendcm.models.hardware import EthernetCard
from opendcm.models.hardware import HardDrive
from opendcm.models.hardware import Mainboard
from opendcm.models.hardware import MemoryDimm
from opendcm.models.hardware import Processor
from opendcm.models.hardware import SoundCard
from opendcm.models.hardware import System
from opendcm.models.hardware import VideoCard

from opendcm.models.system import Partition
from opendcm.models.system import Profile
from opendcm.models.system import Disk

admin.site.register(ApiKey)
admin.site.register(SystemGroup)
admin.site.register(Event)
admin.site.register(NextBoot)

admin.site.register(DataCenter)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Row)
admin.site.register(Rack)
admin.site.register(Bios)

admin.site.register(EthernetCard)
admin.site.register(HardDrive)
admin.site.register(Mainboard)
admin.site.register(MemoryDimm)
admin.site.register(Processor)
admin.site.register(SoundCard)
admin.site.register(System)
admin.site.register(VideoCard)

admin.site.register(Partition)
admin.site.register(Profile)
admin.site.register(Disk)

