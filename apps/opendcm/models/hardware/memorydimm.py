from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class MemoryDimm(models.Model):
   size = models.IntegerField()
   bank = models.IntegerField()
   serialnumber = models.CharField(max_length=50)
   speed = models.IntegerField()
   type = models.CharField(max_length=50)
   system = models.ForeignKey(System)

   def __unicode__(self):
      return u'%s' % (self.name)

   class Meta:
      app_label = 'opendcm'
      permissions = (
         ("view_memoryDimm", "Can view available MemoryDimm"),
         )
