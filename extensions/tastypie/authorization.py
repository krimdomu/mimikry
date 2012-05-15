import logging
from tastypie.authorization import DjangoAuthorization

logger = logging.getLogger('apps')

class CustomDjangoAuthorization(DjangoAuthorization):
    
    """
    Uses permission checking from ``django.contrib.auth`` to map ``GET``, ``POST``,
    ``PUT``, and ``DELETE`` to their equivalent django auth permissions.
    """
    def is_authorized(self, request, object=None):

        klass = self.resource_meta.object_class

        # cannot check permissions if we don't know the model
        if not klass or not getattr(klass, '_meta', None):
            return True

        permission_codes = {
            'GET': '%s.view_%s',
            'POST': '%s.add_%s',
            'PUT': '%s.change_%s',
            'DELETE': '%s.delete_%s',
        }

        # cannot map request method to permission code name
        if request.method not in permission_codes:
            return True

        permission_code = permission_codes[request.method] % (
            klass._meta.app_label,
            klass._meta.module_name)
        # user must be logged in to check permissions
        # authentication backend must set request.user
        if not hasattr(request, 'user'):
            return False
        return request.user.has_perm(permission_code)
