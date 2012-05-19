from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class HardDrive(models.Model):
   devname = models.CharField(max_length=20)
   size = models.IntegerField()
   vendor = models.CharField(max_length=100)
   system = models.ForeignKey(System)

   def __unicode__(self):
      return u'%s' % (self.name)

   class Meta:
      app_label = 'opendcm'
      permissions = (
         ("view_harddrive", "Can view available harddrives"),
         )
