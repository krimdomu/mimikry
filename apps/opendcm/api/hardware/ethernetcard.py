from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import EthernetCard as EthernetCardModel
from system import System as SystemResource

class EthernetCard(ModelResource):
   system = fields.ForeignKey(SystemResource, 'system', full=True)
   class Meta:
      queryset = EthernetCardModel.objects.all()
      allowed_methods = ['get']

