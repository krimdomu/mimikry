from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.support import SystemGroup as SystemGroupModel

class SystemGroup(ModelResource):
   parent = fields.ForeignKey('self', 'parent', full=True, null=True)
   class Meta:
      queryset = SystemGroupModel.objects.all()
      allowed_methods = ['get']

