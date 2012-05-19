from tastypie.resources import ModelResource
from opendcm.models.support import NextBoot as NextBootModel

class NextBoot(ModelResource):
   class Meta:
      queryset = NextBootModel.objects.all()
      allowed_methods = ['get']

