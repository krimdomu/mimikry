from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class Processor(models.Model):
   modelname = models.CharField(max_length=100)
   vendor = models.CharField(max_length=50)
   flags = models.CharField(max_length=200)
   mhz = models.CharField(max_length=50)
   cache = models.IntegerField()
   system = models.ForeignKey(System)

   def __unicode__(self):
      return u'%s' % (self.name)

   class Meta:
      app_label = 'opendcm'
      permissions = (
         ("view_System", "Can view available systems"),
         )
