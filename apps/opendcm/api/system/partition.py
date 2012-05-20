from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.system import Partition as PartitionModel

class Partition(ModelResource):
   class Meta:
      queryset = PartitionModel.objects.all()
      allowed_methods = ['get']

