from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import Processor as ProcessorModel
from system import System as SystemResource

class Processor(ModelResource):
   system = fields.ForeignKey(SystemResource, 'system', full=True)
   class Meta:
      queryset = ProcessorModel.objects.all()
      allowed_methods = ['get']

