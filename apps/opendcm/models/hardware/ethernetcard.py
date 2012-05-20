from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class EthernetCard(models.Model):
   product = models.CharField(max_length=100)
   vendor = models.CharField(max_length=100)
   speed = models.IntegerField(default=1000)
   mac = models.CharField(max_length=17)
   name = models.CharField(max_length=20)
   type = models.CharField(max_length=50)
   system = models.ForeignKey(System, related_name='ethernetcards')


   def __unicode__(self):
      return u'%s' % (self.name)

   class Meta:
      app_label = 'opendcm'
      permissions = (
         ("view_ethercard", "Can view available ethercards"),
         )
