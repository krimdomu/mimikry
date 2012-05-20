from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class Disk(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    system = models.ForeignKey(System, related_name='disks')
   
    def __unicode__(self):
        return u'Disk of %s (%s)' % (self.system.name, self.name)
   
    class Meta:
        app_label = 'opendcm'
        # add view permission (GET)
        permissions = (
            ("view_Disk", "Can view avaliable disks"),
            )
   
