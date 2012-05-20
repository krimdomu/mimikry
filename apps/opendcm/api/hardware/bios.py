from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import Bios as BiosModel
from system import System as SystemResource

class Bios(ModelResource):
   system = fields.ForeignKey(SystemResource, 'system', full=True)
   class Meta:
      queryset = BiosModel.objects.all()
      allowed_methods = ['get']

