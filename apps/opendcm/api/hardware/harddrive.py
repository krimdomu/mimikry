from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import HardDrive as HardDriveModel
from system import System as SystemResource

class HardDrive(ModelResource):
   class Meta:
      queryset = HardDriveModel.objects.all()
      allowed_methods = ['get']

