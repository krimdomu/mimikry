from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class Mainboard(models.Model):
   architecture = models.CharField(max_length=10)
   vendor = models.CharField(max_length=100)
   product = models.CharField(max_length=100)
   memorysize = models.IntegerField()
   processorcount = models.IntegerField(default=1)
   maximummemory = models.IntegerField()
   system = models.ForeignKey(System)

   def __unicode__(self):
      return u'%s' % (self.name)

   class Meta:
      app_label = 'opendcm'
      permissions = (
         ("view_System", "Can view available systems"),
         )
