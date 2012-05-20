from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import MemoryDimm as MemoryDimmModel
from system import System as SystemResource

class MemoryDimm(ModelResource):
   system = fields.ForeignKey(SystemResource, 'system', full=True)
   class Meta:
      queryset = MemoryDimmModel.objects.all()
      allowed_methods = ['get']

