from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import System as SystemModel
from opendcm.api.support import NextBoot as NextBootResource
from opendcm.api.support import SystemGroup as SystemGroupResource

class System(ModelResource):
   next_boot = fields.ForeignKey(NextBootResource, 'next_boot', full=True)
   system_group = fields.ForeignKey(SystemGroupResource, 'system_group', full=True)
   class Meta:
      queryset = SystemModel.objects.all()
      allowed_methods = ['get']

