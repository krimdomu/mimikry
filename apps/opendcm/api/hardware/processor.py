from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import Processor as ProcessorModel
from system import System as SystemResource

class Processor(ModelResource):
   class Meta:
      queryset = ProcessorModel.objects.all()
      allowed_methods = ['get']

