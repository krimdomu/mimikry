from django.contrib import admin
from tastypie.models import ApiKey
from opendcm.models import System
from opendcm.models import Cabinet
from opendcm.models import OSProfile
from opendcm.models.datacenter import DataCenter
from opendcm.models.datacenter import Floor
from opendcm.models.datacenter import Room
from opendcm.models.datacenter import Row
from opendcm.models.datacenter import Rack

admin.site.register(ApiKey)

admin.site.register(DataCenter)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Row)
admin.site.register(Rack)
