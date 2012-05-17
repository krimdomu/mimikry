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
from opendcm.models.hardware import System

admin.site.register(ApiKey)

admin.site.register(SystemGroup)
admin.site.register(Event)
admin.site.register(NextBoot)
admin.site.register(DataCenter)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Row)
admin.site.register(Rack)
admin.site.register(System)