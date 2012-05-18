from django.db import models
from django.conf import settings
from opendcm.models.datacenter import Rack
from opendcm.models.support import SystemGroup
from opendcm.models.support import NextBoot
                
class System(models.Model):
   name = models.CharField(max_length=100)
   system_group = models.ForeignKey(SystemGroup)
   rack = models.ForeignKey(Rack)
   height = models.IntegerField(default=1)
   next_boot = models.ForeignKey(NextBoot)
   descr = models.CharField(max_length=4096, blank=True)
   
   def __unicode__(self):
       return u'%s' % (self.name)
   
   class Meta:
       app_label = 'opendcm'
       # order ascending by order
       ordering = ['name']
       # add view permission (GET)
       permissions = (
           ("view_System", "Can view avaliable systems"),
           )
   
