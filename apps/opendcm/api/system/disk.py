from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.system import Disk as DiskModel

class Disk(ModelResource):
   partitions = fields.ToManyField('opendcm.api.system.partition.Partition', 'partitions', full=True, null=True)

   class Meta:
      queryset = DiskModel.objects.all()
      allowed_methods = ['get']

