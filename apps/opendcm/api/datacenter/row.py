from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.datacenter import Row as RowModel
from room import Room as RoomResource

class Row(ModelResource):
   room = fields.ForeignKey(RoomResource, 'room', full=True)
   class Meta:
      queryset = RowModel.objects.all()
      allowed_methods = ['get']

