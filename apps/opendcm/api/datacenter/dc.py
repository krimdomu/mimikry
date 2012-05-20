from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.datacenter import DataCenter as DataCenterModel

class DataCenter(ModelResource):
   class Meta:
      queryset = DataCenterModel.objects.all()
      allowed_methods = ['get']

