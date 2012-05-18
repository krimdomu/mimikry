from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class VideoCard(models.Model):
   product = models.CharField(max_length=255)
   system = models.ForeignKey(System)

   def __unicode__(self):
      return u'%s' % (self.name)

   class Meta:
      app_label = 'opendcm'
      permissions = (
         ("view_System", "Can view available systems"),
         )
