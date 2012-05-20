from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import VideoCard as VideoCardModel
from system import System as SystemResource

class VideoCard(ModelResource):
   system = fields.ForeignKey(SystemResource, 'system', full=True)
   class Meta:
      queryset = VideoCardModel.objects.all()
      allowed_methods = ['get']

