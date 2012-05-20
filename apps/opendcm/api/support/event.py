from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.support import Event as EventModel
from opendcm.api.hardware import System as SystemResource

class Event(ModelResource):
   system = fields.ForeignKey(SystemResource, 'system', full=True)
   class Meta:
      queryset = EventModel.objects.all()
      allowed_methods = ['get']

