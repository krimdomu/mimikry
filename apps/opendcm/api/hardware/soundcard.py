from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import SoundCard as SoundCardModel
from system import System as SystemResource

class SoundCard(ModelResource):
   class Meta:
      queryset = SoundCardModel.objects.all()
      allowed_methods = ['get']

