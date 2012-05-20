from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.datacenter import Floor as FloorModel
from dc import DataCenter as DataCenterResource

class Floor(ModelResource):
   datacenter = fields.ForeignKey(DataCenterResource, 'datacenter', full=True)
   class Meta:
      queryset = FloorModel.objects.all()
      allowed_methods = ['get']

