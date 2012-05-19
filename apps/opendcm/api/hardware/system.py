from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import System as SystemModel
from opendcm.api.support import NextBoot as NextBootResource

class System(ModelResource):
   next_boot = fields.ForeignKey(NextBootResource, 'next_boot', full=True)
   class Meta:
      queryset = SystemModel.objects.all()
      allowed_methods = ['get']

