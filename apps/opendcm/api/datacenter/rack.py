from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.datacenter import Rack as RackModel
from row import Row as RowResource

class Rack(ModelResource):
   row = fields.ForeignKey(RowResource, 'row', full=True)
   class Meta:
      queryset = RackModel.objects.all()
      allowed_methods = ['get']

