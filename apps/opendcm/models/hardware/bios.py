from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class Bios(models.Model):
   biosdate = models.DateTimeField()
   version = models.CharField(max_length=50)
   ssn = models.CharField(max_length=50)
   manufacturer = models.CharField(max_length=50)
   model = models.CharField(max_length=50)
   system = models.ForeignKey(System)

   def __unicode__(self):
      return u'%s' % (self.name)

   class Meta:
      app_label = 'opendcm'
      verbose_name_plural = 'bioses'
      permissions = (
         ("view_bios", "Can view available bios"),
         )
