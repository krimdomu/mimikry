from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.system import Profile as ProfileModel

class Profile(ModelResource):
   class Meta:
      queryset = ProfileModel.objects.all()
      allowed_methods = ['get']

