from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import Mainboard as MainboardModel
from system import System as SystemResource

class Mainboard(ModelResource):
   system = fields.ForeignKey(SystemResource, 'system', full=True)
   class Meta:
      queryset = MainboardModel.objects.all()
      allowed_methods = ['get']

