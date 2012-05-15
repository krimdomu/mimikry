from django.contrib import admin
from tastypie.models import ApiKey
from mimikry.models import Location
from mimikry.models import System
from mimikry.models import Cabinet
from mimikry.models import OSProfile

admin.site.register(ApiKey)

admin.site.register(Location)
admin.site.register(System)
admin.site.register(Cabinet)
admin.site.register(OSProfile)
