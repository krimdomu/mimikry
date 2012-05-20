from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.datacenter import Room as RoomModel
from floor import Floor as FloorResource

class Room(ModelResource):
   floor = fields.ForeignKey(FloorResource, 'floor', full=True)
   class Meta:
      queryset = RoomModel.objects.all()
      allowed_methods = ['get']

